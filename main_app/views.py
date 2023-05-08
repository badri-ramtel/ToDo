from django.shortcuts import render, redirect
from main_app.models import ToDo

# Create your views here.
def home(request):
    todos = ToDo.objects.all()
    return render(request, 'main_app/home.html', {'todos' : todos })

def edit(request, id):
    todo = ToDo.objects.get(id=id)
    

def delete(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect('main-home')

def add(request):
    if request.method == 'GET':
        return render(request, 'main_app/add.html')
    else:
        print('*************')
        print(request.POST)
        title = request.POST['title']
        desc = request.POST.get('description')
        is_completed = True if request.POST.get('is_completed') else False

        ToDo.objects.create(title=title, description=desc, is_completed=is_completed, user_id=1)
        return redirect('main-home')


# def login(request):
#     return render(request, 'main_app/login.html')