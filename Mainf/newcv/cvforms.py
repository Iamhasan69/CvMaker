from django import forms
from .models import CVINFO

class CVFORM(forms.ModelForm):
    class Meta:
        model = CVINFO
        fields = ('full_name','job_role','contc_info','email_info','location','profile_summary','education','skills','projects','other_info')
        