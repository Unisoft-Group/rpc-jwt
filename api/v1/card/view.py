from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def info(request):
    print(request.data)
    return Response(request.data)
