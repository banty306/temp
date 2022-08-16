import uuid
from blog.db_controller import blog_db_controller
from blog.config import Config
from blog.serializer import blog_serializer

class BlogController():
    def blog(self, **kwargs):
        data ={}
        data["author"] = kwargs.get("author")
        data["title"] = kwargs.get("title")
        data["description"] = kwargs.get("description")
        data["key"] = uuid.uuid4()

        response_status, message, user = blog_db_controller.create_new_entry(data)
        if response_status == Config.GENERIC.SUCCESS[0]:
            response_data ={}
            serialized_data = blog_serializer.BlogSerializer(user)
            response_data["author"] = serialized_data['author'].value
            response_data["title"] = serialized_data['title'].value
            response_data["description"] = serialized_data['description'].value
            response_data["created_at"] = serialized_data['created_at'].value
            # response_data["updated_at"] = serialized_data['updated_at'].value
            response_data["views"] = serialized_data['views'].value
            response_data["link"] = Config.URLS.BASE_URL.format(id= serialized_data["key"].value)
            return response_status, message, response_data

        return response_status, message, None





