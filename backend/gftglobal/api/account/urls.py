from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from api.account.views import TokenObtainPairWithUsernameView
from api.account.views import UserLogin, UserLogout, UserSession

urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('validate/', UserSession.as_view(), name='validate'),

    path("token/", TokenObtainPairWithUsernameView.as_view(), name="obtain_token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="refresh_token"),
]
