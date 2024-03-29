from django.urls import path
from . import views
from neighb import views as user_views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('update_profile/', user_views.update_profile, name='update_profile'),
    path('new_hood/', views.new_hood, name='new_hood'),
    path('hood/', views.hood, name='hood'),
    path('edithood/', views.edit_hood, name='edithood'),
    path('businesses/<id>', views.businesses, name='hoodbusiness'),
    path('singlehood/<id>', views.singlehood, name='singlehood'),
    path('new_business/', views.newbiz, name='newbiz'),
    path('post', views.post, name='post'),
    path('hoodpost/<id>', views.posthood, name='hoodpost'),
    path('joinhood/<id>', views.joinhood, name='joinhood'),
    path('leavehood/<id>', views.leavehood, name='leavehood'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)