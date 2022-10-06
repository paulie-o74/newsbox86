from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('add/', views.add_post, name='add_post'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('edit/<slug:slug>/', views.edit_post, name='edit_post'),
    path('delete/<slug:slug>/', views.delete_post, name='delete_post'),
    path('<int:pk>/delete_comment',
         views.delete_comment, name='delete_comment'),
    path('category/<category>/', views.CatListView.as_view(), name='category'),
]
