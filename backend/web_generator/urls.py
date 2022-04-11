from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api/web_generator', views.UserUploadViewSet, 'web-generator')

# urlpatterns = [
#     path('web_generator/', views.UserUploadViewSet.as_view({'get': 'retrieve', 'post': 'create'})),
# ]
urlpatterns = router.urls
