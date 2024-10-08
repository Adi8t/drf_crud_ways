"""
URL configuration for kins project.

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
from django.urls import path,include
from app_decor import views 
from api_view import views as way3
from model_api import views as way4 
from rest_framework.routers import DefaultRouter
from concrete_views import views as way5
from mixins import views as way6

router = DefaultRouter()
router.register('studentdata',way4.Studentmodelviewset , basename="studentdata")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.studentapi),
    path('api/<int:pk>/', views.studentapi),
    path('way3/', way3.StudentAPI.as_view()),
    path('way3/<int:pk>/', way3.StudentAPI.as_view()),
    path('way5/',way5.Studentlisting.as_view()),
    path('way5/<int:pk>/',way5.Studentedit.as_view()),
    path('way6/',way6.ListStudentapi.as_view()),
    path('way6/<int:pk>/',way6.REadupdateview.as_view()),
    path('', include(router.urls)),
]
