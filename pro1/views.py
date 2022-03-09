from django.http import HttpResponse
def home(request):
    return HttpResponse('hello world')
def assignment(request):
    fp=open(r'C:\Users\Admin\OneDrive\Desktop\django\project1\pro1\project02.html','r')
    temp=fp.read()
    return HttpResponse(temp)











