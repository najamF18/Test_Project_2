from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .views import RegisterUserView, LoginView, LogoutView, ChangePasswordView, ListLoggedInUser
from django.conf.urls.static import static
from rest_framework.authtoken import views

urlpatterns = [
    path('LoginApp/register', RegisterUserView.as_view(), name='register_user'),
    path('LoginApp/login', LoginView.as_view(), name='login_view'),
    path('LoginApp/logout-view', LogoutView.as_view(), name='logout_view'),
    path('LoginApp/change-password-view', ChangePasswordView.as_view(), name='change_password'),
    path('LoginApp/profile/', ListLoggedInUser.as_view(), name='logged_in_user_data'),
    path('LoginApp/api-token-auth/', views.obtain_auth_token)
    # path('/api/users/search/<str:email>', ListLoggedInUser.as_view(), name='logged_in_user_data'),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)