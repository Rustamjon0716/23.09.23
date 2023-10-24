from modeltranslation.translator import translator, TranslationOptions
from app1.models import *

class task_namelTranslation(TranslationOptions):
    fields = ("__all__",)


translator.register(task_name , task_namelTranslation)
