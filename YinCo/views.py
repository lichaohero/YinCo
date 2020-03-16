from django.http import HttpResponse, JsonResponse


def test_cors(request):
    return JsonResponse({'code': 200, 'msg': '跨域成功'})
