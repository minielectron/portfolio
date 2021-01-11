from django.shortcuts import render

app_name="blog"

def blogs(request):
    return render(request,"blog/blog.html")