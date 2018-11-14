
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

# CSRF껌증에서 제외되는 view
@csrf_exempt
def snippet_list(request):
    if request.method =='GET':
        snippets = Snippet.objects.all()
        # Snippet QuerySet을 생성자로 사용한 SnippetSerializer인스턴스
        serializer = SnippetSerializer(snippets, many=True)
        # JSON형식의 문자열을 HttpResponse로 돌려줌 (content_type에 'application/json'명시됨)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        # request를 분석해서 전달받은 JSON형식 문자열을 파이썬 데이터형으로 파싱
        data = JSONParser().parse(request)
        # data인수를 채우면서 Serializer인스턴스 생성 (역직렬화 과정)
        serializer = SnippetSerializer(data=data)
        # Serializer의 validation
        if serializer.is_valid():
            # valid한 경우, Serializer의 save()메서드로 새 Snippet인스턴스 생성
            serializer.save()
            # 생성 후 serializer.data로 직렬화한 데이터를 JSON형식으로 201(Create)상태코드 전달
            return JsonResponse(serializer.data, status=201)
        # invalid한 경우, error목록을 JSON혀익으로 리턴하며 400(Bad Request)상태코드 전달
        return JsonResponse(serializer.error, status=400)