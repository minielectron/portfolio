from django.shortcuts import render


app_name="website"

def home(request):
    return render(request,"website/home.html")