from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import ujson
from microframeworks.settings import HOST, PORT, JSON_DATA, TEXT
import resource
resource.setrlimit(resource.RLIMIT_NOFILE, (999999, 999999))

def text_test(request):
    return Response(TEXT)

def json_test(request):
    return ujson.dumps(JSON_DATA)

def about(request):
    return 'Pyramid'

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('text', '/text')
        config.add_view(text_test, route_name='text')

        config.add_route('about', '/about')
        config.add_view(about, route_name='about')

        config.add_route('json', '/json')
        config.add_view(json_test, route_name='json', renderer='json')

        app = config.make_wsgi_app()
    server = make_server(HOST, PORT, app)
    server.serve_forever()