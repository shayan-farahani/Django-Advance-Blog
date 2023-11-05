
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.PostList.as_view(), name='index'),
    path('<int:pk>/', views.PostDetail.as_view(), name='detail'),
    path('created/', views.PostCreatedView.as_view(), name='created_post'),
    path('edit/post/<int:pk>', views.PostEditView.as_view(), name='edit'),
    path('delete/post/<int:pk>', views.PostDeleteView.as_view(), name='delete'),
     path('api/v1/', include('blog.api.v1.urls')),

] 