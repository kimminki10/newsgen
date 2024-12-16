from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
from ..model.UserModel import User, Ticker
from ..controller.UserSerialize import UserSerializer


class UserView(APIView):
    def get(self,request):
        """
        {
            "name":"A",
            "password":"aaa"
        }      
        """
        # 계정 정보 가져오기
        print("User Get")
        
        name = request.data.get('name')  # GET 요청에서 query parameters로 받음
        password = request.data.get('password')
      

        # 필수 필드 검증
        if not name or not password:
            return Response(
                {"success": False, "error": "Name and password are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # 이름으로 사용자 검색
            user = User.objects.get(name=name)
            ticker = user.tickers
  
            # 비밀번호 확인
            if password == user.password:  # 비밀번호 검증
                serializer = UserSerializer(user)  # 사용자 데이터를 직렬화
                return Response(
                    {"success": True, "user": serializer.data},
                    status=status.HTTP_200_OK
                ) 
            else:
                return Response(
                    {"success": False, "error": "Invalid password."},
                    status=status.HTTP_401_UNAUTHORIZED
                )
        except User.DoesNotExist:
            return Response(
                {"success": False, "error": "User not found."},
                status=status.HTTP_404_NOT_FOUND
            )
    def post(self, request):
        """
        {
            "name":"A",
            "password":"aaa",
            "email":"fenpon45@naver.com"
        }
        """
        print("UserView : Post")
        # 회원 가입
        name = request.data.get('name')
        email = request.data.get('email')
        password = request.data.get('password')

        # 필수 필드 검증
        if not all([name, email, password]):
            return Response({'success': False,'error': 'Name, email, and password are required.'},
                            status=status.HTTP_400_BAD_REQUEST)

        # 중복 이메일 체크
        if User.objects.filter(email=email).exists():
            return Response({'success': False,'error': 'Email already exists.'},
                            status=status.HTTP_400_BAD_REQUEST)
        #중복 이름 체크
        if User.objects.filter(name=name).exists():
            return Response({'success': False,'error': 'Name already exists.'},
                            status=status.HTTP_400_BAD_REQUEST)

        try:    
            # User 객체 생성
            user = User.objects.create(
                name=name,
                email=email,
                password=password,  # 비밀번호 암호화가 필요하다면 make_password 사용
            )
            # ManyToManyField 초기화 (빈 관계 설정)
            user.tickers.set([])
                
            return Response({'success': True}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'success': False,'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    ##def patch(self, request):
        ## 내용 업데이트

        
class UserTickers(APIView):
    """
    User 테이블에 Ticker 객체와 연결
    {
        "user_id":1,
        "tickers":[1]
    }
    """
    def post(self, request):
        print("User Tickers : Post")
        user_id = request.data.get('user_id')
        ticker_ids = request.data.get('tickers', [])  # Expecting a list of ticker IDs

        # Validate required fields
        if not user_id or not ticker_ids:
            return Response(
                {"success": False, "error": "User ID and tickers are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Fetch the user
            user = User.objects.get(id=user_id)
            print(user.name)
            # Fetch the Ticker objects
            tickers = Ticker.objects.filter(id__in=ticker_ids)

            # Add the Ticker objects to the user's tickers field
            user.tickers.add(*tickers)
            print(user.tickers.count())
            return Response(
                {"success": True, "message": "Tickers added successfully."},
                status=status.HTTP_200_OK
            )
        except User.DoesNotExist:
            return Response(
                {"success": False, "error": "User not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"success": False, "error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


    
    