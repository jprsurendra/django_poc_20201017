from django.shortcuts import redirect
from web.common_app.custom_views import WebTemplateView


class BooksListTemplateView(WebTemplateView):
    template_name = 'books/book_list.html'

    def dispatch(self, *args, **kwargs):
        return super(BooksListTemplateView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BooksListTemplateView, self).get_context_data(**kwargs)

        # author_name_list_api = self.fetch_api_data(api_url = '/bookapi/author-name-list/')
        # context['author_names'] = author_name_list_api #.get('data').get('results')
        context['author_names'] = []

        return context

    # def post(self, request, *args, **kwargs):
    #     book_id = request.POST.get('book_id')
    #     return redirect('/customer-care/calendar/' + book_id)

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

class BookTemplateView(WebTemplateView):
    template_name = 'books/book_entry.html'