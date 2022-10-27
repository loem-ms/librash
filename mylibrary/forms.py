from django import forms

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
        
        