from django.shortcuts import render
from django.http import HttpResponse
from .models import signup
from .models import signin
def input(request):
    return render(request,'register.html')
def reg(request):
    if request.method == "POST":
        firstname1 = request.POST['fn']
        lastname1 = request.POST['ln']
        dob1 = request.POST['db']
        city1 = request.POST['ct']
        state1 = request.POST['st']
        pincode1 = request.POST['pc']
        about1 = request.POST['ay']
        gender1 = request.POST['gd']
        email1 = request.POST['em']
        phnum1 = request.POST['pn']
        username1 = request.POST['un']
        password1 = request.POST['pd']
        confpass1 = request.POST['cp']
        answer1 = request.POST['ya']
        f = signup(firstname=firstname1,lastname=lastname1,dob=dob1,city=city1,state=state1,pincode=pincode1,
                   about=about1,gender=gender1,email=email1,phnum=phnum1,username=username1,password=password1,
                   confpass=confpass1,answer=answer1)
        f.save()
    return HttpResponse("successfully registerd")
    #else:
        #return render(request, 'regi.html')
def log(request):
    if request.method == "POST":
        email = request.POST['username']
        username = request.POST['username']
        #phnum = request.POST['username']
        password = request.POST['password']
        dbuser1 = signup.objects.filter(email =email,password=password)
        dbuser2 = signup.objects.filter(username =username, password=password)
        #dbuser3 = signup.objects.filter(phnum =phnum, password=password)
        v = signin(email=email,username=username,phnum=phnum,password=password) #
        v.save()
        if email or username or phnum !="" and password !="": #
            if dbuser1 or dbuser2 or dbuser3:
                #return render(request, "home.html")
                return HttpResponse("login success")
            else:
                return HttpResponse("login failed")
        else:
            return render(request,"login.html")
    else:

        return render(request,"login.html")

