from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r"comments", views.CommentViewSet)
router.register(r"developers", views.DeveloperViewSet)
router.register(r"games", views.GameViewSet)
router.register(r"genres", views.GenreViewSet)
router.register(r"platforms", views.PlatformViewSet)
router.register(r"ratings", views.RatingViewSet)
