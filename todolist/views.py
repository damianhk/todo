from django.shortcuts import render, redirect
from .models import TodoList, Category

def index(request):
    todos = TodoList.objects.all()
    categories = Category.objects.all()
    if request.method == "POST":
        if "taskAdd" in request.POST:
            title = request.POST["description"]
            due_date = str(request.POST["dueDate"])
            category = request.POST["category"]
            Todo = TodoList(title=title, due_date=due_date, category=Category.objects.get(name=category))
            Todo.save()
            return redirect("/")
        if "taskDelete" in request.POST:
            checkedlist = request.POST.getlist("checkedbox")
            print('Checked list ', checkedlist)
            for item in checkedlist:
                task = TodoList.objects.get(id=int(item))
                task.delete()
        if "showCategory" in request.POST:
            print("show")
            category = str(request.POST["showCategory"])
            todos = TodoList.objects.filter(category=Category.objects.get(name=category))


    return render(request, "index.html", {"todos":todos, "categories":categories})