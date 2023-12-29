from django.shortcuts import render
from django.views.generic import DetailView
from . import models
from . import forms

from django.contrib import messages
# Create your views here.
class DetailCarView(DetailView):
    model = models.CarModel
    template_name = 'car_detail.html'
    context_object_name ='car'
    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(self.request.POST)
        car = self.get_object()
        # FOR Buy now
        if 'buy_car' in request.POST:
            if car.quantity > 0:
                car.quantity -=1
                car.save()
                # models.BuyCar.objects.create(user=request.user, car=car)
            else:
                messages.warning(self.request, 'All Car is Sold out please look forward')
            return self.get(request, *args,**kwargs)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
        return self.get(request, *args, **kwargs)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        comments = car.comments.all()
        # print(car)
        comment_form = forms.CommentForm()

        context['comments'] = comments
        context['comment_form'] = comment_form

        return context
        


# class DetailsPost(DetailView):
#     model = models.AddCar
#     pk_url_kwarg = 'id'
#     template_name = 'carDetails.html'
#     def post(self,request,*args,**kwargs):
#         comment_form = forms.CommentForm(data = self.request.POST)
#         post = self.get_object()
#         if comment_form.is_valid():
#             new_comment = comment_form.save(commit = False)
#             new_comment.post = post 
#             new_comment.save()
#         if 'buy_car' in request.POST:
#             if post.quantity > 0:
#                 post.quantity -=1
#                 post.save()
#                 models.BuyCar.objects.create(user=request.user, car=post)
#             else:
#                 messages.warning(self.request, 'All Car is Sold out please look forward')
#         return self.get(request, *args,**kwargs)
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         post = self.object
#         comments = post.comments.all()
#         comment_form = forms.CommentForm()
        
#         context['comments'] = comments
#         context['comment_form'] = comment_form
#         return context