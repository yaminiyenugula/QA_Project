from django.urls import path,include
from rest_framework.routers import DefaultRouter

from QA_APP.views import QuestionViewSet

router = DefaultRouter()
router.register(r'questions',QuestionViewSet , basename = "questions")
urlpatterns = [
    #  path('api/', include(router.urls))
]
urlpatterns = router.urls
