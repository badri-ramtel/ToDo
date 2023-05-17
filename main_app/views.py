from django.shortcuts import render, redirect
from main_app.models import ToDo
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from main_app.forms import ToDoForm
from django.core.paginator import Paginator

# Create your views here.
@login_required
def home(request):
    query = request.GET.get('query')
    if query is None:
        if request.user.is_superuser:
            todos = ToDo.objects.all()
        else:
            todos = ToDo.objects.filter(user_id=request.user.id)
    else:
        if request.user.is_superuser:
            todos = ToDo.objects.filter(title__icontains=query)
        else:
            todos = ToDo.objects.filter(user_id=request.user.id, title__icontains=query)
        request.session['query'] = query

    todo_list = ToDo.objects.all()
    paginator = Paginator(todo_list,3)  # Show 3 todo list per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print('********************')
    print(page_obj)
    return render(request, 'main_app/home.html', {'todos': todos, 'page_obj' : page_obj})
        
    # return render(request, 'main_app/home.html', )

# def listing(request):
#     todo_list = ToDo.objects.all()
#     paginator = Paginator(todo_list,3)  # Show 3 todo list per page.

#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     print('********************')
#     print(page_obj)
#     return render(request, 'main_app/home.html', {'page_obj' : page_obj})

@login_required
def add(request):
    # ---1st form---
    if request.method == 'GET':
        return render(request, 'main_app/add.html')
    else:
        # print('*************')
        # print(request.POST)
        title = request.POST['title']
        desc = request.POST.get('description')

        ToDo.objects.create(title=title, description=desc, is_completed=False, user_id=request.user.id)

        messages.success(request, 'added successfully.')

        return redirect('main-home')

    # if request.method == 'GET':
    #     form = forms.ToDoForm()
    #     return render(request, 'main_app/add.html', {'form':form})

@login_required
def edit(request, id):
    # todo = ToDo.objects.get(id=id)
    try:
        todo = ToDo.objects.get(id=id)
    except ToDo.DoesNotExist:
        return redirect('404notfound')

    if request.method == 'GET':
        return render(request, 'main_app/edit.html', {'todo' : todo})
    
    else:
        todo.title = request.POST['title']
        todo.description = request.POST['description']

        todo.save()

        return redirect('main-home')

@login_required()
def delete(request, id):
    try:
        todo = ToDo.objects.get(id=id)
    except ToDo.DoesNotExist:
        return redirect('404notfound')
    todo.delete()
    return redirect('main-home')

def not_found(request):
    return render(request, 'core/404.html')

def complete(request, id):
    try:
        todo = ToDo.objects.get(id=id)
    except ToDo.DoesNotExist:
        return redirect('404notfound')

    # if todo.is_completed:
    #     todo.is_completed = False
    # else: 
    #     todo.is_completed = True

    # todo.is_completed = True if todo.is_completed else False

    todo.is_completed = not todo.is_completed

    todo.save()
    return redirect('main-home')