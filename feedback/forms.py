from django import forms
from .models import Feedback
from myems.models import Employee


class FeedbackAddForm(forms.ModelForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'size':20}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 6, 'cols': 50, 'style': 'resize:none;'}))

    def clean_emp_no(self):
        emp_no = self.cleaned_data.get('emp_no')
        if emp_no and not Employee.objects.filter(pk=emp_no).exists():
            raise forms.ValidationError(message="Invalid employee number")
        else:
            return emp_no


    class Meta:
        model = Feedback
        fields = ('emp_no', 'name', 'subject', 'category', 'email', 'is_read')


class FeedbackForm(forms.ModelForm):

    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':6, 'cols':50, 'style':'resize:none;'}))
    created_on = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly', 'size':'38'}))
    class Meta:
        model = Feedback
        fields = '__all__'

