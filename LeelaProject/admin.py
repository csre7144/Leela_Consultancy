from django.contrib import admin
from LeelaProject.models import contactform
# Register your models here.

class contactformuser(admin.ModelAdmin):
      list_display = ('name', 'email')

# class intern_diapplyuser(admin.ModelAdmin):
#       list_display = ('name2', 'email2')



admin.site.register(contactform, contactformuser)
# admin.site.register(Data_Integration_Engineer_Apply)
# admin.site.register(Intern_Etl_Developer_Apply,intern_diapplyuser)
# admin.site.register(Informatica_Programmer_Analyst_Apply)
# admin.site.register(Data_Engineer_apply)
# admin.site.register(Sr_Data_Architect_Apply)
# admin.site.register(IT_Internship_Apply)
