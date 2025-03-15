from django.shortcuts import render, redirect
from .models import Course
from .forms import CourseForm
from django.views import View
from django.views.generic import *
from django.urls import reverse_lazy

# Create your views here.
class DeleteCourse(DeleteView):
    model = Course
    success_url = reverse_lazy('course_list')


class UpdateCourse(UpdateView):
        model = Course
        fields = ['name', 'description', 'start_date', 'end_date']
        template_name = 'course/update.html'
        success_url = reverse_lazy('course_list')

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['oldobj'] = self.object
            return context


class ListCourse(View):
    def get(self,req):
        courses = Course.objects.all()
        return render(req, 'course/course_list.html', {'courses': courses})



class AddCourse(View):
    def get(self,req):
        context = {'form': CourseForm()}
        return render(req, 'course/addform.html', context)
    def post(self,req):
        form=CourseForm(data=req.POST,files=req.FILES)
        if(form.is_bound and form.is_valid()):
            form.save()
            return redirect('course_list')
        else:
            context={'form':form,'error':form.errors}
            return render(req, 'course/course_add.html', context)


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course/course_list.html', {'courses': courses})

# def add_course(request):
#     context={'form':CourseForm()}
#     if request.method == 'POST':
#         trname = request.POST['trname']
#         trdescription = request.POST['trdescription']
#         trstart = request.POST['trstart']
#         trend = request.POST['trend']
#         obj = Course(name=trname, description=trdescription, start_date=trstart, end_date=trend)
#         obj.save()
#
#         return redirect('course_list')
#     return render(request, 'course/course_add.html',context)

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
