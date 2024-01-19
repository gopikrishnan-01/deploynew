from django.shortcuts import render, redirect

from Mainapp.models import categorydb, productdb
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate

# Create your views here.
def indexfn(request):
    return render(request,"index.html")

def category(request):
    return render(request,"AddCategory.html")

def savecategory(req):
    if req.method=="POST":
        cn=req.POST.get('cname')
        ca=req.POST.get('caddress')
        ci=req.FILES['cimage']
        obj=categorydb(category_name=cn,category_description=ca,category_image=ci)
        obj.save()
        return redirect(category)


def displaycat(request):
    cat=categorydb.objects.all()
    return render(request,"display_category.html",{'cat':cat})

def Admin_login(req):
    return render(req,"Admin_login.html")


def Add_product(request):
    category=categorydb.objects.all()
    return render(request,"addproducts.html",{'category':category})


def save_product(request):
    if request.method=="POST":
        cat=request.POST.get('category')
        na=request.POST.get('pname')
        des=request.POST.get('pdescription')
        pr=request.POST.get('pprice')
        img=request.FILES['pimage']
        obj=productdb(cat_name=cat,product_name=na,Description=des,price=pr,product_image=img)
        obj.save()
        return redirect(Add_product)

def display_product(req):
    product=productdb.objects.all()
    return render(req,"displayproducts.html",{'product':product})

def edit_products(request,pro_id):
    cat=categorydb.objects.all()
    pro=productdb.objects.get(id=pro_id)
    return render(request,"Edit_products.html",{'cat':cat, 'pro':pro})

def adminlogin(request):
    if request.method=="POST":
        un=request.POST.get('user_name')
        pwd=request.POST.get('pass_word')

        if User.objects.filter(username__contains=un).exists():
            user = authenticate(username=un,password=pwd)
            if user is not None:
                login(request,user)
                request.session['username']=un
                request.session['password']=pwd
                return redirect(indexfn)
            else:
                return redirect(Admin_login)

        else:
            return redirect(Admin_login)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(Admin_login)
