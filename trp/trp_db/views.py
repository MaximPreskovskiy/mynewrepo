from django.shortcuts import render, redirect
from trp_db.models import CommNumber, Spareparts
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, logout, login


def index(request):
    print("test")
    name = request.session.get("user_id", None)
    
    if name !=None:
        name = name
    return render(request, "index.html", {"name":name})

def orders(request):
    name = request.session.get("user_id", None)
    
    if name !=None:
        name = name
    return render(request, "orders.html", {"name":name})

def spareparts(request):
    name = request.session.get("user_id", None)
    new = Spareparts.objects.all()
    if name !=None:
        name = name
    return render(request, "spareparts.html", {"name":name, "new":new})

def search(request):
    new = None
    if request.method == "POST":
        data = request.POST
        new = CommNumber.objects.filter(ID_CommNumber=data["search"])

    name = request.session.get("user_id", None)
    
    if name !=None:
        name = name

    return render(request,"search.html", {"name":name,"result":new})

def auth(request):
    if request.method == "POST":
        auth_data = request.POST
        user = authenticate(username=auth_data["username"], password=auth_data["password"])
       
        if user != None:
           request.session["user_id"]= user.username
          
           login(request, user)
           return redirect("http://127.0.0.1:8000/")
        
    
    #else:
     #   return render(request,"auth.html")

def reg(request):
    if request.method == "POST":
        reg_data = request.POST
        new = User.objects.create_user(username = reg_data["reg_username"], password = reg_data["reg_password"])
        new.save()
        return redirect("http://127.0.0.1:8000/")

    

def order_card(request, ID_CommNumber):
    new = CommNumber.objects.filter(ID_CommNumber = ID_CommNumber)
   
    name = request.session.get("user_id", None)
   
    if name !=None:
        name = name
    return render(request, "order_card.html", {"name":name,"new":new}) 

def prod_card(request, id_num):
    name = request.session.get("user_id", None)
    new = Spareparts.objects.filter(id_num = id_num)
    if name !=None:
        name = name
    return render(request, "prod_card.html", {"name":name, "new":new})

def logout_user(request):
    if request.method == "POST":            
        logout(request)
        return redirect("http://127.0.0.1:8000/")