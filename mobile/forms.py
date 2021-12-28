from django import forms

# creating a form


from django import forms
from mobile.models import Mobile


class Form(forms.ModelForm):
    class Meta:
        model = Mobile
        fields = "__all__"
