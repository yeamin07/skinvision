from rest_framework import serializers

MAX_UPLOAD_SIZE_MB = 5
ALLOWED_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.bmp', '.webp')

class ImageUploadSerializer(serializers.Serializer):
    image = serializers.ImageField()

    def validate_image(self,value):
        if value.size > MAX_UPLOAD_SIZE_MB * 1024 * 1024:
            raise serializers.ValidationError(
                f"Image too large (max {MAX_UPLOAD_SIZE_MB}MB)."
            )
        if not value.name.lower().endswith(ALLOWED_EXTENSIONS):
            raise serializers.ValidationError(
                f"Unsupported file type. Allowed: {ALLOWED_EXTENSIONS}"
            )
         
        return value