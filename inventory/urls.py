from rest_framework.routers import DefaultRouter

from .views import ScreenViewSet


router = DefaultRouter()
router.register(r'screens', ScreenViewSet, basename='screen')
urlpatterns = router.urls
