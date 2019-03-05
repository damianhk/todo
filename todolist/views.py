from django.shortcuts import render, redirect
from .models import TodoList, Category


def index(request, todos=None, categoryFlag=None):
    categories = Category.objects.all()
    if categoryFlag:
        pass
    else:
        todos=TodoList.objects.all()
        
    if request.method == "POST":
        if "taskAdd" in request.POST:
            title = request.POST["description"]
            due_date = str(request.POST["dueDate"])
            category = request.POST["category"]
            Todo = TodoList(title=title, due_date=due_date, category=Category.objects.get(name=category))
            Todo.save()

        if "taskDelete" in request.POST:
            checkedlist = request.POST.getlist("checkedbox")
            for item in checkedlist:
                task = TodoList.objects.get(id=int(item))
                task.delete()
    return render(request, "index.html", {"todos":todos, "categories":categories})

def category(request, category_id):
    todos = TodoList.objects.filter(category=Category.objects.get(name=category_id))
    return index(request, todos, category_id)
