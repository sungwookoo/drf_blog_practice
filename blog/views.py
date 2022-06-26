from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework import permissions
from rest_framework import status
from blog.models import Article
from blog.serializers import ArticleSerializer
from user.models import User
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from drf_shop.permissions import RegistedMoreThanThreeDaysUser

# Create your views here.


class BlogView(APIView):  # CBV 방식
    # permission_classes = [permissions.AllowAny]  # 누구나 view 조회 가능
    # permission_classes = [permissions.IsAdminUser] # admin만 view 조회 가능
    # permission_classes = [permissions.IsAuthenticated]  # 로그인 된 사용자만 view 조회 가능
    permission_classes = [RegistedMoreThanThreeDaysUser]  # custom permission

    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)
        # return Response({'message': 'get method!!'})

    def post(self, request):
        # data = JSONParser().parse(request)
        # serializer = ArticleSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save(author=self.request.user)
        #     return JsonResponse(serializer.data, status=201)

        # return JsonResponse(serializer.errors, status=400)
        user = request.user
        title = request.data.get("title", "")
        content = request.data.get("content", "")
        categories = request.data.get("category", [])

        if len(title) <= 5:
            return Response({"error": "타이틀은 5자 이상 작성하셔야 합니다."}, status=status.HTTP_400_BAD_REQUEST)

        if len(content) <= 20:
            return Response({"error": "내용은 20자 이상 작성하셔야 합니다."}, status=status.HTTP_400_BAD_REQUEST)

        if not categories:
            return Response({"error": "카테고리가 지정되지 않았습니다."}, status=status.HTTP_400_BAD_REQUEST)

        article = Article(
            author=user,
            title=title,
            content=content
        )

        article.save()
        article.category.add(*categories)
        return Response({"message": "성공!"}, status=status.HTTP_200_OK)

    def put(self, request):
        return Response({'message': 'put method!!'})

    def delete(self, request):
        return Response({'message': 'delete method!!'})
