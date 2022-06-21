from django import forms
from website.models import ContactoModel

class ContactosForm(forms.ModelForm):
    nome = forms.CharField()
    email = forms.EmailField()
    mensagem = forms.CharField()

    class Meta:
        model = ContactoModel
        fields = [
            'nome',
            'email',
            'mensagem'
        ]