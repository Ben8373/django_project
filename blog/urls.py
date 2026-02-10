from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    

]