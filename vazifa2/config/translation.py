from modeltranslation.translator import translator, TranslationOptions
from polls.models import *

class BookTranslation(TranslationOptions):
    fields = ("__all__",)


translator.register(BookModel , BookTranslation),
translator.register(AuthorModel , )

