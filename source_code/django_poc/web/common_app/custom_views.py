import json
import requests


from django.views.generic import TemplateView



class WebTemplateView(TemplateView):

    def fetch_api_data(self, api_url, base_url= "http://localhost:8000", method='GET', payload = {}, **kwargs):
        if method and method.upper()=='GET':
            api_req = requests.get(base_url + api_url, params=payload, cookies=self.request.COOKIES)
            return json.loads(api_req.content)