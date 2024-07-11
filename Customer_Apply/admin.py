from django.contrib import admin
from Customer_Apply.models import Data_Integration_Engineer_Apply, Intern_Etl_Developer_Apply,Informatica_Programmer_Analyst_Apply,Data_Engineer_apply,Sr_Data_Architect_Apply,Solutions_Architect_Apply,IT_Internship_Apply
# Register your models here.

class contactformuser(admin.ModelAdmin):
      list_display = ('name', 'email')

class intern_diapplyuser(admin.ModelAdmin):
      list_display = ('name2', 'email2')

admin.site.register(Data_Integration_Engineer_Apply)
admin.site.register(Intern_Etl_Developer_Apply,intern_diapplyuser)
admin.site.register(Informatica_Programmer_Analyst_Apply)
admin.site.register(Data_Engineer_apply)
admin.site.register(Sr_Data_Architect_Apply)
admin.site.register(IT_Internship_Apply)
admin.site.register(Solutions_Architect_Apply)


admin.site.site_header="Leela Consultancy Admin"
admin.site.index_title="Leela Consultancy Report"
admin.site.site_title="Site Leela Consultancy"