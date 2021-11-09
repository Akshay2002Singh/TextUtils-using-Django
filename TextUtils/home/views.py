from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def analyze(request):
    # get text
    text=request.POST.get('text','default')
    # print(text)
    remove_punc = request.POST.get('removepunc', 'off')
    full_caps = request.POST.get('fullcaps', 'off')
    remove_number = request.POST.get('remove_numbers', 'off')
    new_line_rem = request.POST.get('rmnewline', 'off')
    extra_space_remover = request.POST.get('extraspaceremover', 'off')
    params = {'purpose': "", 'analyzed_text':""}
    #Check which checkbox is on
    if remove_punc == "on":
        text=rm_punc(text)
        params['purpose']+='Removed Punctuations \n'
    if full_caps == "on":
        text=capital_all(text)
        params['purpose']+='Changed to Uppercase \n'
    if remove_number == "on":
        text=rm_number(text)
        params['purpose']+='Numbers Removed\n'
    if new_line_rem == 'on':
        text=rm_new_line(text)
        params['purpose']+='Removed NewL ines \n'
    if extra_space_remover == "on":
        text=rm_extra_space(text)
        params['purpose']+='Removed Extra Spaces \n'
    params['analyzed_text']=text
    return render(request,'analyzed_text.html',params)
    # return HttpResponse(params['analyzed_text'])

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
def rm_number(text):
    analyzed = ""
    numbers = '''0123456789'''
    analyzed = ""
    for char in text:
        if char not in numbers:
            analyzed = analyzed + char
    return analyzed
def rm_new_line(text):
    analyzed = ""
    for char in text:
        if char != "\n":
            analyzed = analyzed + char
    return analyzed
def rm_extra_space(text):
    analyzed = ""
    for index, char in enumerate(text):
        if not(text[index] == " " and text[index+1]==" "):
            analyzed = analyzed + char
    return analyzed