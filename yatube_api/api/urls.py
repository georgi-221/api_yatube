from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import SimpleRouter
from .views import CommentViewSet, GroupViewSet, PostViewSet

router = SimpleRouter()

router.register('groups', GroupViewSet, basename='groups')
router.register('posts', PostViewSet, basename='posts')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    # API v1 endpoints
    path('v1/', include(router.urls)),

    # Authentication endpoint
    path('v1/api-token-auth/', obtain_auth_token, name='api_token_auth')
]