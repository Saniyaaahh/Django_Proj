from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from day3_models.forms import StudentForm

from day3_models.models import Student

def index(req):
  t1 = loader.get_template("index.htm")
  return HttpResponse(t1.render())

def list(req):
  students = Student.objects.all()
  return render(req, "list.htm", {'students': students})

def details(req, id):
  student = Student.objects.get(id=id)
  return render(req, "details.htm", {'stu': student})  

def add(req):
  msg = None
  stu_form = StudentForm()
  
  if req.method == 'POST':
    form = StudentForm(req.POST)
    if form.is_valid():
      try:
        s = Student(
          fname=form.cleaned_data['fname'],
          lname= form.cleaned_data['lname'],
          branch= form.cleaned_data['branch'],
          year= form.cleaned_data['year']
        )
        s.save()   
        msg = 'Added successfully, Alhamdulillaah'
        return redirect('/list')
      except:
        msg = 'Ah .. some error!'
        pass
      
  return render(req, "add.htm", {'form': stu_form, 'msg': msg})


def delete(req, id):
  msg = None
  try:
    student = Student.objects.get(id=id)
    student.delete()
    msg = 'Successfully deleted!'
  except:
    msg = 'Unable to delete'

  students = Student.objects.all()  
  return render(req, "list.htm", {'students': students, 'msg': msg})

