from django.http import HttpResponse,Http404
import datetime

def index(request):
    return HttpResponse("Hello World!")

def current_datetime(request):
    now = datetime.datetime.now()
    html= "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def hours_ahead(request,hours_ahead):
    try:
        offset = int(hours_ahead)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be  %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
