from django.shortcuts import render, redirect
from .models import Todo

def home(request):
    if request.method == "POST":
        if "add" in request.POST:
            title = request.POST.get("title")
            if title:
                Todo.objects.create(title=title)

        elif "delete" in request.POST:
            todo_id = request.POST.get("todo_id")
            Todo.objects.filter(id=todo_id).delete()

        elif "toggle" in request.POST:
            todo_id = request.POST.get("todo_id")
            todo = Todo.objects.get(id=todo_id)
            todo.done = not todo.done
            todo.save()

        return redirect("home")

    todos = Todo.objects.all()
    return render(request, "home.html", {"todos": todos})
