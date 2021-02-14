from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet, CommentView, GenreViewSet, ReviewView,
                    TitleViewSet, UserViewSet, obtain_auth_token,
                    obtain_confirmation_code)

router_v1 = DefaultRouter()
router_v1.register('users', UserViewSet)
router_v1.register('titles', TitleViewSet, basename='titles')
router_v1.register('genres', GenreViewSet, basename='genres')
router_v1.register('categories', CategoryViewSet, basename='categories')
router_v1.register(r'titles/(?P<title_id>\d+)/reviews', ReviewView, basename='reviews')
router_v1.register(r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments', CommentView, basename='comments')

auth_urls = [
    path('email/', obtain_confirmation_code, name='confirmation_code_obtain'),
    path('token/', obtain_auth_token, name='token_obtain')
]

urlpatterns = [
    path('v1/auth/', include(auth_urls)),
    path('v1/', include(router_v1.urls)),
]
