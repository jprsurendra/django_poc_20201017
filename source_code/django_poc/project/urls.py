"""project URL Configuration

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
from django.conf.urls import url, include

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', include(('web.books_app.urls', 'books_web_app'), namespace='books_web_app')),

    url(r'^authorsapi/', include(('apis.authors.urls', 'authors'), namespace='authors_apis')),
    url(r'^bookapi/', include(('apis.books.urls', 'books_app'), namespace='books_apis')),
]
