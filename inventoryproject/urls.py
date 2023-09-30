from django.contrib import admin
from django.urls import path, include
from user import views as user_view
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('register/', user_view.register, name='user-register'),
    path('profile/', user_view.profile, name='user-profile'),
    path('profile/update/', user_view.profile_update, name='user-profile-update'),
    path('', auth_views.LoginView.as_view(template_name='user/login.html'), name='user-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='user-logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


