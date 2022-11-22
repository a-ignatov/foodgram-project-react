from django.views.generic.base import TemplateView
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import IngredientsViewSet, RecipesViewSet, TagsViewSet

app_name = 'api'

router = DefaultRouter()

router.register('recipes', RecipesViewSet)
router.register('tags', TagsViewSet)
router.register('ingredients', IngredientsViewSet)

urlpatterns = [
    path('docs/', TemplateView.as_view(template_name='docs/redoc.html')),
    path('', include(router.urls)),
    path('', include('users.urls')),
]
