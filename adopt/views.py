from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.http import JsonResponse
from .models import User,Post,Message
from django.core.paginator import Paginator

def index(request):
    posts = Post.objects.all().order_by("-timestamp")
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "adopt/index.html",{
        "page_obj": page_obj
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "adopt/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "adopt/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "adopt/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "adopt/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "adopt/register.html")

@login_required
def add_post(request):
    if request.method == "GET":
        return render(request,"adopt/addPost.html")
    else:
        post = Post.objects.create(created_by=request.user,animal=request.POST['animal'],desc=request.POST['desc']
        ,name=request.POST['name'],age=request.POST['age'],imageurl=request.POST['url'],State=request.POST['state'],District=request.POST['district'])
        return HttpResponseRedirect(reverse("index"))

@login_required
def profile(request,user_id):
    user_pro= User.objects.get(id=user_id)
    if request.method == "GET":
        return render(request, "adopt/user.html",{"user_profile":user_pro})
    elif request.method == "POST":
        if request.user == user_pro:
            if request.POST['_method'] == 'edit':
                return render(request, "adopt/edit_user.html",{"user_profile":user_pro})
            else:
                
                user_pro.first_name =request.POST.get('firstname')
                user_pro.last_name =request.POST.get('lastname')
                user_pro.Age=request.POST.get('age')
                user_pro.Phone=request.POST.get('phone')
                user_pro.Occupation=request.POST.get('occupation')
                if request.POST.get('garden')=='true':
                    user_pro.HasGarden=True
                else:
                    user_pro.HasGarden=False
                user_pro.save()
                return HttpResponseRedirect(reverse("profile", kwargs={'user_id':user_pro.id}))
        else:
            return render(request, "adopt/apology.html",{"message":"You cannot edit this profile"})

@login_required
def send(request,user_id):
    receiver=User.objects.get(id=user_id)
    if request.method == "GET":
        return render(request, "adopt/send.html",{"user_profile":receiver})
    else:
        message=request.POST["message"]
        new_message= Message.objects.create(sender=request.user,receiver=receiver,message=message)
        return HttpResponseRedirect(reverse("index"))

@login_required
def inbox(request):
    messages= Message.objects.filter(receiver=request.user).order_by("-timestamp")
    return render(request,"adopt/inbox.html",{"messages":messages})      

def get_message(request,message_id):
    message=Message.objects.get(id=message_id)
    return JsonResponse({"sender":message.sender.username,"sender_id":message.sender.id,"message":message.message})        
