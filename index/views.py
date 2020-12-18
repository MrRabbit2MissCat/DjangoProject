import os

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, QueryDict

from django.conf import settings
from index.models import UserModel
from django.core import serializers


# Create your views here.
def index(request):
    if request.method == "POST":
        img = request.FILES.get("fastaFile")
        # 获取上传图片的名称
        img_name = img.name
        # 获取后缀
        ext = os.path.splitext(img_name)[1]
        # 重新规定图片名称，图片类型
        img_name = f'avatar-{ext}'

        # 图片保存路径
        img_path = os.path.join(settings.IMG_UPLOAD, img_name)

        # 写入 上传图片的 内容
        with open(img_path, 'ab') as fp:
            # 如果上传的图片非常大， 那么通过 img对象的 chunks() 方法 分割成多个片段来上传
            for chunk in img.chunks():
                fp.write(chunk)

    return render(
        request,
        "han.html",
    )


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
