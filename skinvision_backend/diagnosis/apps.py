from django.apps import AppConfig
import os 


class DiagnosisConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'diagnosis'

    def ready(self):
        if os.environ.get('RUN_MAIN') != 'true':
            return 
        from . import ml_utils
        ml_utils.get_model()
