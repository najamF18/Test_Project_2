from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .views import RegisterUserView, LoginView, LogoutView, ChangePasswordView, RequestChangePasswordView, ListLoggedInUser
from django.conf.urls.static import static

urlpatterns = [
    path('api/users/register', RegisterUserView.as_view(), name='register_user'),
    path('api/users/login', LoginView.as_view(), name='login_view'),
    path('logout-view', LogoutView.as_view(), name='logout_view'),
    path('change-password-view/<str:email>', ChangePasswordView.as_view(), name='change_password'),
    path('api/users/reset-password', RequestChangePasswordView.as_view(), name='request_change_password'),
    path('api/users/profile/', ListLoggedInUser.as_view(), name='logged_in_user_data'),
    # path('/api/users/search/<str:email>', ListLoggedInUser.as_view(), name='logged_in_user_data'),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)