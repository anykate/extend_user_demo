from django.urls import path
from . import views


app_name = 'app'


urlpatterns = [
    path('', views.index, name='index'),
    path('save/', views.add_update, name='add'),
    path('save/<int:emp_id>/', views.add_update, name='update'),
]
