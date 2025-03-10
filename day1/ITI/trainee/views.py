from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Trainee
from .forms import TraineeForm

def trainee_list(request):
    trainees = Trainee.objects.all()
    return render(request, 'trainee/trainee_list.html', {'trainees': trainees})

def add_trainee(request):
    if request.method == 'POST':
        trname = request.POST['trname']
        tremail=request.POST['tremail']
        trage=request.POST['trage']
        trimg=request.FILES['trimg']
        trcourse=request.POST['trcourse']
        trdate=request.POST['trdate']
        obj=Trainee(name=trname,email=tremail,age=trage,image=trimg,course=trcourse,joined_date=trdate)
        obj.save()

    return render(request, 'trainee/trainee_add.html')




def update_trainee(request,id):
    context = {'oldobj':
                   Trainee.objects.get(id=id)}
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

def delete_trainee(request, trainee_id):
    trainee = get_object_or_404(Trainee, id=trainee_id)
    if request.method == 'POST':
        trainee.delete()
        return redirect('trainee_list')
    return render(request, 'trainee/trainee_delete.html', {'trainee': trainee})
