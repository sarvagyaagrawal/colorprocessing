
from django.urls import path

from . import views


urlpatterns = [
        path('',views.get_data ),
        path('src<src1>/',views.get_data)

]