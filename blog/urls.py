from django.urls import path
from . import views

app_name = 'blog' #Allowing

urlpatterns = [
    #post views

    #functions from views
    path('', views.post_list, name='post_list'),
    path('<int:id>/', views.post_detail, name='post_detail')
]