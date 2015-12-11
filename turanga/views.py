from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
# from django.views.decorators.csrf import csrf_exempt


import time
import json
import codecs


class IndexViews(generic.View):
    templates_file = 'turanga.html'

    def get(self, request):

        context = {
        }

        return render(request,
                      self.templates_file,
                      context)



def crash(request):

    print request

    if request.method == "POST":
        if 'log' in request.POST and request.POST['log']:
            log = request.POST["log"]
        else:
            return HttpResponse("no log!")

        if 'platform' in request.POST and request.POST['platform']:
            service = request.POST['platform']
        else:
            return HttpResponse("no platform!")

        pub_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

        req = json.loads(log)

        print req

        with codecs.open('static/json/' + service + pub_date + '.json', 'w', 'utf-8') as f:
            f.write(json.dumps(log, ensure_ascii=False, indent=1))

        return HttpResponse("success!")

    else:
        return HttpResponse("request is not POST!")