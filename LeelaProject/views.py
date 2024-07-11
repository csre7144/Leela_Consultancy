from django.shortcuts import render,redirect
from .forms import contactform
from Customer_Apply.models import Data_Integration_Engineer_Apply, Informatica_Programmer_Analyst_Apply,Intern_Etl_Developer_Apply,Data_Engineer_apply,Sr_Data_Architect_Apply,Solutions_Architect_Apply,IT_Internship_Apply

# Create your views here.
def home(request):
      return render(request, 'index.html')

def about(request):
      return render(request, 'about.html')

def career(request):
      return render(request, 'career.html')

def contact(request):
      if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            subject = request.POST['subject']
            message = request.POST['message']
            data = contactform(name=name, email=email, phone=phone, subject=subject, message=message)
            data.save()
      return render(request, 'contact.html')

def DA(request):
      return render(request, 'DA.html')

def DE(request):
      return render(request, 'DE.html')

def Di_Apply(request):
      if request.method == 'POST':
            name1 = request.POST['name1']
            email1 = request.POST['email1']
            phone1 = request.POST['phone1']
            city = request.POST['city']
            document = request.FILES['fileUpload']
            data = Data_Integration_Engineer_Apply(name1=name1, email1=email1, phone1=phone1, city=city, document=document)
            if data:
                  data.save()
                  return redirect('ty')
      return render(request, 'Di_apply.html')

def Data_Integration_Engineer(request):
      return render(request, 'DI.html')

def Intern_ETL_Developer(request):
      return render(request, 'intern_di.html')

def IPA(request):
      return render(request, 'IPA.html')

def IT_Intern(request):
      return render(request, 'ITintern.html')

def SA(request):
      return render(request, 'SA.html')

def ty(request):
      return render(request, 'success.html')

def intern_di_apply(request):
      if request.method == 'POST':
            name2 = request.POST['name2']
            email2 = request.POST['email2']
            phone2 = request.POST['phone2']
            city2 = request.POST['city2']
            document2 = request.FILES['fileUpload']
            data = Intern_Etl_Developer_Apply(name2=name2, email2=email2, phone2=phone2,city2=city2,document2=document2)
            if data:
                  data.save()
                  return redirect('ty')
      return render(request, 'intern_di_apply.html')

def ipa_apply(request):
      if request.method == 'POST':
            name2 = request.POST['name3']
            email2 = request.POST['email3']
            phone2 = request.POST['phone3']
            city2 = request.POST['city3']
            document2 = request.FILES['fileUpload']
            data = Informatica_Programmer_Analyst_Apply(name2=name2, email2=email2, phone2=phone2,city2=city2,document2=document2)
            if data:
                  data.save()
                  return redirect('ty')
      return render(request, 'IPA_apply.html')

def DE_apply(request):
      if request.method == 'POST':
            name2 = request.POST['name3']
            email2 = request.POST['email3']
            phone2 = request.POST['phone3']
            city2 = request.POST['city3']
            document2 = request.FILES['fileUpload']
            data = Data_Engineer_apply(name2=name2, email2=email2, phone2=phone2,city2=city2,document2=document2)
            if data:
                  data.save()
                  return redirect('ty')
      return render(request, 'DE_apply.html')

def DA_apply(request):
      if request.method == 'POST':
            name2 = request.POST['name3']
            email2 = request.POST['email3']
            phone2 = request.POST['phone3']
            city2 = request.POST['city3']
            document2 = request.FILES['fileUpload']
            data = Sr_Data_Architect_Apply(name2=name2, email2=email2, phone2=phone2,city2=city2,document2=document2)
            if data:
                  data.save()
                  return redirect('ty')
      return render(request, 'DA_apply.html')

def SA_apply(request):
      if request.method == 'POST':
            name2 = request.POST['name3']
            email2 = request.POST['email3']
            phone2 = request.POST['phone3']
            city2 = request.POST['city3']
            document2 = request.FILES['fileUpload']
            data = Solutions_Architect_Apply(name2=name2, email2=email2, phone2=phone2,city2=city2,document2=document2)
            if data:
                  data.save()
                  return redirect('ty')
      return render(request, 'SA_apply.html')

def ITintern_apply(request):
      if request.method == 'POST':
            name2 = request.POST['name3']
            email2 = request.POST['email3']
            phone2 = request.POST['phone3']
            city2 = request.POST['city3']
            document2 = request.FILES['fileUpload']
            data = IT_Internship_Apply(name2=name2, email2=email2, phone2=phone2,city2=city2,document2=document2)
            if data:
                  data.save()
                  return redirect('ty')
      return render(request, 'ITintern_apply.html')