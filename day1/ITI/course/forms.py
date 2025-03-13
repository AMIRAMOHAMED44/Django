from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    # name=forms.CharField(required=True,min_length=2,max_length=10)
    class Meta:
        model = Course
        fields = ['name','start_date', 'end_date', 'description']
        # fields = '__all__'
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'cols': 45, 'rows': 10}),
        }

