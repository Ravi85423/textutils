from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    #get the text
    djtext = request.POST.get('text','default')

    #Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps','off')
    newline = request.POST.get('newline','off')
    extraspace = request.POST.get('extraspace','off')
    charcnt = request.POST.get('charcnt','off')
    if removepunc=='on':
        punctuations = "!()-[]{}<>./?@#$%^&*_~;,'"
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        param = {'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext = analyzed

    if(fullcaps=='on'):
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        param = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if (extraspace == 'on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed += char
        param = {'purpose': 'Extra space Removed', 'analyzed_text': analyzed}
        djtext = analyzed

    if(newline=='on'):
        analyzed = ""
        for char in djtext:
            if char!='\n' and char!='\r':
                analyzed = analyzed + char
        param = {'purpose': 'New line removed', 'analyzed_text': analyzed}
        djtext = analyzed

    if(removepunc!="on" and fullcaps!="on" and newline!='on' and extraspace!='on' and charcnt!='on'):
        return HttpResponse("Error")
    return render(request,'analyze.html',param)


