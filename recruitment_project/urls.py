"""recruitment_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from library.views import BookListView, BookAddView, BookEditView, GoogleImportView, BookDeleteView, BookAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BookListView.as_view(), name='list'),
    path('book/add', BookAddView.as_view(), name='add'),
    path('book/edit/<int:pk>', BookEditView.as_view(), name='edit'),
    path('import/', GoogleImportView.as_view(), name='import'),
    path('book/delete/<int:pk>', BookDeleteView.as_view(), name='delete'),
    path('book/api/', BookAPIView.as_view(), name='api'),
]
