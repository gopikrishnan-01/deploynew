from django.shortcuts import render, redirect
from Mainapp.models import categorydb,productdb
from frontend.models import contactus_db, signup_db


# Create your views here.
def home_page(request):
    cat=categorydb.objects.all()
    return render(request,"homepage.html", {'cat':cat})

def product_page(request):
    pro=productdb.objects.all()
    return render(request,"products.html",{'pro':pro})

def about_page(req):
    return render(req,"aboutpage.html")


def servicespage(req):
    return render(req,"services.html")


def Contact_us(req):
    return render(req,"contact.html")

def save_contact(request):
    if request.method=="POST":
        na=request.POST.get('fname')
        em=request.POST.get('email')
        ph=request.POST.get('phone')
        sub=request.POST.get('subject')
        msg=request.POST.get('message')
        obj=contactus_db(name=na,email=em,mobile=ph,subject=sub,message=msg)
        obj.save()
        return redirect(Contact_us)

def login_page(req):
    return render(req,"login_signup.html")

def signuppage(req):
    if req.method=="POST":
        n = req.POST.get('name')
        m = req.POST.get('mobile')
        e = req.POST.get('email')
        un = req.POST.get('user')
        pw = req.POST.get('password')
        obj = signup_db(u_name=n,u_mobile=m,u_email=e,u_username=un,u_password=pw)
        obj.save()
        return redirect(login_page)


def save_signup(request):
    if request.method=="POST":
        un = request.POST.get('username')
        pwd = request.POST.get('password')
        if signup_db.objects.filter(u_username = un,u_password = pwd).exists():
            request.session['u_username'] = un
            request.session['u_password'] = pwd
            return redirect(home_page)
        else:
            return redirect(login_page)
    return redirect(login_page)


def cartpage(req):
    return render(req,"cart.html")
