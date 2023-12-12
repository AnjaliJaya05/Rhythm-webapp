from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from .forms import *
from .models import *
import os

# Create your views here.

def index(request):
    return render(request,'index.html')


def reg(request):
    if request.method=='POST':
        a=Regform(request.POST)
        if a.is_valid():
            n=a.cleaned_data['name']
            em=a.cleaned_data['email']
            ad=a.cleaned_data['address']
            pin=a.cleaned_data['pincode']
            phn=a.cleaned_data['phone']
            ps=a.cleaned_data['password']
            cps=a.cleaned_data['cpassword']
            if ps==cps:
                b=Regmodel(name=n,email=em,address=ad,pincode=pin,phone=phn,password=ps)
                b.save()
                subject = "your account has been created"
                message = "you have created an account in Rhythm.Thank you!!!"
                email_from = 'anjalijo543@gmail.com'
                email_to = em
                send_mail(subject, message, email_from, [email_to])
                return redirect(log)
            else:
                return HttpResponse("password doesnot match")
        else:
            return HttpResponse("registration failed")
    return render(request,'reg.html',{'id':id})

def log(request):
    if request.method=='POST':
        a=Logform(request.POST)
        if a.is_valid():
            em=a.cleaned_data['email']
            psw=a.cleaned_data['password']
            b=Regmodel.objects.all()
            for i in b:
                if i.email==em and i.password==psw:
                    request.session['id']=i.id
                    return redirect(index1)
            else:
                return HttpResponse("login failed")
    return render(request,'login.html')

def index1(request):
    a=add_promodel.objects.all()
    id1=[]
    n=[]
    d=[]
    p=[]
    o=[]
    im=[]
    for i in a:
        id=i.id
        id1.append(id)
        na=i.pname
        n.append(na)
        de=i.des
        d.append(de)
        pr=i.pri
        of=i.offer
        o.append(of)
        p.append(pr)
        im1=str(i.file).split('/')[-1]
        im.append(im1)
    pair=zip(n,d,p,o,im,id1)
    return render(request,'index1.html',{'a':pair})



def adminlogin(request):
    if request.method=='POST':
        a=adminform(request.POST)
        if a.is_valid():
            username=a.cleaned_data['username']
            password=a.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                return redirect(alog)
            else:
                return HttpResponse("login failed")
    return render(request,'admin_login.html')

def alog(request):
    return render(request,'admin_button.html')

def add_pro(request):
    if request.method=='POST':
        a=add_proform(request.POST,request.FILES)
        if a.is_valid():
            image=a.cleaned_data['file']
            nam=a.cleaned_data['pname']
            description=a.cleaned_data['des']
            price=a.cleaned_data['pri']
            off=a.cleaned_data['offer']
            b=add_promodel(file=image,pname=nam,des=description,pri=price,offer=off)
            b.save()
            return redirect(index1)
        else:
            return HttpResponse("failed")
    return render(request,'add_pro.html')

def pro_display(request):
    a=add_promodel.objects.all()
    id1=[]
    n=[]
    d=[]
    p=[]
    o=[]
    img=[]
    for i in a:
        id=i.id
        id1.append(id)
        nam=i.pname
        n.append(nam)
        de=i.des
        d.append(de)
        pr=i.pri
        p.append(pr)
        of=i.offer
        o.append(of)
        im=str(i.file).split('/')[-1]
        img.append(im)
    pair=zip(n,d,p,o,img,id1)
    return render(request,'pro_display.html',{'a':pair})

def pro_del(request,id):
    a=add_promodel.objects.get(id=id)
    a.delete()
    return redirect(pro_display)

def pro_edit(request,id):
    a=add_promodel.objects.get(id=id)
    img=str(a.file).split('/')[-1]
    if request.method == 'POST':
        a.name=request.POST.get('pname')
        a.des=request.POST.get('des')
        a.pri=request.POST.get('pri')
        a.offer=request.POST.get('offer')
        if len(request.FILES)!=0:
            if len(a.file)>0:
                os.remove(a.file.path)
            a.file=request.FILES['file']
        a.save()
        return redirect(pro_display)
    return render(request,'pro_edit.html',{'a':a,'img':img})

def wish(request,id):
    a=add_promodel.objects.get(id=id)
    b=wishmodel.objects.all()
    for i in b:
        if i.proid==a.id:
            return HttpResponse("item already in wishlist")
    c=wishmodel(pname=a.pname,des=a.des,pri=a.pri,offer=a.offer,proid=a.id,file=a.file)
    c.save()
    return redirect(wishdisplay)



