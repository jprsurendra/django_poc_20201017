from django.shortcuts import redirect
from django.views.generic import TemplateView


class BooksListTemplateView(TemplateView):
    template_name = 'books/book_list.html'

    def dispatch(self, *args, **kwargs):
        return super(BooksListTemplateView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BooksListTemplateView, self).get_context_data(**kwargs)
        # context['data'] = data
        return context

    def post(self, request, *args, **kwargs):
        book_id = request.POST.get('book_id')
        return redirect('/customer-care/calendar/' + book_id)

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
