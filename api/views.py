import json

from django.views.generic import View, TemplateView
from django.http.response import HttpResponse

from .gokulang.gokulang import GokuLang


class GokuLangView(View):

    def get(self, request):

        text = request.GET.get('text') if request.GET.get('text') else ''

        g = GokuLang()
        translated = g.translate(text)

        response = {'original': text, 'translated': translated}

        return HttpResponse(json.dumps(response, ensure_ascii=False), content_type='application/json')

    def post(self, request):

        text = request.POST.get('text') if request.POST.get('text') else ''

        g = GokuLang()
        translated = g.translate(text)

        response = {'original': text, 'translated': translated}

        return HttpResponse(json.dumps(response, ensure_ascii=False), content_type='application/json')


class IndexView(TemplateView):

    template_name = 'api/index.html'