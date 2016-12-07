from django.template.context_processors import csrf
from django.template.defaultfilters import register
from django.template.loader import get_template
from django.shortcuts import render_to_response

from database.models import req, res
from django.template import Template, Context
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
import datetime
from django.db.models import Q
from pip._vendor import requests
import json
from django.core import serializers


def button(request):
    t = """<html>
             <head>
              <title>Button</title>
             </head>
             <body>
              <form>
               <p><a href= "http://127.0.0.1:8000/run/"><input type="button" value="START THIS SHIT"></a></p>
              </form>
             </body>
            </html>"""
    return HttpResponse(t)


def test(request):
    c = req.objects.all()
    for i in c:
        d = i.header
        r = requests.post(i.url, json=json.loads(i.body.replace('\'', '\"')), headers=d)
        u = datetime.date.today()
        b = res.objects.create(status=str(r), body=r.json(), tag=i, date=u)
        b.save()
    raw_template = """<html>
     <body>
      <form>
        <p>
       DONE:
       SUCCESSFUL - {{ t }}
       </p>
      </form>
     </body>
    </html>"""
    t = Template(raw_template)
    f = t.render(Context({'t': len(c)}))
    return HttpResponse(f)


def doublefilter(request, date, tags):
    c = req.objects.get(tag=tags)
    crit1 = Q(date=date)
    crit2 = Q(tag_id=tags)
    d = res.objects.filter(crit1 & crit2)
    print d
    for i in d:
        print i.body
    t = get_template('doublefilter.html')
    f = t.render(Context({'url': c.url, 'method': c.method, 'header': c.header, 'wtf': d}))
    return HttpResponse(f)


def creat(request):
    hd = {"Authorization": "Basic cDM3NDY3MTI3LTI6JFNTVUtJMjAxNSQ=", "Content-Type": "application/json"}
    bd = {
        "email": "w@w.w",
        "api_key":"14803776003933e18902cbf9b6ed6aa15b18ed6358"
    }
    b = req.objects.create(url="https://ssuki.com/api2/api2.asp?test=yes&cmd=readpage", method='post', header=hd, body=bd, tag='user')
    b.save()
    c = req.objects.get(tag='login')
    return HttpResponse(c.body)


def _byteify(data, ignore_dicts = False):
    # if this is a unicode string, return its string representation
    if isinstance(data, unicode):
        return data.encode('utf-8')
    # if this is a list of values, return list of byteified values
    if isinstance(data, list):
        return [ _byteify(item, ignore_dicts=True) for item in data ]
    # if this is a dictionary, return dictionary of byteified keys and values
    # but only if we haven't already byteified it
    if isinstance(data, dict) and not ignore_dicts:
        return {
            _byteify(key, ignore_dicts=True): _byteify(value, ignore_dicts=True)
            for key, value in data.iteritems()
        }
    # if it's anything else, return it in its original form
    return data


@register.filter
def response_date_filter(request_obj, date_filter):
    c = request_obj.restag.filter(date=date_filter)
    data = serializers.serialize('json', c)
    d = _byteify(json.loads(data, object_hook=_byteify), ignore_dicts=True)
    return d


def wrong(request, date):
        c = req.objects.all()
        # data1 = serializers.serialize('json', wtf)
        # d1 = _byteify(json.loads(data1, object_hook=_byteify), ignore_dicts = True)
        # w = list(res.objects.filter(date=date))
        # data = serializers.serialize('json', c)
        # d = _byteify(json.loads(data, object_hook=_byteify), ignore_dicts = True)
        raw = get_template('tmpl_dtfilter.html')
        # t = Template(raw)
        f = raw.render(Context({'c': c, 'date': date}))
        # a = '\n'.join(str(str(k) + ' : ' + str(v)) for k, v in d1[0].items())
        # print d1[0].get('fields')
        return HttpResponse(f)


def search_form(request):
    c = req.objects.all()
    print c
    return render(request, 'datepicker.html', {'wtf': c})


def search(request):
    if 'date' and 'tag' in request.GET:
        c = req.objects.get(tag=str(request.GET['tag']))
        crit1 = Q(date=str(request.GET['date']))
        crit2 = Q(tag_id=str(request.GET['tag']))
        d = res.objects.filter(crit1 & crit2)
        t = get_template('doublefilter.html')
        print d
        message = t.render(Context({'url': c.url, 'method': c.method, 'header': c.header, 'wtf': d}))
    elif 'date' in request.GET:
        c = req.objects.all()
        raw = get_template('tmpl_dtfilter.html')
        message = raw.render(Context({'c': c, 'date': str(request.GET['date'])}))
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)


def some_form(request):
    if request.method == 'POST':
        if request.POST.get('tag') in request.POST['tag']:
            raw_template = """<html>
                 <body>
                  <form>
                    <p>
                   DONE:
                   SUCCESSFUL - {{ t }}
                   </p>
                  </form>
                 </body>
                </html>"""
            t = Template(raw_template)
            f = t.render(Context({'t': request.POST.get('tag')}))
            return HttpResponse(f)


def some_form2(request):
    c = {}
    c.update(csrf(request))
    return render_to_response("someform2.html", c)
