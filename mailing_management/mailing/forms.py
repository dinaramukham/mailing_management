from django import forms
from .models import  Mailing, Client

class ClientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class']='form-control'
    class Meta:
        model=Client
        fields='__all__'
class MailingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class']='form-control'
    class Meta:
        model=Mailing
        fields='__all__'