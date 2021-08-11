from django.urls import path
from . import views

app_name = 'lecture3'
urlpatterns = [
    path("",views.index,name="index"),
    path("hello/<str:name>",views.greet,name="greet"),
    # path("alper",views.alper,name="alper"),
    # path("david",views.david,name="david"),
    path("newyear",views.newyear,name="newyear"),
    path("tasks",views.tasks,name="tasks"),
    path("add",views.add,name="add"),
    path("base",views.base,name="base"),
    path("sum",views.sumO,name="sum"),
    path("statistics",views.stats_,name="statistics"),
]