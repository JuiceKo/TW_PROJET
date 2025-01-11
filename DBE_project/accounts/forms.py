from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


class accounts(ModelForm):
    class Meta:
        model=models.login
        fields=('Pseudo','Password')
        labels = {
            'Pseudo': _('Pseudo:'),
            'Password': _('Password:'),
        }
