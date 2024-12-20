from django import forms
from .models import CrimeReport

class CrimeReportForm(forms.ModelForm):
    class Meta:
        model = CrimeReport
        fields = ['name', 'email', 'location', 'victims', 'crime_type', 'description', 'image', 'status']  # Added 'status' here

    # Optional: You can customize the form fields further if needed
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].widget.attrs.update({'class': 'form-control'})

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['officer_email', 'comment_text', 'attachments']  # Include other fields if required

    def clean_officer_email(self):
        email = self.cleaned_data.get('officer_email')
        # Add any custom validation for email if necessary
        return email
       

