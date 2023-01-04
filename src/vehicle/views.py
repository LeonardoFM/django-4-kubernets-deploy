from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import IN_PATH, Parameter
from django.http import HttpResponse
from django.template import loader
from rest_framework import views
from rest_framework.response import Response

from .models import Vehicle
from .serializers import VehicleSerializer


class VehicleViews(views.APIView):

    @swagger_auto_schema(
        request_body=VehicleSerializer,
        responses={200: "OK", 400: "BAD REQUESTION"}
    )
    def post(self, request):
        import pdb;pdb.set_trace()

        template = loader.get_template('vehicle/base.html')

        vehicles = Vehicle.objects.all()
        context = {
            'variable_name': 'Leonardo',
            'is_authenticated': True,
            'ships': vehicles
        }
        return HttpResponse(template.render(context, request))

    @swagger_auto_schema(
        manual_parameters=[Parameter(in_=IN_PATH, name='id', required=True, type='string')],
        responses={200: "OK", 400: "BAD REQUESTION"}
    )
    def get(self, request, _id):
        vehicle = get_object_or_404(Vehicle, id=_id)
        progress = vehicle.name
        return Response(data={"progress": f"{progress}", "relation": f"{vehicle.description}:{vehicle.cost}"}, status=200)
