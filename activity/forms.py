from django import forms
from .models import Activity, Review 


class ActivityForm(forms.ModelForm): #cada formulario es una clase
	class Meta:
		model = Activity 
		fields = '__all__'

class ReviewForm(forms.ModelForm):
	class Meta:
		model = Review
		fields = ['title', 'summary', 'body', 'duration', 'rating']