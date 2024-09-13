from django import forms
from .models import UserProfile,Author,Book,Student,Course
from django.core.exceptions import ValidationError

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'birthdate','images','videos']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter author name'}),
            'birthdate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'YYYY-MM-DD'}),
            'images': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'videos': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
    
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter author name'}), required=False)
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), required=False)
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}), required=False)
    videos = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}), required=False)
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise ValidationError('Custom Error: Name is required')
        return name
    
    def clean_birthdate(self):
        birthdate = self.cleaned_data.get('birthdate')
        if not birthdate:
            raise ValidationError('Custom Error: Birthdate is required')
        return birthdate
    
    def clean_images(self):
        images = self.cleaned_data.get('images')
        if not images:
            raise ValidationError('Custom Error: Images is required')
        return images
    
    def clean_videos(self):
        videos = self.cleaned_data.get('videos')
        if not videos:
            raise ValidationError('Custom Error: Video is required')
        return videos