from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Message
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.urls import reverse



@login_required
def index(request, session_id):#FLAW 2 fix: remove session_id from arguments
    messages = Message.objects.filter(owner=request.user)
    return render(request, 'pages/index.html', {'messages': messages, 'session_id':session_id} ) #FLAW 2 fix: remove 'session_id':session_id from arguments


#FLAW 2 fix: remove this view
@login_required
def session(request):
    if not request.session.session_key:
        request.session.create()

    session_id = request.session.session_key

    url = reverse('index', kwargs={'session_id': session_id})
    return redirect(url)

#FLAW X fix: add @login_required as a decorator
@csrf_exempt # FLAW 1 fix : delete this line
def changeUsername(request): #FLAW 2 fix: remove session_id from arguments
    changee = User.objects.get(username=request.POST['user']) #FLAW X fix: change the get() parameter to "username=request.user"
    changee.username = request.POST['username']
    changee.save()
    print("username changed to:" + changee.username)
    messages = Message.objects.filter(owner=changee.username)
    return redirect('/messenger', {'messages': messages})