from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    def clean_class(self):
        input_class= self.cleaned_data['s_class']
        if input_class < 8:
            raise forms.ValidationError('The student must be AT-LEAST in 8th grade')
        else:
            return input_class


    class Meta:
        model = Student
        fields = '__all__'
