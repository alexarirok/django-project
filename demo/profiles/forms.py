from django import forms 
from profiles.models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'location', 'description'] 

class ContactForm(forms.Form):
    name = forms.CharField(max_length=30, required=False, help_text='optional')
    email = forms.EmailField(max_length=100, required=False, help_text='required')
    subject = forms.CharField(max_length=50, help_text='optional')
    message = forms.CharField(widget=forms.Textarea, required=True)