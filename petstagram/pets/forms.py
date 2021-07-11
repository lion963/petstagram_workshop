from django import forms

from pets.models import Pet


class PetCreateForm(forms.ModelForm):
    class Meta:
        model = Pet
        exclude = ['user']

        widgets = {
            'type': forms.Select(attrs= {'class': 'form-control'}),
            'name': forms.TextInput(attrs= {'class': 'form-control'}),
            'age': forms.NumberInput(attrs= {'class': 'form-control'}),
            'description': forms.Textarea(attrs= {'class': 'form-control'}),
            'image_url': forms.FileInput(attrs= {'class': 'form-control'})
        }
