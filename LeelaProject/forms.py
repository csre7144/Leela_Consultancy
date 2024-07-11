from django import forms
from .models import contactform
class contactuser(forms.ModelForm):
      class Meta:
            model = contactform()
            fields = '__all__'


# class diapplyform(forms.ModelForm):
#       class Meta:
#             model = Data_Integration_Engineer_Apply()
#             fields = '__all__'

# class interndiapplyform(forms.ModelForm):
#       class Meta:
#             models = Intern_Etl_Developer_Apply()
#             fields = '__all__'


# class ipaapplyform(forms.ModelForm):
#       class Meta:
#             models = Informatica_Programmer_Analyst_Apply()
#             fields = '__all__'

# class Data_Engineerform(forms.ModelForm):
#       class Meta:
#             models = Data_Engineer_apply()
#             fields = '__all__'

# class Data_Architectform(forms.ModelForm):
#       class Meta:
#             models = Sr_Data_Architect_Apply()
#             fields = '__all__'

# class IT_Internshipform(forms.ModelForm):
#       class Meta:
#             models = IT_Internship_Apply()
#             fields = '__all__'
