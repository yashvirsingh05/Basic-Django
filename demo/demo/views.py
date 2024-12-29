from django.http import HttpResponse
from django.shortcuts import render


# def index(request):
#     return HttpResponse('''<h1>welcome thakur</h1> <a href="https://www.youtube.com/watch?v=QhKPi4gDrOk&list=RDQhKPi4gDrOk&start_radio=1&ab_channel=REDZONEISHERE" </a>code with yash''')

def index(request):
    return render(request,'index.html')


def analyze(request):
    # Get the text
    djtext = request.GET.get('text', 'default')
    removepunc=request.GET.get('removepunc','off')
    fullcap=request.GET.get('fullcaps','off')
    charCount=request.GET.get('charCount','off')
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif(fullcap=='on'):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'changed to uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif(charCount=='on'):
        text_without_spaces = djtext.replace(" ", "")

        character_count = len(text_without_spaces)
        params = {'purpose': 'changed to uppercase', 'analyzed_text': character_count}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse('Error')



def navigation(request):
    s='<h1> Navigation Pages <br></h1> <a a href="https://www.youtube.com/watch?v=QhKPi4gDrOk&list=RDQhKPi4gDrOk&start_radio=1&ab_channel=REDZONEISHERE"</a> youtube<br>'
    return HttpResponse(s)

def NavigationPage(request):
    return render(request,'navigation.html')
