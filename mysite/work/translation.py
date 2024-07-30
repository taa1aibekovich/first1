from .models import UserProfile
from modeltranslation.translator import TranslationOptions,register


@register(UserProfile)
class ProductTranslationOptions(TranslationOptions):
    fields = ('nickname', 'biografi')
