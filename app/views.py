import requests

from django.http import JsonResponse


def loader(request):
    data = request.GET.dict()
    url = data.pop('loader_url')
    response = requests.get(url, params=data)
    return JsonResponse(response.json())
