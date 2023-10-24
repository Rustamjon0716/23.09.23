from modeltranslation.translator import translator, TranslationOptions
from app1.models import *

class SiyosiyTranslation(TranslationOptions):
    fields = ("__all__",)

class IjtimoiyTraslation(TranslationOptions):
    field = ("__all__",) 


translator.register(SiyosiyNewModel , SiyosiyTranslation)
translator.register(IjtimoiyNewModels , IjtimoiyTraslation)

