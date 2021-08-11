from django.urls import path
from . import views

app_name ='lecture1'
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
    path("size",views.size,name="size"),
    path("font",views.font,name="font"),
    path("descedant",views.descedant,name="descedant"),
    path("attribute",views.attribute,name="attribute"),
    path("hover",views.hover,name="hover"),
    path("responsive",views.responsive,name="responsive"),
    path("flexbox",views.flexbox,name="flexbox"),
    path("grid",views.grid,name="grid"),
    path("bootstrap",views.bootstrap,name="bootstrap"),
    



# Give url 'alper' , give run function 'alper function insice views ' and a name 

]
