from django.http import HttpResponse
from django.shortcuts import render
from django.db.models.query import QuerySet

from rest import settings
from version import VERSION
import time
from auditlog.models import PersistentLog
from . import model as ms
from . import collection as cs
from . import json as js
from . import csv
from . import excel
# from . import profiler

def restStatus(request, status, data={}, **kwargs):
    if isinstance(data, str):
        if status:
            data = dict(message=data)
        else:
            data = dict(error=data)
    data = data.copy()
    data.update(kwargs)
    data["status"] = status
    return restResult(request, data)


# @profiler.timeit
def restGet(request, obj, fields=None, extra=[], exclude=[], recurse_into=[], **kwargs):
    data = ms.to_dict(obj, fields, extra, exclude, recurse_into)
    if not kwargs.get("return_httpresponse", True):
        return data
    data = dict(data=data, status=kwargs.get("status", True))
    data["datetime"] = int(time.time())
    data["elapsed"] = get_request_elapsed(request)
    return restResult(request, data)

# @profiler.timeit
def restList(request, qset, size=25, start=0, sort=None, fields=None, extra=[], exclude=[], recurse_into=[], **kwargs):
    count = 0
    if isinstance(qset, QuerySet):
        count = qset.count()
    elif isinstance(qset, list):
        count = len(qset)
    start = request.DATA.get("start", start, field_type=int)
    size = request.DATA.get("size", size, field_type=int)
    sort = request.DATA.get("sort", sort)
    data = cs.to_list(qset, sort, size, start, fields, extra, exclude, recurse_into)
    data["status"] = kwargs.get("status", True)
    data["datetime"] = int(time.time())
    data["elapsed"] = get_request_elapsed(request)
    data["count"] = count
    return restResult(request, data)


def restResult(request, data, status=200):
    if "status" not in data:
        data["status"] = True
        data["datetime"] = int(time.time())
        data["elapsed"] = get_request_elapsed(request)
    accept_list = parse_accept_list(request)
    restResponseLog(request, data)
    if 'application/json' in accept_list:
        return HttpResponse(js.serialize(data), content_type="application/json", status=status)
    elif 'text/html' in accept_list:
        return render_webview(request, data, status)
    return HttpResponse(js.prettyJSON(data), content_type="text/plain", status=status)


restReturn = restResult  # legacy support


def restResponseLog(request, resp):
    # render response
    if hasattr(request, "rest_debug") and request.rest_debug:
        if settings.DEBUG_REST_NO_LISTS and "count" in resp:
            if "count" in resp:
                if settings.DEBUG_REST_NO_LIST == "example":
                    sanatized = dict(count=resp.get("count"), size=resp.get("size"), data=resp.get("data", [])[:1])
                else:
                    sanatized = dict(count=resp.get("count"), size=resp.get("size"))
                PersistentLog.log(sanatized, 0, request, "rest", action="response")
            else:
                PersistentLog.log(resp, 0, request, "rest", action="response")
        else:
            PersistentLog.log(resp, 0, request, "rest", action="response")


def restPermissionDenied(request, error="permission denied", error_code=403):
    return restStatus(request, False, error=error, error_code=error_code)


def restNotFound(request):
    return restStatus(request, False, error="not found", error_code=404)


def restOK(request):
    return restStatus(request, True)


def restError(request, error, error_code=None):
    return restStatus(request, False, error=error, error_code=error_code)


def restJSON(request, qset, fields, name, size=10000):
    data = restList(None, qset, fields=fields, size=size)
    response = HttpResponse(js.prettyJSON(data), content_type="application/json")
    response['Content-Disposition'] = 'attachment; filename="{0}"'.format(name)
    return response


def restFlat(request, qset, fields, name, size=10000, header_cols=None):
    return HttpResponse(js.prettyJSON(list(qset.values_list(*fields))), content_type="application/json", status=200)


def restCSV(request, qset, fields, name, size=10000, header_cols=None):
    if size > 1200 and qset.count() > 1200:
        # large data set lets stream
        qset = qset[:size]
        response = csv.generateCSVStream(qset, fields, name)
        response['Cache-Control'] = 'no-cache'
        response['Content-Disposition'] = f'attachment; filename="{name}"'
    else:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{name}"'
        qset = qset[:size]
        csv.generateCSV(qset, fields, name, output=response, header_cols=header_cols)
    return response


def restExcel(request, qset, fields, name, size=10000, **kwargs):
    return excel.qsetToExcel(request, qset[:size], fields, name)


def parse_accept_list(request):
    if request and request.DATA.get('_type', None):
        accept_list = [request.DATA.get('_type')]
    elif request and 'HTTP_ACCEPT' in request.META:
        accept_list = request.META["HTTP_ACCEPT"].split(',')
    elif request and 'HTTP_ACCEPT_ENCODING' in request.META:
        accept_list = request.META["HTTP_ACCEPT_ENCODING"].split(',')
    else:
        accept_list = []
    return accept_list


def get_request_elapsed(request):
    if request is not None:
        return int((time.perf_counter() - request._started)*1000)
    return 0


def render_webview(request, data, status=200):
    output = js.prettyJSON(data)
    req_dict = request.DATA.asDict()
    req_out = js.prettyJSON(req_dict)
    path = request.path
    parts = path.split('/')
    last_pk = parts.pop()
    if last_pk and last_pk.isdigit():
        path = "/".join(parts)
    else:
        last_pk = ""

    is_debug = settings.get("DEBUG", False) or settings.get("REST_DEBUGGER", False)
    rest_help = {}
    if is_debug and hasattr(request, "rest_class"):
        rest_help = request.rest_class.get_rest_help()
        rest_help = js.prettyJSON(rest_help)
    context = {
        "help": rest_help,
        "input": req_dict,
        "pk": last_pk,
        "output_dict": data,
        "output": output,
        "req_out": req_out,
        "path": path,
        "method": request.method,
        "debug": is_debug,
        "request": request,
        "version": VERSION
    }
    return render(request, "rest_html.html", context, status=status)
