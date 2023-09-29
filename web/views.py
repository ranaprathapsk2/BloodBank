from datetime import datetime
from django.contrib import messages
from django.shortcuts import render,redirect
from bloodapp.models import *

# Create your views here.

def index(req):
    hospital = hospitalDB.objects.all()
    blood = BloodDB.objects.all()
    data = RequestBD.objects.all()
    return render(req,"index.html",{'data':data,'hospital':hospital,'blood':blood,})

def check(req):
    data = BloodDB.objects.all()
    return render(req,"bloodcheck.html",{'data':data})

def volunteer(req):
    data = RegisterDB.objects.filter(Email=req.session['email'])
    return render(req,"volunteer.html",{'data':data})

def register(req):
    return render(req,"register.html")

def loginpage(req):
    return render(req,"loginpage.html")

def contact(req):
    return render(req,"contact.html")

def about(req):
    return render(req,"about.html")

def faq(req):
    data = FaqDB.objects.all()
    return render(req,"faq.html",{'data':data})

def news(req):
    data = ArticleDB.objects.all().order_by('-Time')
    return render(req,"news.html",{'data':data})

def singlearticle(req,dataid):
    getid = ArticleDB.objects.filter(id=dataid)
    data = RegisterDB.objects.filter(Email=req.session['email'])
    rec = ArticleDB.objects.all().order_by('-Time')
    det = ArticleDB.objects.get(id=dataid)
    com = CommentDB.objects.filter(Idd=dataid)
    return render(req,"details.html",{'det':det,'rec':rec,'data':data,'getid':getid,'com':com})

def donations(req):
    return render(req,"donations.html")

def request(req):
    data = RegisterDB.objects.filter(Email=req.session['email'])
    return render(req,"request.html",{"data":data})

def donate(req):
    data = RegisterDB.objects.all()
    return render(req,"donate.html",{"data":data})

def blooddonate(req):
    data = RegisterDB.objects.filter(Email=req.session['email'])
    return render(req,"blooddonate.html",{"data":data})



def profile(req):
    now = RequestBD.objects.filter(Email=req.session['email'])
    allrequests = RegisterDB.objects.filter(Email=req.session['email'])
    old = OldRequestBD.objects.filter(Email=req.session['email']).order_by('-Time')
    return render(req,"profile.html",{"allrequests":allrequests,"now":now,"old":old})

def testing(req):
    data = OldRequestBD.objects.all()
    return render(req,"testing.html",{'data':data})

def saveregister(req):
    if req.method=="POST":
        em = req.POST.get('email')
        ac = req.POST.get('action')
        ti = datetime.now()
        obj = UserActivity(Email=em,Action=ac,Time=ti)
        obj.save()
    if req.method=="POST":
        em = req.POST.get('email')
        na = req.POST.get('name')
        bg = req.POST.get('group')
        pw = req.POST.get('password')
        ln = req.POST.get('lname')
        di = req.POST.get('district')
        pl = req.POST.get('place')
        ge = req.POST.get('gender')
        ag = req.POST.get('age')
        nu = req.POST.get('number')
        rp = req.POST.get('repassword')
        ti = datetime.now()
        obj = RegisterDB(Email=em, Name=na, BloodGroup=bg, Password=pw,LastName=ln,District=di,Place=pl,Gender=ge,Age=ag,MobileNumber=nu,RePassword=rp,Time=ti)
        obj.save()
        messages.success(req, "User Registered. Now Login")
        return redirect(register)

def login(req):
    if req.method=="POST":
        em = req.POST.get('email')
        ac = req.POST.get('action')
        ti = datetime.now()
        obj = UserActivity(Email=em,Action=ac,Time=ti)
        obj.save()
    if req.method=="POST":
        em = req.POST.get('email')
        pw = req.POST.get('password')
        if RegisterDB.objects.filter(Email=em,Password=pw).exists():
            req.session['email'] =em
            req.session['password'] =pw
            messages.success(req, "Login Successfully")
            return redirect(index)
        else:
            messages.error(req, "User or Password not matching")
            return redirect(login)
    else:
        messages.error(req, "User or Password not matching")
        return redirect(login)

def logout(req):
    if req.method=="POST":
        em = req.POST.get('email')
        ac = req.POST.get('action')
        ti = datetime.now()
        obj = UserActivity(Email=em,Action=ac,Time=ti)
        obj.save()
    del req.session['email']
    del req.session['password']
    messages.success(req, "Logout Successfully")
    return redirect(index)

def profileedit(req,dataid):
    data = RegisterDB.objects.get(id=dataid)
    return render(req,"profileedit.html",{"data":data})

def savedonations(req):
    if req.method=="POST":
        em = req.POST.get('email')
        ac = req.POST.get('action')
        ti = datetime.now()
        obj = UserActivity(Email=em,Action=ac,Time=ti)
        obj.save()
    if req.method=="POST":
        em = req.POST.get('email')
        na = req.POST.get('name')
        ln = req.POST.get('lname')
        ag = req.POST.get('age')
        bg = req.POST.get('group')
        di = req.POST.get('district')
        pl = req.POST.get('place')
        ge = req.POST.get('gender')
        nu = req.POST.get('number')
        bb = req.POST.get('bloodbank')
        de = req.POST.get('diseases')
        ti = datetime.now()
        obj = BloodDonation(Email=em, Name=na, BloodGroup=bg, LastName=ln, District=di, Place=pl, Gender=ge, Age=ag, MobileNumber=nu, BloodBank=bb, Diseases=de,Time=ti)
        obj.save()
        messages.success(req, "Donation Blood Created.More Details will Through Email. Check your Email")
        return redirect(blooddonate)


