import random
import json
import requests
from django.http import HttpResponse

from django.shortcuts import redirect

from django.template import RequestContext, loader, Template, Context
# from apis.authors.tasks import demo_task
from web.common_app.custom_views import WebTemplateView

BASE_URL =  'http://localhost:8000'


def call_api(request, url):
    resp = requests.get(BASE_URL + url, request.COOKIES)
    json_data = json.loads(resp.content)
    return json_data


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
        context['books_list'] = call_api(self.request, url='/bookapi/common_operations/')
        return self.render_to_response(context)

class BookTemplateView(WebTemplateView):
    template_name = 'books/book_entry.html'

    def dispatch(self, *args, **kwargs):
        return super(BookTemplateView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BookTemplateView, self).get_context_data(**kwargs)
        try:
            context['authors_list'] = call_api(self.request, url='/authorsapi/common_operations/')
            context['categories_list'] = call_api(self.request, url='/categoryapi/common_operations/')
            publishers_name_list = []
            publishers_list = call_api(self.request, url='/publisherapi/publisher-name-list/')
            context['publishers_name_list'] = publishers_list

            return context
        except Exception as e:
            return context

    def post(self, request, *args, **kwargs):
        params = request.POST
        print("params: ", params)
        try:
            data = {}
            book_id = params.get('book_id', None)
            if book_id:
                data['id'] = book_id
            data['book_name'] = params.get("book_name")
            data['publisher_id'] = params.get("publisher_id")
            # data['book_authors'] = params.get("book_authors")
            data['book_category_id'] = params.get("book_category")
            data['book_language'] = params.get("book_language")
            data['book_language_other_value'] = params.get("book_language_other_value")
            data['book_availability'] = params.get("book_availability")
            data['book_description'] = params.get("book_description")

            resp = requests.post(BASE_URL + "/bookapi/common_operations/", data=data, cookies=request.COOKIES)
            print("Res: ", resp)
            print("Res Content: ", resp.content)
            data = json.loads(resp.content)

            return redirect(BASE_URL +'/')

        except Exception as e:
            data['status_code'] = 400
            data['message'] = str(e)
            return data


    # def post(self, request, *args, **kwargs):
    #     user_id = request.POST.get('user_id')
    #     return redirect('/customer-care/calendar/' + user_id)


def edit_book(request, pk=None):
    template_name = 'books/book_entry.html'
    if request.method == "GET":
        context = {}
        context['authors_list'] = call_api(request, url='/authorsapi/common_operations/')
        context['categories_list'] = call_api(request, url='/categoryapi/common_operations/')
        context['publishers_name_list'] = call_api(request, url='/publisherapi/publisher-name-list/')
        context['book_details'] = call_api(request, url='/bookapi/common_operations/' + str(pk)+'/')
        template = loader.get_template(template_name)
        return HttpResponse(template.render(context, request))



