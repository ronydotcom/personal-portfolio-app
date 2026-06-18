from django import forms
from django.contrib.auth.forms import UserCreationForm
from portfolio.models import *

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['user']

class SkillForm(forms.ModelForm):
    class Meta:
        model=Skill
        exclude=['user']

class EducationForm(forms.ModelForm):
    class Meta:
        model=Education
        exclude=['user']

class ExperienceForm(forms.ModelForm):
    class Meta:
        model=Experience
        exclude=['user']

class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        exclude=['user']

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'