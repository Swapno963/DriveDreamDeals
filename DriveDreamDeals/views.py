from django.shortcuts import render
from car.models import CarModel
from categories.models import CategoryModel

def home(request, category_slug = None):
    data = CarModel.objects.all()
    if category_slug is not None:
        category = CategoryModel.objects.get(slug = category_slug)
        data = CarModel.objects.filter(category = category)

    category = CategoryModel.objects.all()
    return render(request,'home.html',{'data':data, 'category':category})