from django import forms
from .models import Comments, Project


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'comment',)

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    "placeholder": 'Enter Your Name',
                    'rows': 20,
                    'cols': 70,
                }
            ),
            'comment': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    "placeholder": 'Enter your comment here',
                    'rows': 10,
                    'cols': 80,
                }
            )

        }


class ProjectForm(forms.ModelForm):
    class Meta:
        models = Project
        fields = '__all__'

