from django.conf.urls import url
from . import views

expatterns = [

]

urlpatterns = [
    url(r"prices/(\w+)/$", views.gen_price),
    url(r'^$', views.index),
]
