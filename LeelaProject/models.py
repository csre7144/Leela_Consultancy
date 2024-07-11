from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class contactform(models.Model):
      name = models.CharField(max_length=30)
      email = models.EmailField(max_length=50)
      phone = PhoneNumberField(max_length= 20)
      subject = models.CharField(max_length=50)
      message = models.TextField(max_length=5000)

      def __str__(self) -> str:
            return self.name + ' ' + self.email
      


# class Data_Integration_Engineer_Apply(models.Model):
#       name1 = models.CharField(max_length=30)
#       email1 = models.EmailField(max_length=50)
#       phone1 = PhoneNumberField(max_length=20)
#       city = models.CharField(max_length=30)
#       document = models.FileField(upload_to="Resume/")

#       def __str__(self):
#             return self.name1
      

# class Intern_Etl_Developer_Apply(models.Model):
#       name2 = models.CharField(max_length=30)
#       email2 = models.EmailField(max_length=50)
#       phone2 = PhoneNumberField(max_length=20)
#       city2 = models.CharField(max_length=30)
#       document2 = models.FileField(upload_to="Resume/")

#       def __str__(self):
#             return self.name2 
      

# class Informatica_Programmer_Analyst_Apply(models.Model):
#       name2 = models.CharField(max_length=30)
#       email2 = models.EmailField(max_length=50)
#       phone2 = PhoneNumberField(max_length=20)
#       city2 = models.CharField(max_length=30)
#       document2 = models.FileField(upload_to="Resume/")

#       def __str__(self):
#             return self.name2 

# class Data_Engineer_apply(models.Model):
#       name2 = models.CharField(max_length=30)
#       email2 = models.EmailField(max_length=50)
#       phone2 = PhoneNumberField(max_length=20)
#       city2 = models.CharField(max_length=30)
#       document2 = models.FileField(upload_to="Resume/")

#       def __str__(self):
#             return self.name2 
      
# class Sr_Data_Architect_Apply(models.Model):
#       name2 = models.CharField(max_length=30)
#       email2 = models.EmailField(max_length=50)
#       phone2 = PhoneNumberField(max_length=20)
#       city2 = models.CharField(max_length=30)
#       document2 = models.FileField(upload_to="Resume/")

#       def __str__(self):
#             return self.name2 
      
# class Solutions_Architect_Apply(models.Model):
#       name2 = models.CharField(max_length=30)
#       email2 = models.EmailField(max_length=50)
#       phone2 = PhoneNumberField(max_length=20)
#       city2 = models.CharField(max_length=30)
#       document2 = models.FileField(upload_to="Resume/")

#       def __str__(self):
#             return self.name2 
      

# class IT_Internship_Apply(models.Model):
#       name2 = models.CharField(max_length=30)
#       email2 = models.EmailField(max_length=50)
#       phone2 = PhoneNumberField(max_length=20)
#       city2 = models.CharField(max_length=30)
#       document2 = models.FileField(upload_to="Resume/")

#       def __str__(self):
#             return self.name2 