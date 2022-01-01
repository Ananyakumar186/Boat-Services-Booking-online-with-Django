from django.shortcuts import render,redirect,HttpResponse
from .forms import ContactForm,UserRegisterForm ,BookingForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse 
from django.contrib.auth import authenticate, login, logout
from boat.models import Booking
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
#from django.views.generic import DeleteView#, UpdateView
#from django.urls import reverse_lazy
# Create your views here.
def boatservices(request):
    return render(request, 'services.html')

def navbar(request):
    return render(request, 'navbar.html')

def about(request):
    return render(request, 'about.html')

def speed(request):
    return render(request, 'speed_boat.html')

def sailB(request):
    return render(request, 'sail_boat.html')

def motoryachts(request):
    return render(request, 'motor.html')
def sailY(request):
    return render(request, 'sail.html')

def cabinY(request):
    return render(request, 'cabinY.html')


#create a new view for  contact page where it takes the name, email and message from the user and sends it to the appropriate email of the admin by clicking the submit button
'''
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'Website Inquiry'
            message = '\n'.join(['Name: ' + form.cleaned_data['name'],
                                 'Email: ' + form.cleaned_data['email'],
                                 'Message: ' + form.cleaned_data['message']
                                 ])
            try:
                send_mail(subject, message, 'admin@example.com',[from_email=form.cleaned_data['from_email']])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, 'contact.html')
    form = ContactForm()
    return render(request, 'contact.html', {'form': form})
'''

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'admin@example.com',['admin@example.com'])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return render(request,"contact.html")
    form = ContactForm()
    return render(request,"contact.html",{'form':form})

#create a view for user registration by name,email,password,phoneno and storing them in the database and redirecting to the login page after registration is successful and redirecting to the registration page if registration is unsuccessful.
def register(request):
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            login(request, user)
            return redirect('/services/?submitted=True')
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
            
            return render(request = request,
                          template_name = 'registration/register.html',
                          context={"form":form})
    form = UserRegisterForm
    return render(request = request,
                    template_name = 'registration/register.html',
                    context={"form":form})

#create a view for user login by username and password and redirecting to the home page if login is successful and redirecting to the login page if login is unsuccessful. 
def login_view(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/services/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = 'registration/login.html',
                    context={"form":form})

#create a view for user logout by redirecting to the login page after logout is successful.
def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('/services/')

#create a view for boat booking which takes the modelform of boat booking and stores the data in the database and redirecting to the order listing page after booking is successful.

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            book=form.save(commit=False)
            book.name = request.user.username
            book.email = request.user.email
            book.save()
            return redirect('/order/?submitted=True')
        else:
            return render(request,'booking.html', {'form': form})
    else:
        form = BookingForm()
        return render(request,'booking.html', {'form': form})
     

def orderlisting(request):
    #code to send authhenticated user's order list to the order listing page
    if request.user.is_authenticated:
        order_list = Booking.objects.filter(name=request.user.username)
        return render(request,'order_listing.html',{'order_list': order_list})
    else:
        return redirect('/login/')
    
#create a view for deleting order by id and redirecting to the order listing page after deletion is successful.
'''
def delete_order(request, pk):
    order = get_object_or_404(Booking, pk=pk)
    order.delete()
    return redirect('/orderlisting/')
'''
    
def delete_order(request,id):
    order = Booking.objects.get(id=id)
    order.delete()
    return redirect('/order/')

def update_order(request,id):
    order = Booking.objects.get(id=id)
    form = BookingForm(request.POST or None, instance=order)
    if form.is_valid():
        form.save()
        return redirect('/order/')
    return render(request,'booking.html',{'form': form})

