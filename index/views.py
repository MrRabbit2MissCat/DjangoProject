from django.shortcuts import render
from django.http import JsonResponse
from index.models import UserModel


# Create your views here.
def index(request):
    return render(
        request,
        "index.html",
    )


def user(request):
    if request.method == "GET":
        return render(
            request,
            "base.html"
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

        u = UserModel.objects.create(id=user_id, name=name, email=email, address=address, message=message)
        u.save()
        data = {"code": 200, "message": f"{name}你好！信息录入成功"}
        return JsonResponse(data)
