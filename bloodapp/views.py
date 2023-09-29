from django.shortcuts import render,redirect
from bloodapp.models import *
from web.views import request,addarticles
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from datetime import datetime
from django.contrib import messages


# Create your views here.


def home(req):
    requ = RequestBD.objects.all().order_by('-Time')
    reg = RegisterDB.objects.all().order_by('-Time')
    return render(req,"home.html",{'reg':reg,'requ':requ})

def hospital(req):
    return render(req,"hospital.html")

def adminlogin(req):
    return render(req,"adminlogin.html")

def adminloginfun(req):
    if req.method=="POST":
        na =req.POST.get('username')
        ac =req.POST.get('action')
        ti = datetime.now()
        obj = AdminActivity(AdminName=na,Action=ac,Time=ti)
        obj.save()
    if req.method=="POST":
        un = req.POST.get('username')
        pw = req.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            user = authenticate(username=un,password=pw)
            if user is not None:
                login(req,user)
                req.session['username']=un
                req.session['password']=pw
                messages.success(req, "Login Successfully")
                return redirect(home)
            else:
                messages.error(req, "User or Password not matching")
                return redirect(adminlogin)
        else:
            messages.error(req, "User or Password not matching")
            return redirect(adminlogin)


def adminlogout(req):
    if req.method=="POST":
        na =req.POST.get('username')
        ac =req.POST.get('action')
        ti = datetime.now()
        obj = AdminActivity(AdminName=na,Action=ac,Time=ti)
        obj.save()
    del req.session['username']
    del req.session['password']
    messages.success(req, "Logout Successfully")
    return redirect(adminlogin)
def savehospital(req):
    if req.method=="POST":
        na =req.POST.get('name')
        ac =req.POST.get('action')
        ti = datetime.now()
        obj = AdminActivity(AdminName=na,Action=ac,Time=ti)
        obj.save()
    if req.method=="POST":
        na = req.POST.get('hname')
        di = req.POST.get('district')
        nu = req.POST.get('number')
        em = req.POST.get('email')
        ca = req.POST.get('category')
        im = req.FILES['image']
        ad = req.POST.get('address')
        obj = hospitalDB(Name=na,District=di,Number=nu,Email=em,Category=ca,Image=im,Address=ad)
        obj.save()
        messages.success(req, "Hospital Added")
        return redirect(hospital)

def hospitaldisplay(req):
    data = hospitalDB.objects.all()
    return render(req,"hospitaldisplay.html",{'data':data})

def hospitaldelete(req,dataid):
    if req.method=="POST":
        na =req.POST.get('name')
        ac =req.POST.get('action')
        ti = datetime.now()
        obj = AdminActivity(AdminName=na,Action=ac,Time=ti)
        obj.save()
    data = hospitalDB.objects.filter(id=dataid)
    data.delete()
    messages.success(req, "Hospital Deleted")
    return redirect(hospitaldisplay)

def addblood(req):
    hosp = hospitalDB.objects.all()
    return render(req,"bloodadding.html",{'hosp':hosp})

def saveblood(req):
    if req.method=="POST":
        na =req.POST.get('name')
        ac =req.POST.get('action')
        ti = datetime.now()
        obj = AdminActivity(AdminName=na,Action=ac,Time=ti)
        obj.save()
    if req.method=="POST":
        na = req.POST.get('hname')
        on = req.POST.get('Oneg')
        an = req.POST.get('Aneg')
        bn = req.POST.get('Bneg')
        abn = req.POST.get('ABneg')
        op = req.POST.get('Opos')
        ap = req.POST.get('Apos')
        bp = req.POST.get('Bpos')
        abp = req.POST.get('ABpos')
        hid = req.POST.get('hospid')
        him = hospitalDB.objects.get(id=hid)
        img = him.Image
        ti= datetime.now()
        obj = BloodDB(Name=na,ONeg=on,OPos=op,ANeg=an,APos=ap,BNeg=bn,BPos=bp,ABNeg=abn,ABPos=abp,Image=img,Time=ti)
        obj.save()
        messages.success(req, "Blood added According to Hospital")
        return redirect(addblood)

def blooddisplay(req):
    data = BloodDB.objects.all()
    return render(req,"blooddisplay.html",{'data':data})

def bloodedit(req,dataid):
    data = BloodDB.objects.get(id=dataid)
    hospdb = hospitalDB.objects.all()
    return render(req,"bloodedit.html",{'data':data,'hospdb':hospdb})

