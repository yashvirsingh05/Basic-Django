from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse('''<h1>welcome thakur</h1> <a href="https://www.youtube.com/watch?v=QhKPi4gDrOk&list=RDQhKPi4gDrOk&start_radio=1&ab_channel=REDZONEISHERE" </a>code with yash''')

def index(request):
    params={'name':"yash",'place':"Aligarh"}
    return render(request,'index.html',params)

def about(request):
    return HttpResponse("about my name thakur")

def removepuch(request):
    print(request.GET.get('text','default'))
    return HttpResponse("remove puch")
def cappunch(request):
    return HttpResponse("add cappunch")

def newlineremove(request):
    return HttpResponse("new line remove  <a href='/'> back</a>")

def spaceremover(request):
    return HttpResponse("space remover ")