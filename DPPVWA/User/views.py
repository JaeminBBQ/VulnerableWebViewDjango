from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from secrets import token_hex
from django.db import connection


# Create your views here.


def index(request):
    return render(request, "User/index.html")

def register(request):
    return render(request, "User/register.html")

def passwords(request):
    return render(request, "User/passwords.html")

@api_view(['POST'])
def registerAPI(request):
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    username = request.POST["username"]
    password = request.POST["password"]

    with connection.cursor() as cursor:
        cursor.execute(f"""
                INSERT INTO User_app_user (username, password, first_name, last_name)
                VALUES ('{username}', '{password}', '{first_name}', '{last_name}');
            """)
        # rows = cursor.fetchall()

    return JsonResponse({"Status":0})

@api_view(['POST'])
def loginAPI(request):
    username = request.POST["username"]
    password = request.POST["password"]

    with connection.cursor() as cursor:
        cursor.execute(f"""
                SELECT * FROM User_app_user
                WHERE username='{username}';
            """)
        rows = cursor.fetchall()
        user_info = rows[0]

        if user_info[2] == password:
            token = token_hex(10)
            cursor.execute(f"""
                UPDATE User_app_user
                SET token = '{token}'
                WHERE username='{username}';
            """)
            return JsonResponse({"Status":token})
        else:
            return JsonResponse({"Status":1})

@api_view(['POST'])
def add_passwordAPI(request):
    website = request.POST["website"]
    username = request.POST["username"]
    password = request.POST["password"]
    token = request.POST["token"]

    with connection.cursor() as cursor:
        cursor.execute(f"""
                SELECT * FROM User_app_user
                WHERE token='{token}';
            """)
        rows = cursor.fetchall()
        relation_id = rows[0][0]
        cursor.execute(f"""
                INSERT INTO User_passwords (website, username, password, relation_id)
                VALUES ('{website}', '{username}', '{password}', '{relation_id}');
            """)
    
    return JsonResponse({"Status":0})

@api_view(['POST'])
def get_passwordAPI(request):
    token = request.POST["token"]

    with connection.cursor() as cursor:
        cursor.execute(f"""
                SELECT * FROM User_app_user
                WHERE token='{token}';
            """)
        rows = cursor.fetchall()
        relation_id = rows[0][0]
        cursor.execute(f"""
                SELECT * FROM User_passwords
                WHERE relation_id='{relation_id}';
            """)
        rows = cursor.fetchall()
    
    return JsonResponse({"Status":rows})

@api_view(['POST'])
def search_passwordAPI(request):
    search = request.POST["search"]
    token = request.POST["token"]

    with connection.cursor() as cursor:
        cursor.execute(f"""
                SELECT * FROM User_app_user
                WHERE token='{token}';
            """)
        rows = cursor.fetchall()
        relation_id = rows[0][0]
        if search:
            cursor.execute(f"""
                    SELECT * FROM User_passwords
                    WHERE relation_id='{relation_id}' AND website LIKE '{search}';
                """)
        else:
            cursor.execute(f"""
                SELECT * FROM User_passwords
                WHERE relation_id='{relation_id}';
            """)
        rows = cursor.fetchall()
    
    return JsonResponse({"Status":rows})

