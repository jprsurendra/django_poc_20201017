from django.conf.urls import url

from web.books import views

urlpatterns = [
    url(r'^$', views.BooksListTemplateView.as_view(), name='book_dashboard'),
    url(r'^book-list/$', views.BooksListTemplateView.as_view(), name='book_list'),

]
app_name = 'books'