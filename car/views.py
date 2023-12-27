from django.shortcuts import render
from django.views.generic import DetailView
from . import models
from . import forms
# Create your views here.
class DetailCarView(DetailView):
    model = models.CarModel
    template_name = 'car_detail.html'
    context_object_name ='car'
    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(self.request.POST)
        car = self.get_object()
        if comment_form.i_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = car
            new_comment.save()
        return self.get(request, *args, **kwargs)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        comments = car.comments.all()
        print(car)
        comment_form = forms.CommentForm()

        context['comments'] = comments
        context['cmment_form'] = comment_form

        return context
        
