from django.shortcuts import render, redirect
from .models import Todo

def index(request):
    if request.method == 'POST':
        new_todo = Todo(text=request.POST['text'])
        new_todo.save()
        return redirect('index')
    else:
        todos = Todo.objects.all()
        return render(request, 'index.html', {'todos': todos})

def delete(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.delete()
    return redirect('index')

def delete_multiple(request):
    if request.method == 'POST':
        todos_ids = request.POST.getlist('todos')
        Todo.objects.filter(pk__in=todos_ids).delete()
        return redirect('index')
    else:
        return redirect('index')