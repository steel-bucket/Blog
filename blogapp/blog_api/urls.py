from .views import PostList
from rest_framework.routers import DefaultRouter

app_name = 'blog_api'

router = DefaultRouter()
router.register('', PostList, basename='post')
urlpatterns = router.urls




















# from django.urls import path
# from .views import PostList
#
# app_name = 'blog_api'
#
# urlpatterns = [
#     path('<int:pk>/', PostList.as_view({'get': 'list'}), name='detail_create'),
#     path('', PostList.as_view({'get': 'retrieve'}), name='list_create'),
# ]
