from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

class ContatoView(TemplateView):
    template_name = 'contatos.html'