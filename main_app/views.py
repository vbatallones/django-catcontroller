from django.shortcuts import render
from .models import TheseCats
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
# Create your views here.(like controller actions)
# create view
class TheseCatsCreate(CreateView):
    model = TheseCats
    fields = '__all__'
    success_url = '/cats'

# create a update view
class TheseCatsUpdate(UpdateView):
    model = TheseCats
    fields = ['name', 'breed', 'description', 'age']
    # form is like a req.body
    # instead of using success_url we are going to use the function below
    # to redirect us
    #  form valid is a hook built in django
    def form_valid(self, form): # this will allow us to catch the pk to redirect to the show page
        self.object = form.save(commit=False) # dont post int he db until we say so
        self.object.save()
        return HttpResponseRedirect('/cats/'+str(self.object.pk))

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def cats_index(request):
    # get all cats from the db
    cats = TheseCats.objects.all()
    return render(request, 'cats/index.html', {'cats':cats})
    
def cats_show(request, TheseCats_id):
    cat = TheseCats.objects.get(id=TheseCats_id)
    return render(request, 'cats/show.html', {'cat': cat})
# class Cat: 
#     def __init__(self, name, breed, description, age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.age = age

# cats = [
#     Cat('Lolo', 'tabby', 'foul little demon', 3),
#     Cat('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
#     Cat('Raven', 'black tripod', '3 legged cat', 4)
# ]

