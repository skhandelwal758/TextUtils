from django.http import HttpResponse
from django.shortcuts import render

def analyze(request):
    #Get the Text
    djtext=request.POST.get('text','default')

    #Check checkbox values
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount=request.POST.get('charcount','off')

    # Check which checkbox is on
    if(removepunc=="on"):
        analyzed=""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed+=char
        params={
            'purpose':'Removed Punctuations!',
            'analyzed_text':analyzed
        }
        djtext=analyzed

    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'Changed to UpperCase','analyzed_text':analyzed}
        djtext=analyzed

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed Extraspaces', 'analyzed_text': analyzed}
        # Analyze the text
        djtext=analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        djtext=analyzed

    if(charcount=="on"):
        count=0
        for char in djtext:
            count+=1
        analyzed=djtext+"\nNo. of characters in your text:"+str(count)
        params = {'purpose': 'Count Characters', 'analyzed_text': analyzed}

    if(removepunc != "on" and fullcaps != "on" and extraspaceremover != "on" and newlineremover != "on" and charcount!="on"):
        return HttpResponse("Please select any operation and try again")


    return render(request, 'analyze.html', params)


def index(request):
    # params={'name':'harry','place':'USA'}
    return render(request, 'index.html')
    # return HttpResponse('''<a href="https://www.youtube.com/">You Tube</a>''')