def deleteandsave(req,dataid):
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
        obj = OldRequestBD(Email=em, Name=na, Bystander=by, BloodGroup=gr, District=di, Date=da, ContactNumber=co, Hospital=ho, Reason=re, Place=pl,Time=ti)
        obj.save()
    data = RequestBD.objects.filter(id=dataid)
    data.delete()
    messages.success(req, "Request Deleted")
    return redirect(profile)

def savevolunteer(req):
    if req.method=="POST":
        em = req.POST.get('email')
        ac = req.POST.get('action')
        ti = datetime.now()
        obj = UserActivity(Email=em,Action=ac,Time=ti)
        obj.save()
    if req.method=="POST":
        na = req.POST.get('name')
        em = req.POST.get('email')
        su = req.POST.get('subject')
        cv = req.FILES['cv']
        me = req.POST.get('message')
        obj = VolunteerDB(Email=em,Name=na,Subject=su,Cv=cv,Message=me)
        obj.save()
        messages.success(req, "Volunteer Form Created. Will Contact You Soon...")
        return redirect(volunteer)

def savecontact(req):
    if req.method=="POST":
        em = req.POST.get('email')
        ac = req.POST.get('action')
        ti = datetime.now()
        obj = UserActivity(Email=em,Action=ac,Time=ti)
        obj.save()
    if req.method=="POST":
        na = req.POST.get('name')
        em = req.POST.get('email')
        su = req.POST.get('subject')
        me = req.POST.get('message')
        obj = ContactDB(Name=na,Email=em,Subject=su,Message=me)
        obj.save()
        messages.success(req, "Contact Form Created.Will Contact Soon.")
        return redirect(contact)

def savecomment(req):
    if req.method=="POST":
        em = req.POST.get('email')
        ac = req.POST.get('action')
        ti = datetime.now()
        obj = UserActivity(Email=em,Action=ac,Time=ti)
        obj.save()
    if req.method=="POST":
        idd = req.POST.get('idd')
        na = req.POST.get('name')
        em = req.POST.get('email')
        co = req.POST.get('comment')
        obj = CommentDB(Idd=idd,Name=na,Email=em,Comment=co)
        obj.save()
        return redirect(news)

def addarticles(req):
    data = RegisterDB.objects.filter(Email=req.session['email'])
    return render(req,"addarticles.html",{'data':data})

def savearticlebyuser(req):
    if req.method=="POST":
        em = req.POST.get('email')
        ac = req.POST.get('action')
        ti = datetime.now()
        obj = UserActivity(Email=em,Action=ac,Time=ti)
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
        return redirect(addarticles)

def community(req):
    ques = QuestionDB.objects.all().order_by('-Time')
    data = RegisterDB.objects.filter(Email=req.session['email'])
    return render(req,"community.html",{'data':data,'ques':ques})

def singlequestion(req,dataid):
    com = QuestionCommentDB.objects.filter(Idd=dataid)
    getid = ArticleDB.objects.filter(id=dataid)
    reg = RegisterDB.objects.filter(Email=req.session['email'])
    data = QuestionDB.objects.get(id=dataid)
    return render(req,"question.html",{'data':data,'getid':getid,'reg':reg,'com':com})

def savequestion(req):
    if req.method=="POST":
        em = req.POST.get('email')
        ac = req.POST.get('action')
        ti = datetime.now()
        obj = UserActivity(Email=em,Action=ac,Time=ti)
        obj.save()
    if req.method=="POST":
        na = req.POST.get('name')
        em = req.POST.get('email')
        qu = req.POST.get('question')
        ti = datetime.now()
        obj = QuestionDB(Name=na,Email=em,Question=qu,Time=ti)
        obj.save()
        messages.success(req, "Question Added.")
        return redirect(community)

def savequestioncomment(req):
    if req.method=="POST":
        em = req.POST.get('email')
        ac = req.POST.get('action')
        ti = datetime.now()
        obj = UserActivity(Email=em,Action=ac,Time=ti)
        obj.save()
    if req.method=="POST":
        idd = req.POST.get('idd')
        na = req.POST.get('name')
        em = req.POST.get('email')
        co = req.POST.get('comment')
        obj = QuestionCommentDB(Idd=idd,Name=na,Email=em,Comment=co)
        obj.save()
        return redirect(community)

def requestchat(req,dataid):
    reg = RegisterDB.objects.filter(Email=req.session['email'])
    getid = RequestBD.objects.filter(id=dataid)
    data = RequestBD.objects.filter(id=dataid)
    com = RequestCommentDB.objects.filter(Idd=dataid)
    return render(req,"requestchat.html",{'data':data,'getid':getid,'reg':reg,'com':com})

def saverequestcomment(req):
    if req.method=="POST":
        em = req.POST.get('email')
        ac = req.POST.get('action')
        ti = datetime.now()
        obj = UserActivity(Email=em,Action=ac,Time=ti)
        obj.save()
    if req.method=="POST":
        idd = req.POST.get('idd')
        na = req.POST.get('name')
        em = req.POST.get('email')
        co = req.POST.get('comment')
        ti = datetime.now()
        obj = RequestCommentDB(Idd=idd,Name=na,Email=em,Comment=co,Time=ti)
        obj.save()
        return redirect(index)
