from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('career/', views.career, name='career'),
    path('contact/', views.contact, name='contact'),
    path('Data_Architect/', views.DA, name='DA'),
    path('Programmer_Analyst_Data_Engineer/', views.DE, name='DE'),
    path('Di_Apply/', views.Di_Apply, name='Di_Apply'),
    path('Data_Integration_Engineer/', views.Data_Integration_Engineer, name='Data_Integration_Engineer'),
    path('Intern_ETL_Developer/', views.Intern_ETL_Developer, name='Intern_ETL_Developer'),
    path('Informatica_Programmer_Analyst/', views.IPA, name='IPA'),
    path('IT_Internship/', views.IT_Intern, name='IT_Intern'),
    path('Solutions_Architect/', views.SA, name='SA'),
    path('Thank_you/', views.ty, name='ty'),
    path('Intern_ETL_Developer_apply/', views.intern_di_apply, name='intern_di_apply'),
    path('Informatica_Programmer_Analyst_apply/', views.ipa_apply, name='ipa_apply'),
    path('Programmer_Analyst_Data_Engineer_apply/', views.DE_apply, name='DE_apply'),
    path('Data_Architect_apply', views.DA_apply, name='DA_apply'),
    path('Solutions_Architect_apply/', views.SA_apply, name='SA_apply'),
    path('IT_Internship_apply/', views.ITintern_apply, name='ITintern_apply'),
]
