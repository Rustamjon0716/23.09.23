from modeltranslation.translator import translator, TranslationOptions
from polls.models import *

class LaptopTranslation(TranslationOptions):
    fields = ("__all__",)


translator.register(LaptopModel , LaptopTranslation)