def wishdisplay(request):
    a=wishmodel.objects.all()
    Id1=[]
    n=[]
    d=[]
    p=[]
    o=[]
    f=[]
    for i in a:
        id=i.id
        Id1.append(id)
        na=i.pname
        n.append(na)
        de=i.des
        d.append(de)
        pr=i.pri
        p.append(pr)
        of=i.offer
        o.append(of)
        fi=str(i.file).split('/')[-1]
        f.append(fi)
    pair=zip(n,d,p,o,f,Id1)
    return render(request,'wishlist.html',{'a':pair})

def wish_rem(request,id):
    a=wishmodel.objects.get(id=id)
    a.delete()
    return redirect(wishdisplay)

def cart(request,id):
    a=add_promodel.objects.get(id=id)
    b=cartmodel.objects.all()
    for i in b:
        if a.id==i.proid:
            return HttpResponse("item already in cart")
    c=cartmodel(proid=a.id,pname=a.pname,des=a.des,pri=a.pri,offer=a.offer,file=a.file)
    c.save()
    # return render(request,'cart.html',{'a':a,'b':b,'c':c})
    return redirect(cartdisplay)

def cartdisplay(request):
    a=cartmodel.objects.all()
    Id1=[]
    n=[]
    d=[]
    p=[]
    o=[]
    f=[]
    for i in a:
        id=i.id
        Id1.append(id)
        na=i.pname
        n.append(na)
        de=i.des
        d.append(de)
        pr=i.pri
        p.append(pr)
        of=i.offer
        o.append(of)
        fi=str(i.file).split('/')[-1]
        f.append(fi)
    pair=zip(n,d,p,o,f,Id1)
    return render(request,'cart.html',{'a':pair})


def cart_rem(request,id):
    a=cartmodel.objects.get(id=id)
    a.delete()
    return redirect(cartdisplay)

def profile(request):
    id1=request.session['id']
    a=Regmodel.objects.get(id=id1)
    return render(request, 'profile.html',{'a': a})

def edit(request,id):
    a=Regmodel.objects.get(id=id)
    if request.method=='POST':
        a.name=request.POST.get('name')
        a.email=request.POST.get('email')
        a.address=request.POST.get('address')
        a.pincode=request.POST.get('pincode')
        a.phone=request.POST.get('phone')
        a.save()
        return redirect(profile)
    return render(request,'edit_profile.html',{'a':a})

def logout_view(request):
    logout(request)
    return redirect(index)

def change(request,id):
    a=Regmodel.objects.get(id=id)
    if request.method=='POST':
        p1=request.POST.get('password')
        p2=request.POST.get('cpassword')
        if p1==p2:
            a.password=p1
            a.save()
            return HttpResponse("password changed")
        else:
            return HttpResponse("sorry")
    return render(request,'change.html')

def forgot_password(request):
    a=Regmodel.objects.all()
    if request.method=='POST':
        em=request.POST.get('email')
        n=request.POST.get('name')
        for i in a:
            if (i.email==em and i.name==n):
                id=i.id
                subject="password change"
                message=f"http://127.0.0.1:8000/web_app/change/{id}"
                frm="anjalijo543@gmail.com"
                to=em
                send_mail(subject,message,frm,[to])
                return HttpResponse("check mail")
        else:
            return  HttpResponse("sorry")
    return render(request,'forgot_password.html')

def check(request,id):
    b=cartmodel.objects.get(id=id)
    request.session['pri'] =b.pri
    request.session['pname']=b.pname
    if request.method == 'POST':
        n=request.POST.get('name')
        ad= request.POST.get('address')
        pin = request.POST.get('pincode')
        phn= request.POST.get('phone')
        pri=request.POST.get('pri')
        pname=request.POST.get('pname')
        pay=request.POST.get('payment')
        c=checkout(name=n,address=ad,pincode=pin,phone=phn,pri=pri,pname=pname,payment=pay)
        c.save()
        request.session['name'] =n
        request.session['address'] =ad
        request.session['pincode'] =pin
        request.session['phone'] = phn
        payment=request.POST.get('select')
        if payment== "Cash on Delivery":
            b.delete()
            return redirect (success)
        elif payment=="Credit/Debit Card":
            b.delete()
            return redirect (card)
    return render(request, 'checkout.html', {'b':b})


def success(request):
    pri= request.session['pri']
    name=request.session['pname']
    return render(request,'success.html',{'pri':pri,'pname':name})

def card(request):
    if request.method=='POST':
        a=cardform(request.POST)
        if a.is_valid():
            n=a.cleaned_data['cno']
            e= a.cleaned_data['mm']
            ex=a.cleaned_data['yy']
            c=a.cleaned_data['cvv']
            na= a.cleaned_data['cname']
            b=cardmodel(cno=n,mm=e,yy=ex,cvv=c,cname=na)
            b.save()
            return redirect (success)
        else:
            return HttpResponse("failed")
    return render(request,'card.html')


