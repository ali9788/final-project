from django.shortcuts import render
from .models import Car, Service, Slide, AzService, RuService
from .forms import *
from django.shortcuts import redirect

def home(request):
    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            order = form.save()
            order.save()
            return redirect('base:Cars')
    else:
        cars = Car.objects.order_by('-id')
        services = Service.objects.order_by('-id')
        slides = Slide.objects.order_by('-id')[0:]
        print(slides)
        first_slide = Slide.objects.all()[0]
        context = {'cars' : cars, 'services': services, 'slides': slides, 'first_slide': first_slide, 'form': ContactForm()}
    return render(request, 'Car.html', context)

def AZhome(request):
    if request.method == 'POST':
        form=AzContactForm(request.POST)
        if form.is_valid():
            order = form.save()
            order.save()
            return redirect('base:Cars')  
    else:      
        cars = Car.objects.order_by('-id')
        services = AzService.objects.order_by('-id')
        slides = Slide.objects.order_by('-id')[0:]
        print(slides)
        first_slide = Slide.objects.all()[0]
    return render(request, 'AzCar.html', {'cars' : cars, 'services': services, 'slides': slides, 'first_slide': first_slide, 'form': AzContactForm})

def RUhome(request):
    if request.method == 'POST':
        form=AzContactForm(request.POST)
        if form.is_valid():
            order = form.save()
            order.save()
            return redirect('base:Cars')
    else: 
        cars = Car.objects.order_by('-id')
        services = RuService.objects.order_by('-id')
        slides = Slide.objects.order_by('-id')[0:]
        print(slides)
        first_slide = Slide.objects.all()[0]
    return render(request, 'RuCars.html', {'cars' : cars, 'services': services, 'slides': slides, 'first_slide': first_slide, 'form': RuContactForm})