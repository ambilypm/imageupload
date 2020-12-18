from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ProductForm
from .models import Product


def index(request):
    product = Product.objects.all()
    return render(request, 'index.html', {'product': product})


def upload_image(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(index))
    else:
        form = ProductForm()
    return render(request, 'upload.html', {'form': form})


def sort_watches(request):
    product = Product.objects.all().filter(category='Watches')
    return render(request, 'sort_watches.html', {'product': product})


def sort_tshirts(request):
    product = Product.objects.all().filter(category='Tshirts')
    return render(request, 'sort_tshirts.html', {'product': product})