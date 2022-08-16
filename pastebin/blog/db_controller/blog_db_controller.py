from blog.models import BlogData
from blog.config import Config
from rest_framework import exceptions
from django.db.utils import IntegrityError

def create_new_entry(payload):
    try:
        user = BlogData.objects.create(**payload)
        response_status, message = Config.GENERIC.SUCCESS
        return response_status, message, user
    except Exception as e:
        response_status, message = Config.GENERIC.FAILURE
        return response_status, message, None