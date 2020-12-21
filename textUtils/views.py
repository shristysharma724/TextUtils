#this file is made by me- shristy

from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')
#def index(request):
    #return HttpResponse('''<h1>hello everyone</h1> <a href="https://www.youtube.com/watch?v=zs2Ux1jfDD0&t=161s">Django Course</a>''')
def about(request):
    return HttpResponse("about us")
def analyze(request):
    removepunc = request.POST.get('removepunc','off')
    print(removepunc)
    djtext=request.POST.get('text','default') #get the text
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover= request.POST.get('extraspaceremover', 'off')
    print(djtext)
    analyzed =""
    if removepunc == "on":
      punctuations = '''!$^*~&$#@<>:;"()?'()./,'''
      for charc in djtext:
         if charc not in punctuations:
           analyzed = analyzed + charc
           params = {'purpose':'Removed Punctuations','analyzed_text':analyzed}
           djtext =analyzed
      #return render(request,'analyze.html',params)
    if(fullcaps=="on"):
           analyzed = ""
           for char in djtext:
             analyzed =analyzed + char.upper()
           params = {'purpose' : 'Changed  to Uppercase' , 'analyzed_text':analyzed}
           djtext = analyzed
           #return render(request , 'analyze.html',params)
    if (extraspaceremover == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]== " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'removed extraspace', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if(newlineremover =="on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
              analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if(removepunc != "on" and fullcaps!="on" and extraspaceremover != "on" and newlineremover !="on"):
           return HttpRespone("Error")

    return render(request, 'analyze.html', params)
