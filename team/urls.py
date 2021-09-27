from django.conf.urls import url
from team import views

urlpatterns = [
    url('get_employees/', views.get_employees),
    ]
