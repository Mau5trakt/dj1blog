from django.urls import path
from . import views

app_name = 'blog' #Allowing

urlpatterns = [
    #post views

    #functions from views
    #path('', views.post_list, name='post_list'),
    path('', views.PostListView.as_view(), name='post-list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),
]