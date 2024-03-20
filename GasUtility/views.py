from django.shortcuts import render
from customer_service.models import WebCustomersData,ServiceRequestData
from datetime import date
# from django.contrib.auth import authenticate

def homepage (request):
    return render(request, 'index.html')

def login (request):
     if request.method == 'POST':
            email = request.POST.get('username')
            password = request.POST.get('password')
            if WebCustomersData.objects.filter(user_email = email).exists():
                if WebCustomersData.objects.filter(user_pass = password).exists():
                    bill = WebCustomersData.objects.filter(user_email= email)
                    k_number = request.session['bill'] = email
                    return  render(request, 'sucess.html',{'user': k_number})
                    
     else:
         return render(request, 'login.html', {'error': True })
     return render(request, 'login.html')

def logout(request):
    request.session.clear()
    data = {'info': "You have Successfully Logged Out"}
    return render(request, 'sucess.html', data)

def signup (request):
    return render(request, 'signup.html')

def profile(request):
    if request.session.get('bill') is not None:
        id = request.session.get('bill')
        s_data = ServiceRequestData.objects.all()
        w_data = WebCustomersData.objects.filter(user_email = id)
        context = {'s_data': s_data, 'w_data': w_data}
        return render(request, 'profile.html', context)
    else:
        return render(request, 'login.html')

def newuser(request):
    if request.method=="POST":
        name=request.POST.get('name') 
        email=request.POST.get('email')       
        k_number=request.POST.get('k_number')
        address=request.POST.get('address')
        mobile_number=request.POST.get('mobile_number')
        password=request.POST.get('password')
        en=WebCustomersData(bill_number=k_number,user_name=name,user_address=address,user_number=mobile_number,user_email=email,user_pass=password)
        en.save()
        data={'info': "You have succefully Signed-up"}
    return render(request, 'sucess.html',data )

def request(request):
    return render(request, 'request.html')

def newrequest(request):
    if request.method=="POST":
        k_number=request.POST.get('k_number')
        name= request.POST.get('name')
        address= request.POST.get('address')
        mobile_number= request.POST.get('mobile_number')
        request_description= request.POST.get('request_description')
        current_date= date.today()
        en=ServiceRequestData(bill_number=k_number,user_name=name,user_address=address,user_number=mobile_number,req_date=current_date,req_description=request_description)
        en.save()
        data=data={'info': "You have successfully raised the service request"}
    return render(request,'sucess.html',data)