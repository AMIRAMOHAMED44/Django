from django.shortcuts import render, redirect
from .models import Trainee
from course.models import Course
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def trainee_list(request):
    trainees = Trainee.objects.filter(isactive=True)
    return render(request, 'trainee/trainee_list.html', {'trainees': trainees})

@login_required
def add_trainee(request):
    context={'courses':Course.getallcourses()}
    if request.method == 'POST':
        trname = request.POST['trname']
        tremail=request.POST['tremail']
        trage=request.POST['trage']
        trimg=request.FILES['trimg']
        trcourse=Course.getcoursebyid(id=request.POST['trcourse'])
        trdate=request.POST['trdate']
        obj=Trainee(name=trname,email=tremail,age=trage,image=trimg,course=trcourse,joined_date=trdate)
        obj.save()

        return redirect('trainee_list')
    return render(request, 'trainee/trainee_add.html',context)



@login_required
def update_trainee(request,id):
    context = {'oldobj':Trainee.objects.get(id=id),
               'courses':Course.getallcourses()}
    if (request.method == 'POST'):
        Trainee.objects.filter(id=id).update(
            name=request.POST['trname'],
            email=request.POST['tremail'],
            age=request.POST['trage'],
            image=request.FILES['trimg'],
            course=request.POST['trcourse'],
            joined_date=request.POST['trdate']
        )
        return  redirect('trainee_list')

    return render(request, 'trainee/update.html',context)

@login_required
def delete_trainee(request, id):
    Trainee.objects.filter(id=id).update(isactive=False)
    return redirect('trainee_list')
