from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:pk>/',views.DetailCarView.as_view(),name='detail_car')
]
