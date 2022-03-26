import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from jsonrpcserver import method, Result, Success, dispatch, Error
from rest_framework import serializers


@method
def info(**kwargs) -> Result:
    print(kwargs)
    valid = CardSerializer(data=kwargs)
    if valid.is_valid():
        number = json.dumps(kwargs['number'])
        expire = json.dumps(kwargs['expire'])
        return Success(kwargs)
    else:
        return Error(404, {
            "uz": "Xato",
            "ru": "Oshibka",
            "en": "Validation error",
        }

                     )


@csrf_exempt
def jsonrpc(request):
    return HttpResponse(
        dispatch(request.body.decode()), content_type="application/json"
    )


class CardSerializer(serializers.Serializer):
    number = serializers.CharField(required=True, max_length=16)
    expire = serializers.CharField(required=True, max_length=4)
