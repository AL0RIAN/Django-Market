from django import forms
from django.utils.translation import gettext_lazy as _


class CouponsApplyForm(forms.Form):
    code = forms.CharField(label=_('Coupons'))
