from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..model.UserModel import UserItem
from ..controller.UserSerialize import UserItemSerializer


class TestAPIView(APIView):
    """
    Handle GET and POST requests.
    """
    def get(self,request):
        # GET 요청에서 간단히 데이터를 반환
        return Response({"data":8}, status=status.HTTP_200_OK)
    def post(self, request):
        # POST 요청 데이터를 검증
        result = {"test": 3}
        return Response(result, status=status.HTTP_200_OK)