def bloodupdate(req,dataid):
    if req.method=="POST":
        na =req.POST.get('name')
        ac =req.POST.get('action')
        ti = datetime.now()
        obj = AdminActivity(AdminName=na,Action=ac,Time=ti)
        obj.save()
    if req.method=="POST":
        na = req.POST.get('hname')
        on = req.POST.get('Oneg')
        an = req.POST.get('Aneg')
        bn = req.POST.get('Bneg')
        abn = req.POST.get('ABneg')
        op = req.POST.get('Opos')
        ap = req.POST.get('Apos')
        bp = req.POST.get('Bpos')
        abp = req.POST.get('ABpos')
        ti = datetime.now()
        BloodDB.objects.filter(id=dataid).update(Name=na,ONeg=on,OPos=op,ANeg=an,APos=ap,BNeg=bn,BPos=bp,ABNeg=abn,ABPos=abp,Time=ti)
        messages.success(req, "Blood Updated")
        return redirect(blooddisplay)


def blooddelete(req,dataid):
    data = BloodDB.objects.filter(id=dataid)
    data.delete()
    messages.success(req, "Blood Deleted")
    return redirect(blooddisplay)

def requesthisory(req):
    data = hospitalDB.objects.all()
    return render(req,"requesthisory.html",{'data':data})

def saverequest(req):
    if req.method=="POST":
        em = req.POST.get('email')
        ac = req.POST.get('action')
        ti = datetime.now()
        obj = UserActivity(Email=em,Action=ac,Time=ti)
        obj.save()
    if req.method=="POST":
        em = req.POST.get('email')
        na = req.POST.get('name')
        by = req.POST.get('bystander')
        gr = req.POST.get('group')
        di = req.POST.get('district')
        da = req.POST.get('date')
        co = req.POST.get('number')
        ho = req.POST.get('hospital')
        pl = req.POST.get('place')
        re = req.POST.get('reason')
        ti = datetime.now()
        obj = RequestBD(Email=em,Name=na,Bystander=by,BloodGroup=gr,District=di,Date=da,ContactNumber=co,Hospital=ho,Reason=re,Place=pl,Time=ti)
        obj.save()
        messages.success(req, "Request Created")
        return redirect(request)

def displaydonate(req):
    data = BloodDonation.objects.all()
    return render(req,"displaydonate.html",{"data":data})

def displayrequest(req):
    data = RequestBD.objects.all()
    old = OldRequestBD.objects.all()
    return render(req,"displayrequest.html",{'data':data,'old':old})

def deleterequest(req,dataid):
    data = RequestBD.objects.filter(id=dataid)
    data.delete()
    return redirect(displayrequest)

def deleteoldrequest(req,dataid):
    data = OldRequestBD.objects.filter(id=dataid)
    data.delete()
    return redirect(displayrequest)

def displaysupport(req):
    data = ContactDB.objects.all()
    return render(req,"displaysupport.html",{'data':data})

def displayregister(req):
    data = RegisterDB.objects.all().order_by('-Time')
    return render(req,"displayregister.html",{'data':data})

def deleteregister(req,dataid):
    data = RegisterDB.objects.filter(id=dataid)
    data.delete()
    return redirect(displayregister)

def adminactivity(req):
    act = AdminActivity.objects.all().order_by('-Time')
    return render(req,"adminactivity.html",{'act':act})

def useractivity(req):
    act = UserActivity.objects.all().order_by('-Time')
    return render(req,'useractivity.html',{'act':act})

def faqnotes(req):
    return render(req,"faqnotes.html")

def savefaq(req):
    if req.method=="POST":
        na =req.POST.get('name')
        ac =req.POST.get('action')
        ti = datetime.now()
        obj = AdminActivity(AdminName=na,Action=ac,Time=ti)
        obj.save()
    if req.method=="POST":
        ti = req.POST.get('title')
        te = req.POST.get('text')
        obj = FaqDB(Title=ti,Text=te)
        obj.save()
        messages.success(req, "FAQ Added")
        return redirect(faqnotes)

def displayfaq(req):
    data = FaqDB.objects.all()
    return render(req,"displayfaq.html",{'data':data})

def article(req):
    return render(req,"article.html")

def savearticle(req):
    if req.method=="POST":
        na =req.POST.get('name')
        ac =req.POST.get('action')
        ti = datetime.now()
        obj = AdminActivity(AdminName=na,Action=ac,Time=ti)
        obj.save()
    if req.method=="POST":
        ti = req.POST.get('title')
        au = req.POST.get('author')
        ca = req.POST.get('category')
        im = req.FILES['image']
        p1 = req.POST.get('p1')
        p2 = req.POST.get('p2')
        p3 = req.POST.get('p3')
        tim = datetime.now()
        obj = ArticleDB(Title=ti,Author=au,Category=ca,Image=im,Paragraph1=p1,Paragraph2=p2,Paragraph3=p3,Time=tim)
        obj.save()
        messages.success(req, "Article Created")
        return redirect(article)

def displayarticles(req):
    data = ArticleDB.objects.all().order_by('-Time')
    return render(req,"displayarticles.html",{'data':data})

def deletearticle(req,dataid):
    data = ArticleDB.objects.filter(id=dataid)
    data.delete()
    return redirect(displayarticles)

