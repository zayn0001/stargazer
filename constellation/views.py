from django.shortcuts import render
import constellation
from constellation.prediction import *
from django import forms
from django.core.files.storage import FileSystemStorage

# Create your views here.



def index(request):
    return render(request, "constellation/index.html")

def possibilities(request):
    if request.method == "POST":
        #print("hererer")
        form = dict(request.POST)
        print(form)
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        #print("SDfsdfs")
        print(file_url)
        hemisphere = form["hemisphere"][0]
        predictions = runthis(file_url, hemisphere)
        sources = [f"constellation/images/{prediction}.png" for prediction in predictions]
        print(sources)
        
        return render(request, "constellation/possibilities.html", {
            "predimg1":sources[0],
            "name1":predictions[0],
            "predimg2":sources[1],
            "name2":predictions[1],
            "predimg3":sources[2],
            "name3":predictions[2],
            "predimg4":sources[3],
            "name4":predictions[3]
        })
    return render(request, "constellation/index.html")

def solution(request):
    if request.method == "POST":
        form = dict(request.POST)
        solutioncons = form['solution'][0]
        solutionconsimg = f"constellation/images/{solutioncons}.png"
        return render(request, "constellation/solution.html", {
            "solutionimg":solutionconsimg,
            "solname":solutioncons 
        })



