from django.apps import AppConfig


class CandidateConfig(AppConfig):
    '''Configuration for the 'candidate' app.

    Attributes:
        default_auto_field (str): The name of the default auto field to use for models.
        name (str): The name of the 'candidate' app.

    Usage:
        This configuration class is used to specify settings for the 'candidate' app within Django.
   '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'candidate'
