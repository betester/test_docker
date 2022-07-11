from django.shortcuts import render,HttpResponse

# Create your views here.
def hello_world(request):
    if request.user.is_authenticated :
        return HttpResponse(f"<h1>hello {request.user.username}</h1>")
    return HttpResponse("Hello unknown user")