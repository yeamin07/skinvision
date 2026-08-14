import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from . import class_config

from .serializers import ImageUploadSerializer
from .ml_utils import predict_top_k, InvalidImageError

logger = logging.getLogger(__name__)


class PredictSkinDiseaseView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        serializer = ImageUploadSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {"success": False, "errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

        image_file = serializer.validated_data["image"]

        try:
            k=3
            k = min(k, len(class_config.CLASS_NAMES))
            predictions = predict_top_k(image_file, k)
        except InvalidImageError as e:
            return Response(
                {"success": False, "error": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except RuntimeError as e:
            logger.exception("Inference error")
            return Response(
                {"success": False, "error": "Model inference failed. Please try again."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        except Exception as e:
            logger.exception("Unexpected error during prediction")
            return Response(
                {"success": False, "error": "Unexpected server error."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        return Response(
            {
                "success": True,
                "predictions": predictions,
                "top_prediction": predictions[0] if predictions else None,
            },
            status=status.HTTP_200_OK,
        )


class HealthCheckView(APIView):
    def get(self, request):
        return Response({"status": "ok"})
    
