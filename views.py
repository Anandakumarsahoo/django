from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.


def register(request):
    if request.method == "POST":
        u_fname = request.POST.get("first_name")
        u_lname = request.POST.get("last_name")
        u_name = request.POST.get("username")
        u_email = request.POST.get("email")
        u_pass = request.POST.get("password")
        print(u_fname,u_lname,u_name,u_email,u_pass)
        User.objects.create_user(first_name=u_fname,last_name=u_lname,username=u_name, email=u_email, password=u_pass)  
        return redirect('login')   
    
    elif request.method == "GET":
          print("come to get methord")

    return render(request,'register.html')


def login(request): 
    u_name = request.POST.get("name")
    u_pass = request.POST.get("password")

    user = authenticate(request, username=u_name, password=u_pass)
    if user is not None:
           
            auth_login(request, user)
            return redirect('dashboard')  
    else:
            
            messages.error(request, "Invalid username or password.")
            return render(request, 'login.html')

  
def dashboard(request):
      return render(request,'dashboard.html')

def user_list(request):
    users = User.objects.all() 
    return render(request, 'alluser.html', {'users': users})
     

def edit_user(request,id):      
      if request.method == "POST":
        user  = User.objects.get(id=id)
        print(user)
        u_fname = request.POST.get("first_name")
        u_lname = request.POST.get("last_name")

        u_email = request.POST.get("email")
        print(user, "hg")

        user.first_name = u_fname
        user.last_name = u_lname
        user.email = u_email
        user.save()
        print(user,"sdsda")

        messages.success(request, "User updated successfully!")
        return redirect('userlist')
      
      elif request.method == "GET":
        user = User.objects.get(id = id)
        return render(request,'edit_user.html',{'user_obj': user})
      
      



def delete_user(request, id):
    if request.method == "GET":
        user = User.objects.get(id=id)


        user.delete()
        messages.success(request, "User deleted successfully!")
        print('ghghgjg')
        return redirect('userlist')
# def add_user(request):
#      return HttpResponse("ffjhf")
def add_user(request):
    if request.method == "POST":
        u_fname = request.POST.get("first_name")
        u_lname = request.POST.get("last_name")
        u_name = request.POST.get("username")
        u_email = request.POST.get("email")
        User.objects.create_user(first_name=u_fname,last_name=u_lname,username=u_name, email=u_email) 

        return redirect('userlist')
    
    return render(request,'add.html')
    



     
     
     
 

    
