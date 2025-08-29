from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Task, Category, Subtask, UserProfile, Comment
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email"]

class TaskForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority', 'status', 'category', 'attachment']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['category'].queryset = Category.objects.filter(user=user) or Category.objects.none()

class SubtaskForm(forms.ModelForm):
    class Meta:
        model = Subtask
        fields = ['title', 'complete']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a comment...'})
        }
