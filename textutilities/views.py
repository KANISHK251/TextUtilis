from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

# def index(request):
#     nav = '''
#         <p>Home Page</p>
#         <ul>
#         <li> <a href = "capitalize">To Capitailze</a></li>
#         <li> <a href = "removepunc">To Remove Punctuation</a></li>
#         <li> <a href = "newlineremove">To Remove New Line</a></li>
#         <li> <a href = "spaceremove">To Remove Space</a></li>
#         <li> <a href = "charcount">To count characters</a></li>
#         </ul>'''
#     return HttpResponse(nav)

def  aboutus(request):
    return render(request,'aboutus.html')


def analyze(request):
    djtext = request.POST.get('text','default')
    punc = request.POST.get('removepunc','off')
    capital = request.POST.get('capitalize','off')
    extraspaceremove = request.POST.get('extraspaceremove','off')
    newlineremove = request.POST.get('newlineremove','off')
    charcount = request.POST .get('charcount','off')

    operations = []

    
    # print(djtext)
    # print(punc)
    if punc == 'on':
        analyze = ""
        punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for char in range(len(djtext)):
            if djtext[char] not in punctuation:
                analyze=analyze+djtext[char]
            
        operations.append({'operation' : 'remove_punctuation', 'result' : analyze})
    
    
    if capital == 'on':
        analyze = ""
        analyze = djtext.upper()
        operations.append({'operation' : 'capitalize', 'result' : analyze})
      

    if newlineremove == 'on':
        analyze=""
        for char in djtext:
            if char != '\n':
                analyze = analyze+char
        operations.append({'operation' : 'remove_newline', 'result' : analyze})

      
    if extraspaceremove == 'on':
        analyze  = ""
        for index in range(len(djtext)):
            if djtext[index]!=" " or djtext[index+1]!=" ":
                analyze = analyze+djtext[index]
        operations.append({'operation' : 'remove_extraspace', 'result' : analyze})
    

    if charcount == 'on':
        count=0
        for char in djtext:
            if char!= "  ":
                count+=1
        analyze = count
        operations.append({'operation' : 'char_count', 'result' : analyze})    

    # else:
    #     return HttpResponse("Error 404")
    
    params = {'oper' : operations}
    return render(request,'analyze.html',params)
 
    



def removepunc(request):
    djtext = request.GET.get('text','default')
    print(djtext)
    return HttpResponse('''It will remove the punctuation <br><a href = "/">Back Button''')

def capitalize(request):
    return HttpResponse('''It will capital the letter <br><a href = "/">Back Button''')

def newlineremove(request):
    return HttpResponse('''It will remove the newline <br><a href = "/">Back Button''')

def spaceremove(request):
    return HttpResponse('''It will remove the space <br><a href = "/">Back Button''')

def charcount(request):
    return HttpResponse('''It will count the characters <br><a href = "/">Back Button''')

