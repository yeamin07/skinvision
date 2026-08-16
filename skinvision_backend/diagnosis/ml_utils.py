# import io
# import logging
# import numpy as np
# #import tensorflow
# from PIL import Image,UnidentifiedImageError 
# from django.conf import settings
# from tensorflow.keras.models import load_model
# from tensorflow.keras.applications.efficientnet import preprocess_input
# from skinvision_api import settings
# from . import class_config

# from . import class_config

# logger = logging.getLogger(__name__)
# IMG_SIZE = (224, 224) 
# _model = None


# def get_model():    # load the model
#     global _model
#     if _model is None:
#         logger.info('Loading SkinVision model from %s', settings.ML_MODEL_PATH)
#         _model = load_model(settings.ML_MODEL_PATH)

#         dummy = np.zeros((1,*IMG_SIZE, 3), dtype=np.float32)
#         _model.predict(dummy,verbose=0)
#         logger.info('Model loaded and warmed up')
#     return _model


# class InvalidImageError(Exception):
#     pass 


# def preprocess_image(file_obj):
#     try:
#         # file_obj.seek(0)
#         # img = Image.open(io.BytesIO(file_obj.read()))
#         # img.verify()
#         # file_obj.seek(0)
#         # img = Image.open(io.BytesIO(file_obj.read()))

#         file_obj.seek(0)
#         image_bytes = file_obj.read()
#         img = Image.open(io.BytesIO(image_bytes))
#         img.verify()
#         img = Image.open(io.BytesIO(image_bytes))

#     except (UnidentifiedImageError,OSError,IOError) as e:
#         raise InvalidImageError(f'Uploaded file is not a valid image: {e}')
    
#     try:
#         img = img.convert('RGB')
#         img = img.resize(IMG_SIZE)
#         arr = np.array(img,dtype=np.float32)
#         arr = preprocess_input(arr)
#         arr = np.expand_dims(arr, axis=0)
#         return arr 
#     except Exception as e:
#         raise InvalidImageError(f"Failed to preprocess image: {e}")
    



# default_rec = {
#     "Causes & Symptoms": "There could be certain cases",
#     "Treatment": "Consult a dermatologist.",
#     "Prevention": "Maintain healthy skin habits."
# }

# def predict_top_k(file_obj,k=3):
#     arr = preprocess_image(file_obj)
#     model = get_model()

#     try:
#         preds = model.predict(arr,verbose=0)[0]
#     except Exception as e:
#         logger.exception("Model inference failed")
#         raise RuntimeError(f"Model inference failed: {e}")
    
#     top_indices = preds.argsort()[-k:][::-1]
#     results = []

#     for idx in top_indices:
#         idx = int(idx)
#         if idx >= len(class_config.CLASS_NAMES):
#             continue
#         class_name = class_config.CLASS_NAMES[idx]
#         confidence = float(preds[idx])
#         rec = class_config.RECOMMENDATIONS.get(class_name, default_rec)
#         results.append({
#             "class": class_name,
#             "confidence": round(confidence, 4),
#             "causes & symptoms":rec["Causes & Symptoms"],
#             "treatment": rec["Treatment"],
#             "prevention": rec["Prevention"],
#         })
#     return results


        



import logging
import io
import numpy as np
from PIL import Image

logger = logging.getLogger(__name__)

# Global variable to cache the model
_model = None

def get_model():
    """Lazy load the model only when needed"""
    global _model
    
    if _model is None:
        try:
            # Import TensorFlow only when first needed
            import keras
            logger.info("Loading TensorFlow model...")
            _model = keras.models.load_model('path/to/your/model.h5')
            logger.info("Model loaded successfully")
        except Exception as e:
            logger.error(f"Failed to load model: {e}")
            raise
    
    return _model

def predict_top_k(image_file, k=3):
    """Predict skin disease from image"""
    try:
        # Get the lazy-loaded model
        model = get_model()
        
        # Read and preprocess image
        image = Image.open(io.BytesIO(image_file.read()))
        image = image.resize((224, 224))
        image_array = np.array(image) / 255.0
        
        # Handle both RGB and RGBA
        if image_array.shape[2] == 4:
            image_array = image_array[:, :, :3]
        
        image_array = np.expand_dims(image_array, axis=0)
        
        # Make prediction
        predictions = model.predict(image_array)
        
        # Get top k predictions
        from . import class_config
        top_k_indices = np.argsort(predictions[0])[-k:][::-1]
        
        results = [
            {
                'class': class_config.CLASS_NAMES[idx],
                'confidence': float(predictions[0][idx])
            }
            for idx in top_k_indices
        ]
        
        return results
        
    except InvalidImageError as e:
        raise InvalidImageError(str(e))
    except Exception as e:
        logger.exception("Prediction error")
        raise RuntimeError(f"Model inference failed: {str(e)}")


