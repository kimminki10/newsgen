from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def test(request):
    """
    Handle GET and POST requests.
    """
    if request.method == 'GET':
        # GET 요청에서 간단히 데이터를 반환
        result = {"test": 3}
        return Response(result, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        # POST 요청 데이터를 검증
        result = {"test": 3}
        return Response(result, status=status.HTTP_200_OK)
