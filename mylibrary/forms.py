from django import forms
from django.core.mail import EmailMessage

from .models import Document

class InquiryForm(forms.Form):
    name = forms.CharField(label='Name', max_length=30)
    email = forms.EmailField(label='Email')
    title = forms.CharField(label='Title', max_length=30)
    message = forms.CharField(label='Message', widget=forms.Textarea)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['name'].widget.attrs['class'] = 'form-control col-9'
        self.fields['name'].widget.attrs['placeholder'] = 'Input your name here'
        
        self.fields['email'].widget.attrs['class'] = 'form-control col-11'
        self.fields['email'].widget.attrs['placeholder'] = 'Your e-mail address'
        
        self.fields['title'].widget.attrs['class'] = 'form-control col-11'
        self.fields['title'].widget.attrs['placeholder'] = 'Title of inquiry'
        
        self.fields['message'].widget.attrs['class'] = 'form-control col-12'
        self.fields['message'].widget.attrs['placeholder'] = 'Your message'
        
    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        title = self.cleaned_data['title']
        message = self.cleaned_data['message']
        
        subject = f'Inquiry: {title}'
        message = f'Sent from {name}\nEmail:{email}\nMessage:\n{message}'
        sendfrom_email = 'contact@librash.com'
        sendto_email = [
            'services@librash.com',
        ]
        sendcc_email = [
            email
        ]
        
        message = EmailMessage(
            subject=subject,
            body=message,
            from_email=sendfrom_email,
            to=sendto_email,
            cc=sendcc_email
        )
        message.send()

class DocumentCreateForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title', 'summary', 'keyword', 'photo')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'