from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Votre nom', max_length=42, error_messages={'required': 'Entrer votre Nom.'})
    subject = forms.CharField(label='Sujet', max_length=100)
    email_address = forms.EmailField(label='Votre adresse e-mail', error_messages={'required': 'Entrer votre adresse mail.', 'invalid':'Entrer une adresse mail valide.'})
    message = forms.CharField(widget=forms.Textarea)
