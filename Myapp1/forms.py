from django import forms
from .models import UserProfile,Author,Book,Student,Course,User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
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

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=False,widget=forms.EmailInput(attrs={'class':'form-control'}))
    username = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(required=False,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(required=False,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ['email','username','password1','password2']
        
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'enrollment_date']
        
        # Add Bootstrap classes to form widgets
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter student name'}),
            'enrollment_date': forms.DateInput(attrs={
                'class': 'form-control', 
                'placeholder': 'YYYY-MM-DD', 
                'type': 'date'  # Set the input type to date
            }),
        }
        
        # Optionally, add custom error messages
        error_messages = {
            'name': {
                'required': 'Please enter the student name.',
            },
            'enrollment_date': {
                'required': 'Please select an enrollment date.',
            },
        }

class CourseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields = ['title','students']
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter course name'}),
            'students': forms.CheckboxSelectMultiple,
        }
    