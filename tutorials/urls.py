from django.urls import path
from . import views
# from blog import urls

urlpatterns = [
    path('', views.PostList.as_view(), name='tutorials'),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/', views.post_detail, name='tuts_details'),
]
