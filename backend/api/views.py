import json
from products.models import Product

""" from django.forms.models import model_to_dict
from django.http import JsonResponse """

from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer


""" def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data)
        #json_string = josn.dumps(data)
    return JsonResponse(data) """

@api_view(['GET'])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        data = ProductSerializer(instance).data
    return Response(data)