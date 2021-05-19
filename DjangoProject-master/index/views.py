import os

from django.shortcuts import render
from django.http import JsonResponse, QueryDict

from index.models import UserModel


def user(request):
    if request.method == "GET":
        return render(
            request,
            "index.html",
        )
    elif request.method == "POST":
        user_id = 0
        name = request.POST['username']
        email = request.POST['email']
        address = request.POST['address']
        message = request.POST['message']
        last_u = UserModel.objects.last()
        if last_u:
            user_id = int(last_u.id) + 1

        u = UserModel.objects.create(id=user_id, name=name,
                                     email=email, address=address,
                                     message=message)
        u.save()
        data = {"code": 200, "message": f"{name}你好！信息录入成功"}
        return JsonResponse(data)


def table(request):
    if request.method == "GET":
        users = UserModel.objects.all()
        return render(
            request,
            "table.html",
            {"data": users}
        )
    elif request.method == "DELETE":
        delete = QueryDict(request.body)
        delete_id = delete.get("id")
        UserModel.objects.get(id=delete_id).delete()
        data = {"code": 200, "message": f"成功删除"}
        return JsonResponse(data)
