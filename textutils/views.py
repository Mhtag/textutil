# I have created this file

from django.http import HttpResponse
from django.shortcuts import render

# def ex1(request):
#     return HttpResponse('''<h1>about Mohit</h1> <a href="http://google.com">Goggle</a>''')

# def about(request):
#     return HttpResponse('''<h1>about Mohit</h1>''')

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Home")

def analyze(request):

    # Get the text from the home page
    # djtext = request.GET.get('text', 'default')
    djtext = request.POST.get('text', 'default')

    # For our GET MEthod

    # Checking the checkbox value
    # removepunc = request.GET.get('removepunc', 'off')
    # fullcaps = request.GET.get('fullcaps', 'off')
    # newlineremover = request.GET.get('newlineremover', 'off')
    # extraspaceremover = request.GET.get('extraspaceremover', 'off')
    # charactercounter = request.GET.get('charactercounter', 'off')

    # For our POST mETHOD
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charactercounter = request.POST.get('charactercounter', 'off')
    
    # Checking which checkbox is ON

    if removepunc == 'on':
        punctuations = '''!@#$%^&*()_-+=~`<>,.:;/|\{}[]"'?'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        print(analyzed)        
        params = {'purpose':'Remove Punctuation', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if fullcaps == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Changed to UpperCase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if extraspaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose':'Remove new line', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if newlineremover == 'on':
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != '\r':
                analyzed = analyzed + char
        params = {'purpose':'Extra Space Remover', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if charactercounter == 'on':
        caracters = 0
        for char in djtext:
            if not char == " ":
                caracters += 1
        total_caracters = f"Total Number of Characters in text is {caracters}"
        params = {'purpose':'Counting the characters', 'analyzed_text': total_caracters}
        # return render(request, 'analyze.html', params)

    if(removepunc != 'on'and fullcaps != 'on' and extraspaceremover != 'on' and newlineremover != 'on' and charactercounter != 'on'):
        return HttpResponse('Error')

    return render(request, 'analyze.html', params)






# def removepunc(request):
#     # Get the text from the home page
#     djtext = request.GET.get('text', 'default')
#     print(djtext)
#     # analyze the text
#     return HttpResponse('''remove punc <a href="/">Back</a>''')

# def capfirst(request):
#     return HttpResponse('''capitalize first <a href="/">Back</a>''')

# def spaceremove(request):
#     return HttpResponse('''spaceremove <a href="/">Back</a>''')

# def newlineremove(request):
#     return HttpResponse('''newlineremove <a href="/">Back</a>''')

# def charcount(request):
#     return HttpResponse('''charcount <a href="/">Back</a>''')