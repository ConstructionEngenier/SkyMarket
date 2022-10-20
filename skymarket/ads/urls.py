from django.urls import include, path
from rest_framework_nested import routers

from ads.views import AdViewSet, CommentViewSet

# urlpatterns = [
#     path('', views.AdViewSet.as_view({
#         'get': 'list',
#         'post': 'create',
#     })),
#
#     path('me/', views.AdViewSet.as_view({'get': 'me'})),
#     path('<int:pk>/', views.AdViewSet.as_view({
#         'get': 'retrieve',
#         'patch': 'partial_update',
#         'delete': 'destroy'
#     })),
#
#     path('<int:ad>/comments/', views.CommentViewSet.as_view({
#         'get': 'list',
#         'post': 'create'
#     })),
#
#     path('<int:ad>/comments/<int:id>/', views.CommentViewSet.as_view({
#         'get': 'retrieve',
#         'patch': 'partial_update',
#         'delete': 'destroy'
#     })),
# ]


ads_router = routers.SimpleRouter()
ads_router.register(r"ads", AdViewSet)

ads_router.register("ads", AdViewSet, basename="users")
comment_router = routers.NestedSimpleRouter(ads_router, r"ads", lookup="ad")
comment_router.register(r"comments", CommentViewSet, basename="comments")

urlpatterns = [
    path("", include(ads_router.urls)),
    path("", include(comment_router.urls)),
]
