from django.urls import path
from .views import UGCPostListCreateView, UGCPostDetailView, LocationListCreateView


urlpatterns = [
    path('posts/', UGCPostListCreateView.as_view(), name='ugc-post-list-create'),
    path('detail/<int:pk>/', UGCPostDetailView.as_view(), name='ugc-post-detail'),
    path('locals/', LocationListCreateView.as_view(), name='locals-post-list-create'),
    # 添加其他API端点
]