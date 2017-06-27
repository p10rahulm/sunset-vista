from django.http import HttpResponse,Http404
from django.template.loader import get_template
from django.shortcuts import render
from collections import defaultdict

import datetime

def index(request):
    return HttpResponse("Hello World!")

def current_datetime(request):
    now = datetime.datetime.now()
    #t = get_template('current_datetime.html')
    #html = t.render()
    #return HttpResponse(html)
    return render(request,'current_datetime.html',{'current_date': now})

def display_meta(request):
    values = request.META
    html = []
    print(values)
    for k in sorted(values.keys()):
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, values[k]))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def hours_ahead(request,hours_ahead):
    try:
        offset = int(hours_ahead)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render(request, "hours_ahead.html",{'hour_offset': hours_ahead, 'next_time': dt})
    html = "<html><body>In %s hour(s), it will be  %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
