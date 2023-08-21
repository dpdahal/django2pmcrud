from django.shortcuts import render,redirect
from .models import Students
from django.http import HttpResponse
from django.contrib import messages
import os

# Create your views here.
def index(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        language_list = request.POST.getlist('language')
        language = ','.join(language_list)
        country = request.POST.get('country')
        image = request.FILES.get('image')
        Students.objects.create(name=name,email=email,gender=gender,language=language,country=country,image=image)
        back = request.META.get('HTTP_REFERER')
        messages.success(request,'Student added successfully')
        return redirect(back)
        
    else:
        data={
            'studentsData':Students.objects.all()
        }
        return render(request, 'index.html',data)


def delete_file(id):
    findData = Students.objects.get(id=id)
    imageName = findData.image
    filePath='uploads/'+str(imageName)
    if os.path.exists(filePath) and os.path.isfile(filePath):
        os.remove(filePath)
        return True
    return True

def delete(request,id):
    sobject =Students.objects.get(id=id)
    delete_file(id)
    sobject.delete()
    messages.success(request,'Student deleted successfully')
    return redirect('index')

def edit(request,id):
    if request.method=="POST":
        sobject =Students.objects.get(id=id)
        sobject.name = request.POST.get('name')
        sobject.gender = request.POST.get('gender')
        language_list = request.POST.getlist('language')
        sobject.language = ','.join(language_list)
        sobject.country = request.POST.get('country')
        if request.FILES.get('image'):
            delete_file(id)
            sobject.image = request.FILES.get('image')
        
        sobject.save()
        messages.success(request,'Student updated successfully')
        return redirect('index')
        
    else:
        data={
            'studentData':Students.objects.get(id=id)
        }
        return render(request, 'edit.html',data)
   