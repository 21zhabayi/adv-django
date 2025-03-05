"""
URL configuration for cv_task project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from app.views import share_cv_email 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', views.contact_view, name='contact'),
    path('share/email/<int:cv_id>/', share_cv_email, name='share_cv_email'),
    path('cv/', views.create_cv, name='cv'),
    path('allcv/', views.cv_list, name='cv_list'),
    path('success/', views.success, name = 'success')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
