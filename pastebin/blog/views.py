from django.http import HttpResponse
from rest_framework.views import APIView
from blog.serializer import blog_serializer
from blog.controllers.blog_controller import BlogController
from blog.config import Config
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class BlogView(APIView):

    def post(self, request):
        serialized_data = blog_serializer.BlogSerializer(data=request)
        serialized_data.is_valid(raise_exception=True)
        request_data = serialized_data.validated_data
        response_status, message, response = BlogController().blog(**request_data)
        if not (response_status == Config.GENERIC.SUCCESS[0]):
            response = {
                "status": response_status,
                "message": message,
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        if response_status == Config.GENERIC.SUCCESS[0]:
            response = {
                "status": response_status,
                "message": message,
                "data": response
            }
            return Response(response, status=status.HTTP_200_OK)

