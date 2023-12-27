from django import forms 
from .models import CommentModel
from .models import CarModel

class CarForm(forms.ModelForm):
    class Meta:
        model = CarModel
        exclude = ['brand']
        # fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['name','email','body']

