import io
import logging
import numpy as np
#import tensorflow
from PIL import Image,UnidentifiedImageError 
from django.conf import settings
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.efficientnet import preprocess_input
from skinvision_api import settings
from . import class_config

from . import class_config

logger = logging.getLogger(__name__)
IMG_SIZE = (224, 224) 
_model = None


def get_model():    # load the model
    global _model
    if _model is None:
        logger.info('Loading SkinVision model from %s', settings.ML_MODEL_PATH)
        _model = load_model(settings.ML_MODEL_PATH)

        dummy = np.zeros((1,*IMG_SIZE, 3), dtype=np.float32)
        _model.predict(dummy,verbose=0)
        logger.info('Model loaded and warmed up')
    return _model


class InvalidImageError(Exception):
    pass 


def preprocess_image(file_obj):
    try:
        # file_obj.seek(0)
        # img = Image.open(io.BytesIO(file_obj.read()))
        # img.verify()
        # file_obj.seek(0)
        # img = Image.open(io.BytesIO(file_obj.read()))

        file_obj.seek(0)
        image_bytes = file_obj.read()
        img = Image.open(io.BytesIO(image_bytes))
        img.verify()
        img = Image.open(io.BytesIO(image_bytes))

    except (UnidentifiedImageError,OSError,IOError) as e:
        raise InvalidImageError(f'Uploaded file is not a valid image: {e}')
    
    try:
        img = img.convert('RGB')
        img = img.resize(IMG_SIZE)
        arr = np.array(img,dtype=np.float32)
        arr = preprocess_input(arr)
        arr = np.expand_dims(arr, axis=0)
        return arr 
    except Exception as e:
        raise InvalidImageError(f"Failed to preprocess image: {e}")
    



default_rec = {
    "Causes & Symptoms": "There could be certain cases",
    "Treatment": "Consult a dermatologist.",
    "Prevention": "Maintain healthy skin habits."
}

def predict_top_k(file_obj,k=3):
    arr = preprocess_image(file_obj)
    model = get_model()

    try:
        preds = model.predict(arr,verbose=0)[0]
    except Exception as e:
        logger.exception("Model inference failed")
        raise RuntimeError(f"Model inference failed: {e}")
    
    top_indices = preds.argsort()[-k:][::-1]
    results = []

    for idx in top_indices:
        idx = int(idx)
        if idx >= len(class_config.CLASS_NAMES):
            continue
        class_name = class_config.CLASS_NAMES[idx]
        confidence = float(preds[idx])
        rec = class_config.RECOMMENDATIONS.get(class_name, default_rec)
        results.append({
            "class": class_name,
            "confidence": round(confidence, 4),
            "causes & symptoms":rec["Causes & Symptoms"],
            "treatment": rec["Treatment"],
            "prevention": rec["Prevention"],
        })
    return results


        




