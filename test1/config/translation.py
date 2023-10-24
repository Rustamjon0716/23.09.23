from modeltranslation.translator import translator, TranslationOptions
from polls.models import NewsModel

class TestModelTranslation(TranslationOptions):
    fields = ("title",)


translator.register(NewsModel , TestModelTranslation)
