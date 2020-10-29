from django.urls import path, include

from .views import HomeView, CreatePostView, PostDetailView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='detail-view'),
    path('add-post/<int:pk>', CreatePostView.as_view(), name='add-post'),
]
