from django import forms
from .models import Data_Integration_Engineer_Apply,Intern_Etl_Developer_Apply,Informatica_Programmer_Analyst_Apply,Data_Engineer_apply,Sr_Data_Architect_Apply,Solutions_Architect_Apply,IT_Internship_Apply



class interndiapplyform(forms.ModelForm):
      class Meta:
            models = Intern_Etl_Developer_Apply()
            fields = '__all__'


class ipaapplyform(forms.ModelForm):
      class Meta:
            models = Informatica_Programmer_Analyst_Apply()
            fields = '__all__'

class Data_Engineerform(forms.ModelForm):
      class Meta:
            models = Data_Engineer_apply()
            fields = '__all__'

class Data_Architectform(forms.ModelForm):
      class Meta:
            models = Sr_Data_Architect_Apply()
            fields = '__all__'

class IT_Internshipform(forms.ModelForm):
      class Meta:
            models = IT_Internship_Apply()
            fields = '__all__'
