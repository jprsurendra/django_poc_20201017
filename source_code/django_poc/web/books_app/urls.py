from django.conf.urls import url

from web.books_app import views

urlpatterns = [
    url(r'^$', views.BooksListTemplateView.as_view(), name='book_dashboard'),
    url(r'^book-list/$', views.BooksListTemplateView.as_view(), name='book_list'),
    url(r'^book-new/$', views.BookTemplateView.as_view(), name='book_new'),
    url(r'^book-edit/(?P<pk>\d{0,50})/$', views.edit_book, name='book_view'),


]
app_name = 'books_web_app'