from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import User
from .utils import generate_otp

# Create your views here.
def Home(request):
    return render(request,'main/index.html')

def Products(request):
    return render(request,'main/products.html')

def About(request):
    return render(request,'main/about.html')

def Contact(request):
    return render(request,'main/contact.html')


# register view

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(email = email).exists():
            messages.error(request,"Email already registered.!!")
            return redirect('register')

        otp = generate_otp()

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password
        )

        user.first_name = name
        user.otp = otp
        user.is_active = False
        user.save()

        send_mail(
            "ApanBazaar OTP Verification",
            f"Your OTP is {otp}",
            None,
            [email]
        )

        request.session['email'] = email
        return redirect('verify_otp')
    
    return render(request,'main/register.html')

def verify_otp(request):
    if request.method == 'POST':
        otp = request.POST['otp']
        email = request.session.get('email')

        user = User.objects.get(email=email)

        if user.otp == otp:
            user.is_verified = True
            user.is_active = True
            user.otp = ''
            user.save()
            messages.success(request,'Account verified successfully.!')
            return redirect('Home')
        else:
            messages.error(request, "Invalid OTP")

    return render(request,'main/verify_otp.html')
