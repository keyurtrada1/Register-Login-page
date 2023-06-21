from django.shortcuts import render
from .models import registertable
from django.contrib import messages

def registerpage(request):
    return render(request, 'register.html')

def fetchregdata(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        uemail = request.POST.get("useremail")
        uphone = request.POST.get("userphone")
        upass = request.POST.get("userpass")


        if uname=="" or uemail=="" or uphone=="" or upass=="":
            messages.error(request,'FIELDS MUST BE FILLED')
        else:
            insertdata = registertable(name=uname, email=uemail, phone=uphone, password=upass)
            insertdata.save()
            messages.success(request, "SUCCESSFULLY REGISTERED")
    else:
        messages.error(request, "ERROR OCCURED")

    return render(request, 'register.html')

def loginpage(request):
    return render(request, 'login.html')

def fetchlogindata(request):
    if request.method =="POST":
        uemail = request.POST.get("useremail")
        upass = request.POST.get("userpass")

        try:
            userdetails = registertable.objects.get(email=uemail,password=upass)
            request.session['logid'] = userdetails.id
            request.session['logname'] = userdetails.name
            request.session.save()
        except:
            userdetails = None

        if userdetails is not None:
            return render(request,'dashboard.html')
        else:
            messages.error(request,"incorrect username or password")

    else:
        pass

    return render(request,'login.html')

def dashboardpage(request):
    return render(request,'dashboard.html')

def logout(request):
    try:
        del request.session['logid']
        del request.session['logname']
    except:
        pass

    return render(request,'login.html')