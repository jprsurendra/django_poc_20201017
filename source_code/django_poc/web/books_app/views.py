import random
import json
import requests

from django.shortcuts import redirect

# from apis.authors.tasks import demo_task
from web.common_app.custom_views import WebTemplateView

BASE_URL =  'http://localhost:8000'

class BooksListTemplateView(WebTemplateView):
    template_name = 'books/book_list.html'
    last_value = 1

    # def new_number(self):
    #     num = BooksListTemplateView.last_value
    #     print("Last Number:", num)
    #     res = demo_task.delay(num)
    #     print(type(res))
    #     # print(f"id={res.id}, state={res.state}, status={res.status} ")
    #
    #     # print(res.get())
    #     # x = random.randint(1,9)
    #     # BooksListTemplateView.last_value += x
    #     # print("New Number ref: ", x)


    def dispatch(self, *args, **kwargs):
        return super(BooksListTemplateView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BooksListTemplateView, self).get_context_data(**kwargs)

        # author_name_list_api = self.fetch_api_data(api_url = '/bookapi/author-name-list/')
        # context['author_names'] = author_name_list_api #.get('data').get('results')
        context['author_names'] = []

        # self.new_number()

        return context

    # def post(self, request, *args, **kwargs):
    #     book_id = request.POST.get('book_id')
    #     return redirect('/customer-care/calendar/' + book_id)

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

class BookTemplateView(WebTemplateView):
    template_name = 'books/book_entry.html'

    def call_api(self, url):
        resp = requests.get(BASE_URL + url, cookies=self.request.COOKIES)
        json_data = json.loads(resp.content)
        return json_data

    def dispatch(self, *args, **kwargs):
        return super(BookTemplateView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BookTemplateView, self).get_context_data(**kwargs)
        try:
            context['authors_list'] = self.call_api(url='/authorsapi/common_operations/')
            context['categories_list'] = self.call_api(url='/categoryapi/common_operations/')
            publishers_name_list = []
            publishers_list = self.call_api(url='/publisherapi/publisher-name-list/')
            for item in publishers_list:
                publishers_name_list.append(item['publisher_name'])
            context['publishers_name_list'] = publishers_name_list

            return context
        except Exception as e:
            return context

    def post(self, request, *args, **kwargs):
        params = request.POST
        print("params: ", params)

    # def post(self, request, *args, **kwargs):
    #     user_id = request.POST.get('user_id')
    #     return redirect('/customer-care/calendar/' + user_id)



