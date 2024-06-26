from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(required = True, widget=forms.TextInput(attrs={'id': 'question', 'placeholder': 'Enter the name', 'class': 'contact-name-input mt-4'}))
    phone = forms.CharField(required = True, widget=forms.TextInput(attrs={'id': 'question', 'placeholder': 'Enter the phone number', 'class': 'contact-name-input mt-3'}))
    email = forms.CharField(required = True, widget=forms.EmailInput(attrs={'id': 'question', 'placeholder': 'Enter the g-mail', 'class': 'contact-name-input mt-3'}))
    message = forms.CharField(required = True, widget=forms.Textarea(attrs={'id': 'question', 'placeholder': 'Enter a message', 'class': 'contact-name-textarea mt-3', 'style': 'padding-top: 15px;'}))
    class Meta:
        model = Contact
        fields = '__all__'

class AzContactForm(forms.ModelForm):
    name = forms.CharField(required = True, widget=forms.TextInput(attrs={'id': 'question', 'placeholder': 'Adı daxil edin', 'class': 'contact-name-input mt-4'}))
    phone = forms.CharField(required = True, widget=forms.TextInput(attrs={'id': 'question', 'placeholder': 'Telefon nömrəsini daxil edin', 'class': 'contact-name-input mt-3'}))
    email = forms.CharField(required = True, widget=forms.EmailInput(attrs={'id': 'question', 'placeholder': 'G-maili daxil edin', 'class': 'contact-name-input mt-3'}))
    message = forms.CharField(required = True, widget=forms.Textarea(attrs={'id': 'question', 'placeholder': 'Mesaj daxil edin', 'class': 'contact-name-textarea mt-3', 'style': 'padding-top: 15px;'}))
    class Meta:
        model = Contact
        fields = '__all__'

class RuContactForm(forms.ModelForm):
    name = forms.CharField(required = True, widget=forms.TextInput(attrs={'id': 'question', 'placeholder': 'Введите имя', 'class': 'contact-name-input mt-4'}))
    phone = forms.CharField(required = True, widget=forms.TextInput(attrs={'“‘lkid': 'question', 'placeholder': 'Введите номер телефона', 'class': 'contact-name-input mt-3'}))
    email = forms.CharField(required = True, widget=forms.EmailInput(attrs={'id': 'question', 'placeholder': 'Введите адрес электронной почты', 'class': 'contact-name-input mt-3'}))
    message = forms.CharField(required = True, widget=forms.Textarea(attrs={'id': 'question', 'placeholder': 'Введите сообщение', 'class': 'contact-name-textarea mt-3', 'style': 'padding-top: 15px;'}))
    class Meta:
        model = Contact
        fields = '__all__'