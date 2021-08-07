from unicodedata import name
from django.urls import URLPattern
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("hello",views.hello,name="hello"),
    path("headings",views.headings,name="headings"),
    path("lists",views.lists,name="lists"),
    path("image",views.image,name="image"),
    path("link",views.link,name="link"),
    path("table",views.table,name="table"),
    path("form",views.form,name="form"),
    path("style",views.style,name="style"),



# Give url 'alper' , give run function 'alper function insice views ' and a name 

]
