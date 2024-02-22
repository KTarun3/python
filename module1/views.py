import string
import random
from .forms import *
from django.http import HttpResponse
from django.shortcuts import render


def travelpackage(request):
    return render(request, 'travelpackage.html')


def hello3(request):
    return render(request, 'hello.html')


def hello(request):
    return HttpResponse(" <center style=color:blue;>  Welcome to TTM homepage </center>")


def print1(request):
    return render(request, 'print_to_console.html')


def print_to_console(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        print(f'user input:{user_input}')
    bc = {'user_input': user_input}
    return render(request, 'print_to_console', bc)


def homepage(request):
    return render(request, 'homepage.html')


def random123(request):
    ran = ''.join(random.sample(string.digits, k=10))
    print(ran)
    a2 = {'ran': ran}
    return render(request, 'random123.html', a2)


def datetime1(request):
    return render(request, 'datetime.html')


import datetime
from django.shortcuts import render


def get_date(request, integer_value=None):
    if request.method == 'post':
        form = IntegerDateForm(request.POST)
        if form.is_valid():
            Integer_value = form.cleaned_data['integer_value']
            date_value = form.cleaned_data['date_value']
            updated_date = date_value + datetime.timedelta(days=integer_value)
            return render(request, 'datetime.html', {'updated_date': updated_date})
        else:
            form = IntegerDateForm()
        return render(request, 'datetime.html', {'form': form})


def pagecall(request):
    return render(request, 'register.html')


def tz(request):
    return render(request, 'pytzexample.html')


from .models import *
from django.shortcuts import render, redirect


def pagecall(request):
    return render(request, 'register1.html')


from .models import *
from django.shortcuts import render, redirect


def register_function(request):
    if request.method == ' POST ':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phonenumber = request.POST.get('phonenumber')
        if Register.objects.filter(email=email).exists():
            message1 = "email already registered"
            return render(request, 'register1.html', {'message1': message1})
        Register.objects.create(name=name, email=email, password=password, phonenumber=phonenumber)
        return redirect('newhomepage')
    return render(request, 'register1.html')


import matplotlib.pyplot as plt
import numpy as np


def pie_chart(request):
    if request.method == 'POST':
        form = PieChartForm(request.POST)
        if form.is_valid():
            # Process user input
            y_values = [int(val) for val in form.cleaned_data['y_values'].split(',')]
            labels = [label.strip() for label in form.cleaned_data['labels'].split(',')]

            # Create pie chart
            plt.pie(y_values, labels=labels, startangle=90)
            plt.savefig('static/images/pie_chart.png')  # Save the chart image
            img1 = {'chart_image': '/static/images/pie_chart.png'}
            return render(request, 'chart_form.html', img1)
    else:
        form = PieChartForm()
    return render(request, 'chart_form.html', {'form': form})


def slides(request):
    return render(request, 'slide.html')


def weather1(request):
    return render(request, 'weather.html')


def weatherlogic(request):
    if request.method == 'POST':
        place = request.POST['place']
        API_KEY = '7dea4ba5d142fbb7cfa25ba4468f366a'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperature1 = round(temperature - 273.15, 2)
            return render(request, 'weather.html',
                          {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
        else:
            error_message = 'City not found. Please try again.'
            return render(request, 'weather.html', {'error_message': error_message})


from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        user = auth.authenticate(username=username, password=pass1)
        if user is not None:
            auth.login(request, user)
            return render(request, 'homepage.html')
        else:
            messages.info(request, 'invalid credentials')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def signup1(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['password']
        pass2 = request.POST['password']
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'oops! username already taken')
                return render(request, 'signup.html')
            else:
                user = User.objects.create_user(username=username, password=pass1)
                user.save()
                messages.info(request, 'Account created successfully')
                return render(request, 'login.html')

    else:
        messages.info(request, 'password do not match')
        return render(request, 'signup.html')


def logout(request):
    auth.logout(request)
    return render(request, 'homepage.html')
