from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
from .forms import CourseForm

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course/course_list.html', {'courses': courses})

def add_course(request):
    if request.method == 'POST':
        trname = request.POST['trname']
        trdescription = request.POST['trdescription']
        trstart = request.POST['trstart']
        trend = request.POST['trend']
        obj = Course(name=trname, description=trdescription, start_date=trstart, end_date=trend)
        obj.save()

        return redirect('course_list')
    return render(request, 'course/course_add.html')

def update_course(request, id):
    context = {'oldobj':
        Course.objects.get(id=id)}
    if (request.method == 'POST'):
        Course.objects.filter(id=id).update(
            name=request.POST['trname'],
            description=request.POST['trdescription'],
            start_date = request.POST['trstart'],
            end_date = request.POST['trend']
        )
        return  redirect('course_list')

    return render(request, 'course/update.html',context)

def delete_course(request, id):
    Course.objects.filter(id=id).delete()
    return redirect('course_list')
