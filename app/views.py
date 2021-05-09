from django.shortcuts import render
from .models import Post

def index(request):
    context = {
        "posts": Post.objects.all()
    }
    if request.method == "POST":

        title = request.POST.get("title")
        description = request.POST.get("description")
        data = Post(title=title,description=description)
        data.save()
    return render(request, "test.html",context)
