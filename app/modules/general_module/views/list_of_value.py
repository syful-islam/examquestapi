from django.apps import apps
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import PermissionDenied

class LovView(APIView):
    # authentication_classes = []
    # permission_classes = [AllowAny]
   
    models_config = {
        "departments": {
            "model": "Department",
            "id_field": "id",
            "title_field": "name",
            "sub_title_field": "",
        },
        "categories": {
            "model": "Category",
            "id_field": "id",
            "title_field": "name",
            "sub_title_field": "type",
        },
        "softwarepublishers": {
            "model": "SoftwarePublisher",
            "id_field": "id",
            "title_field": "name",
            "sub_title_field": "",
        },
        "softwares": {
            "model": "Software",
            "id_field": "id",
            "title_field": "software_name",
            "sub_title_field": "category__name",  # Assuming category is a ForeignKey
        },
        "suppliers": {
            "model": "Supplier",
            "id_field": "id",
            "title_field": "supplier_name",
            "sub_title_field": "software_name__software_name",  # Assuming software is a ForeignKey
        },
        "users": {
            "model": "SAMUser",
            "id_field": "id",
            "title_field": "full_name",
            "sub_title_field": "",
        },
        # "packages": {
        #     "model": "Package",
        #     "id_field": "id",
        #     "title_field": "name",
        #     "sub_title_field": "",
        # },
    }

    def get(self, request, model):
        config = self.models_config.get(model)
        if not config:
            return Response({"error": "Invalid data model"}, status=status.HTTP_400_BAD_REQUEST)

        if not self.request.user.is_authenticated or not hasattr(self.request.user, 'subscriber'):
            raise PermissionDenied("User must be authenticated to access.")
        
        ModelClass = apps.get_model('app', config["model"])  # Replace 'app' with your app name
        queryset = ModelClass.objects.filter(subscriber=self.request.user.subscriber)        
        
        # Apply filters based on query parameters
        for key, value in request.GET.items():
            if key == "manufacturer":  # Filtering by manufacturer ID
                queryset = queryset.filter(manufacturer_id=value)
            if key == "type":  # Filtering by category type
                queryset = queryset.filter(type=value)
            elif key == "keyword":  # Filtering where title (model) starts with the keyword
                queryset = queryset.filter(**{f"{config['title_field']}__istartswith": value})

        # Fetch and rename fields
        data = self.new_method(config, queryset)
        data.sort(key=lambda x: x[config["title_field"]].lower())
        formatted_data = [
            {
                "id": item[config["id_field"]],
                "title": item[config["title_field"]],
                "sub-title": item[config["sub_title_field"]] if config["sub_title_field"] else '',
            }
            for item in data
        ]

        return Response(formatted_data, status=status.HTTP_200_OK)

    def new_method(self, config, queryset):
        fields = [config["id_field"], config["title_field"]]
        if config["sub_title_field"]:
            fields.append(config["sub_title_field"])
        data = list(queryset.values(*fields))
        return data
    
class LovAllowAnyView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]
   
    models_config = {
        "packages": {
            "model": "Package",
            "id_field": "id",
            "title_field": "name",
            "sub_title_field": "",
        },
    }

    def get(self, request, model):
        config = self.models_config.get(model)
        if not config:
            return Response({"error": "Invalid data model"}, status=status.HTTP_400_BAD_REQUEST)

        ModelClass = apps.get_model('app', config["model"])  # Replace 'app' with your app name
        queryset = ModelClass.objects.all()
        
        # Apply filters based on query parameters
        for key, value in request.GET.items():
            if key == "manufacturer":  # Filtering by manufacturer ID
                queryset = queryset.filter(manufacturer_id=value)
            if key == "type":  # Filtering by category type
                queryset = queryset.filter(type=value)
            elif key == "keyword":  # Filtering where title (model) starts with the keyword
                queryset = queryset.filter(**{f"{config['title_field']}__istartswith": value})

        # Fetch and rename fields
        data = self.new_method(config, queryset)
        data.sort(key=lambda x: x[config["title_field"]].lower())
        formatted_data = [
            {
                "id": item[config["id_field"]],
                "title": item[config["title_field"]],
                "sub-title": item[config["sub_title_field"]] if config["sub_title_field"] else '',
            }
            for item in data
        ]

        return Response(formatted_data, status=status.HTTP_200_OK)

    def new_method(self, config, queryset):
        fields = [config["id_field"], config["title_field"]]
        if config["sub_title_field"]:
            fields.append(config["sub_title_field"])
        data = list(queryset.values(*fields))
        return data