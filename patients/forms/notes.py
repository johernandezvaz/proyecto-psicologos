from django import forms
from patients.models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-input',
                'rows': 10,
                'placeholder': 'Dicta o escribe tus notas aquí...'
            })
        }