from django.shortcuts import render
import constellation
from constellation.prediction import *
from django import forms

# Create your views here.



def index(request):
    return render(request, "constellation/index.html")

def possibilities(request):
    if request.method == "POST":
        print("hererer")
        form = dict(request.POST)
        print(form)
        print("SDfsdfs")
        url = form["url"][0]
        hemisphere = form["hemisphere"][0]
        predictions = runthis(url, hemisphere)
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



