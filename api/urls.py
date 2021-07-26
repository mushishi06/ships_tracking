from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'ships', views.ShipViewSet)
router.register(r'positions', views.PositionViewSet)


urlpatterns = [
    path('', include(router.urls)),
    # path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
]