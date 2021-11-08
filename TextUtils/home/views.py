from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')


def analyze(request):
    # get text
    text=request.POST.get('text','default')
    # print(text)
    remove_punc = request.POST.get('removepunc', 'off')
    full_caps = request.POST.get('fullcaps', 'off')
    new_line_remover = request.POST.get('newlineremover', 'off')
    extra_space_remover = request.POST.get('extraspaceremover', 'off')
    params = {'purpose': "", 'analyzed_text':""}
    #Check which checkbox is on
    if remove_punc == "on":
        text=rm_punc(text)
        params['purpose']+='Removed Punctuations \n'
    if full_caps == "on":
        text=capital_all(text)
        params['purpose']+='Changed to Uppercase \n'
    if new_line_remover == "on":
        text=rm_new_line(text)
        params['purpose']+='Removed NewLines \n'
    if extra_space_remover == "on":
        text=rm_extra_space(text)
        params['purpose']+='Removed Extra Spaces \n'
    params['analyzed_text']=text
    return HttpResponse(params['analyzed_text'])

def rm_punc(text):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = ""
    for char in text:
        if char not in punctuations:
            analyzed = analyzed + char
    return analyzed
def capital_all(text):
    analyzed = ""
    for char in text:
        analyzed = analyzed + char.upper()
    return analyzed
def rm_new_line(text):
    analyzed = ""
    for char in text:
        if char != "\n" and char!="\r":
            analyzed = analyzed + char
    return analyzed
def rm_extra_space(text):
    analyzed = ""
    for index, char in enumerate(text):
        if not(text[index] == " " and text[index+1]==" "):
            analyzed = analyzed + char
    return analyzed