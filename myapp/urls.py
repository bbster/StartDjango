from rest_framework.routers import DefaultRouter
from myapp.views import BookViewSet

router = DefaultRouter()
router.register('book', BookViewSet, basename='book')
urlpatterns = router.urls
