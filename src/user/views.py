from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import IN_PATH, Parameter
from rest_framework import views
from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User


class UserViews(views.APIView):

    @swagger_auto_schema(
        responses={200: "OK", 400: "BAD REQUESTION"}
    )
    def post(self, request):
        form = UserForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('list_users')
        return render(request, 'users/create_user.html', {'form': form})

    @swagger_auto_schema(
        responses={200: "OK", 400: "BAD REQUESTION"}
    )
    def list(self, request):
        users = User.objects.all()
        return render(request, 'users/list_users.html', {'users': users})

    @swagger_auto_schema(
        manual_parameters=[Parameter(in_=IN_PATH, name='id', required=True, type='string')],
        responses={204: "NO CONTENT", 400: "BAD REQUESTION"}
    )
    def put(self, request, id):
        user = User.objects.get(id=id)
        form = UserForm(request.POST or None, instance=user)
        if form.is_valid():
            form.save()
            return redirect('list_users')
        return render(request, 'users/update_user.html', {'form': form, 'user': user})
