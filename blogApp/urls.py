from . import views
from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
# basic URL Configurations
from django.urls import include, path
# import routers
from rest_framework import routers

from . import views



urlpatterns = [
    path('redirect-admin', RedirectView.as_view(url="/admin"),name="redirect-admin"),
    path('', views.home, name="home-page"),
    path('login',auth_views.LoginView.as_view(template_name="login.html",redirect_authenticated_user = True),name='login'),
    path('userlogin', views.login_user, name="login-user"),
    path('user-register', views.registerUser, name="register-user"),
    path('logout',views.logoutuser,name='logout'),
    path('profile',views.profile,name='profile'),
    path('update-profile',views.update_profile,name='update-profile'),
    path('update-avatar',views.update_avatar,name='update-avatar'),
    path('category_mgt',views.category_mgt,name='category-mgt'),
    path('manage_category',views.manage_category,name='manage-category'),
    path(r'manage_category/<int:pk>',views.manage_category,name='edit-category'),
    path('save_category',views.save_category,name='save-category'),
    path('delete_category',views.delete_category,name='delete-category'),
    path('post_mgt',views.post_mgt,name='post-mgt'),
    path('manage_post',views.manage_post,name='manage-post'),
    path(r'manage_post/<int:pk>',views.manage_post,name='edit-post'),
    path('save_post',views.save_post,name='save-post'),
    path('delete_post',views.delete_post,name='delete-post'),
    path(r'view_post/<int:pk>',views.view_post,name='view-post'),
    path(r'<int:pk>',views.post_by_category,name='category-post'),
    path('categories',views.categories,name='category-page'),
    path('search-blogs/', views.BlogSearchView.as_view(), name='search_blogs'),
    path('categorylist/<int:pk>/',views.CategoryList.as_view(),),
    path('categorydetail/<int:pk>/', views.CategoryDetail.as_view()),
    path('updatecategory/<int:pk>/',views.UpdateCategory.as_view()),
    path('postdetail/<int:pk>/', views.Postdetail.as_view()),
    path('updatepost/<int:pk>/', views.Updatepost.as_view()),
    #path('createprofile/', views.Createuser.as_view()),
    path('search/', views.PostSearchAPIView.as_view(), name='post-search'),
    path('tags/', views.TagListCreateAPIView.as_view(), name='tag-list'),
    path('tags/<int:pk>/', views.TagDetailAPIView.as_view(), name='tag-detail'),
    path('profiles/<int:pk>/', views.UserProfileDetailAPIView.as_view(), name='user-profile-detail'),
    path('profiles/', views.UserProfileListCreateAPIView.as_view(), name='user-profile-list'),
    # path('create-user-profile/', CreateUserProfileView.as_view(), name='create-user-profile'),

 ]
