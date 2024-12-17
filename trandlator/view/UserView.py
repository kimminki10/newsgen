from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
from django.core.exceptions import ObjectDoesNotExist
from ..model.UserModel import User
from ..model.TickerModel import Ticker
from ..controller.UserSerialize import UserSerializer
from ..controller.TickerSerialize import TickerSerializer


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
        
    def patch(self, request):
        ## 내용 업데이트
        """
        {
            "id" :  3, 
            "name":"A",
            "password":"aaa",
            "email":"fenpon45@naver.com"
        }
        id는 필수
        User 테이블에서 id를 조회하여 name , password , email 값을 바꿔줌 
        """
        data = request.data
        
        # 필수 값 확인
        user_id = data.get("id")
        if not user_id:
            return Response({"error": "User ID is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        # User 객체 가져오기
        user = User.objects.get(id=user_id)

         # 제공된 값만 업데이트
        update_fields = {}
        for field in ['name', 'password', 'email']:
            if field in data:
                update_fields[field] = data[field]
        
        # User 모델 업데이트
        for key, value in update_fields.items():
            setattr(user, key, value)
        
        user.save()  # 변경 사항 저장
        
        return Response({"message": "User updated successfully", "updated_fields": update_fields}, status=status.HTTP_200_OK)
    def delete(self, request):
        ##User table에서 id조회하여 제거
        """
        {
            "id" :  3, 
        }
        """
        data = request.data
        
        # 필수 값 확인
        user_id = data.get("id")
        if not user_id:
            return Response({"error": "User ID is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        # User 객체 가져오기
        user = User.objects.get(id=user_id)
        
        # User 삭제
        user.delete()
        
        return Response({"message": f"User with id {user_id} deleted successfully."}, status=status.HTTP_200_OK)
       
        
class UserTickers(APIView):
    """
    User 테이블에 Ticker 객체와 연결
    {
        "id":1,
        "ticker_names":["ticker"],
        "option" : false
    }
    """
    def post(self, request):
        
        print("User Tickers : Post")
        user_id = request.data.get('id')
        ticker_names = request.data.get('ticker_names', [])  # Expecting a list of ticker IDs
        option = request.data.get('option', True)  # True = add, False = remove (default is add)

        if not user_id or not ticker_names:
            return Response(
                {"success": False, "error": "User ID and tickers are required."},
                status=status.HTTP_400_BAD_REQUEST
            )
        

        tickers = Ticker.objects.filter(ticker_name__in=ticker_names)
        
        try:
            # Fetch the user
            print("!")
            user = User.objects.get(id=user_id)
            print(user.name)

            # Fetch the Ticker objects as a queryset
           
           
            if option:
                # Add the Ticker objects to the user's tickers field
                user.tickers.add(*tickers)  # Unpack only if iterable
                action = "added"
                print("+")
            else:
                print("----")
                print(tickers)
                if not tickers.exists():
                    return Response(
                        {"success": False, "error": "No valid tickers found for the given IDs."},
                        status=status.HTTP_400_BAD_REQUEST
                    )
                # Remove the Ticker objects from the user's tickers field
                user.tickers.remove(*tickers)
                action = "removed"
                print("-")

            print(user.tickers.count())
            return Response(
                {
                    "success": True,
                    "message": f"Tickers successfully {action}.",
                    "remaining_tickers_count": user.tickers.count()
                },
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"success": False, "error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def get(self, request):
        """
        User 테이블에 연결된 Ticker 객체 목록 가져옴
        {
            "id":1
        }
        """
        user_id = request.data.get('id')  # Query Parameters에서 id 가져오기
        
        # id가 제공되지 않은 경우 예외 처리
        if not user_id:
            return Response({
                "success": False,
                "error": "Query parameter 'id' is required."
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            # User 객체 가져오기
            user = User.objects.get(id=user_id)

            # ManyToMany 관계로 연결된 Ticker 객체들 가져오기
            tickers = user.tickers.all()

            # Ticker 데이터 직렬화
            serializer = TickerSerializer(tickers, many=True)

            return Response({
                "success": True,
                "tickers": serializer.data
            }, status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            return Response({
                "success": False,
                "error": f"User with id '{user_id}' does not exist."
            }, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({
                "success": False,
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
    