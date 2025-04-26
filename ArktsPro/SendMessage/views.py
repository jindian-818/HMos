import random

from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import *
import json


@csrf_exempt
def json_view(request):
    TheData = JSONParser().parse(request)
    username = TheData.get('user', None)
    thePassword = TheData.get('password', None)
    print("*************************************")
    print(username, thePassword)
    ParentsNumber = Parent.objects.filter(id=username, password=thePassword).count()
    if ParentsNumber == 0:
        data = {
            "answer": "false"
        }
        return JsonResponse(data)
    elif ParentsNumber >= 1:
        data = {
            "answer": "true"
        }
        return JsonResponse(data)


@csrf_exempt
def registerUi(request):
    TheData = JSONParser().parse(request)
    password = TheData.get('password', None)
    userName = TheData.get('username', None)
    phoneNumber = TheData.get('phoneNumber', None)
    address = TheData.get('address', None)
    print("************************")
    print(password)
    parent = Parent(id=userName, password=password, phone=phoneNumber, address_info=address)  # 创建 Parent 实例
    parent.save()  # 保存实例到数据库中
    ParentsNumber = Parent.objects.filter(id=userName, password=password).count()
    if ParentsNumber == 0:
        data = {
            "answer": "false"
        }
        return JsonResponse(data)
    elif ParentsNumber >= 1:
        data = {
            "answer": "true"
        }
        return JsonResponse(data)


@csrf_exempt
def search(request):
    TheData = JSONParser().parse(request)
    info = TheData.get('data', None)
    print("************************")
    print(info)
    TeacherInfo = Teacher.objects.filter(name=info)
    teachers = TeacherInfo.values('name', 'id')  # 使用values()获取特定字段
    data = []
    for teacher in teachers:
        teacher_data = {"name": teacher['name'], "id": teacher['id']}
        data.append(teacher_data)
    return json.dumps(data)


@csrf_exempt
def teacherSearch(request):
    TheData = JSONParser().parse(request)
    subject = TheData.get('subject')
    teachers = Teacher.objects.filter(teaching_experience='数学')
    results = [teacher.values() for teacher in teachers]
    print("results")
    return JsonResponse({"teachers": results}, safe=False)


@csrf_exempt
def subjectSearch(request):
    TheData = JSONParser().parse(request)
    subject = TheData.get('subject', None)
    # 查询teaching表中subject字段与给定subject匹配的记录
    teachers = Teacher.objects.filter(teaching_experience=subject)
    # 将查询结果转换为JSON格式
    data = [{'name': teacher.name, 'id': teacher.id, 'grade': teacher.grade} for teacher in teachers]
    print(data)
    return JsonResponse({'teachers': data}, safe=False)


@csrf_exempt
def gradeSearch(request):
    TheData = JSONParser().parse(request)
    subject = TheData.get('subject', None)
    grade = TheData.get('grade', None)
    print(type(grade), grade)
    # 查询teaching表中subject字段与给定subject匹配的记录
    teachers = Teacher.objects.filter(teaching_experience=subject, grade=grade)
    # 将查询结果转换为JSON格式
    data = [{'name': teacher.name, 'id': teacher.id, 'grade': teacher.grade} for teacher in teachers]
    print(data)
    return JsonResponse({'teachers': data}, safe=False)


@csrf_exempt
def booking(request):
    TheData = JSONParser().parse(request)
    name = TheData.get('name', None)
    print('******************')
    print(name)
    if name is not None:
        data = {
            'result': "true"
        }
    else:
        data = {
            'result': 'false'
        }
    return JsonResponse(data)


@csrf_exempt
def iot(request):
    # 生成七个随机数
    random_numbers = [random.randint(1, 50) for _ in range(10)]
    print('*****************')
    print(random_numbers,type(random_numbers))
    # 将随机数封装成一个字典
    data = {
        'random_numbers': random_numbers
    }

    # 返回JSON响应
    return JsonResponse(data)



@csrf_exempt
def advise(request):
    TheData = JSONParser().parse(request)
    advice = TheData.get('advice', None)
    name = TheData.get('teacherName', None)
    teacher = Teacher.objects.filter(name=name).first()
    if not teacher:
        data = {
            'answer': 'false'
        }
        return JsonResponse(data)

        # 提取需要的信息
    id = teacher.id
    phone = teacher.phone
    teaching_experience = teacher.teaching_experience
    evaluate = Evaluate.objects.filter(name=name).first()
    evaluate = Evaluate(name=name, id=id, teacher_phone=phone, subject=teaching_experience,content =advice)
    evaluate.save()
    data = {
        'answer': 'true'
    }
    return JsonResponse(data)