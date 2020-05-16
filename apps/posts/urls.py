from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/delete/<int:pk>', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/update/<int:pk>', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>',views.PostDetailView.as_view(), name='post_detail')
]
