import datetime
import random

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from register.models import User
from sayt.base.helper import code_decoder
from sayt.models import OTP


class RegisView(GenericAPIView):

    def post(self, requests, *args, **kwargs):
        data = requests.data

        nott = ["first_name", "last_name", "phone", "password", 'email']
        s = ''

        for i in nott:
            if i not in data:
                s += f" {i} "

        if s:
            return Response({
                "Error": f" datada {s} polyalar to`ldirilmagan"

            })

        if len(data['phone']) != 12:
            return Response({"Error": "Telefon raqam + olib tashlaganda 12 tadan iborat bo`lishi kerak !"})

        if not data['phone'].isdigit():
            return Response({"Error": "Raqamlarni sonlarda kiritish kerak."})

        if len(data['password']) < 6:
            return Response({"Error": "Parol juda oddiy"})

        user = User.objects.create_user(
            phone=data['phone'],
            email=data['email'],
            password=data.get('password', ''),
            first_name=data.get('first_name', ''),
            last_name=data.get('password', ''),
            region=data.get('region', ''),
        )

        token = Token.objects.get_or_create(user=user)[0]

        return Response({
            "Success": token.key,
        })


class LoginView(GenericAPIView):
    def post(self, requests, *args, **kwargs):
        data = requests.data

        if data is None:
            return Response({
                "error": "data to'ldirilmagan"
            })

        # if 'email' not in data:
        #     return Response({
        #         "error": "email yo'q"
        #     })
        # if 'password' not in data:
        #     return Response({
        #         "error": "password yo'q"
        #     })
        nott = 'email' if 'email' not in data else 'password' if "password" not in data else None
        if nott:
            return Response({
                "Error": f"{nott} to`ldirilmagan"
            })
        user = User.objects.filter(email=data['email']).first()

        if not user:
            return Response({
                "Error": "Bunday foydalanuvchi afsuski yo`q."
            })
        if not user.check_password(data['password']):
            return Response({
                "Error": "Parol xato"
            })

        token = Token.objects.get_or_create(user=user)[0]

        return Response({
            "Success": token.key,
            "user": user.format()
        })


class StepOne(GenericAPIView):

    def post(self, requests, ):
        data = requests.data

        if "email" not in data:
            return Response({
                "Error": "Email kiritilmagan"
            })

        code = random.randint(100000, 999999)
        shifr = code_decoder(code)
        otp_token = OTP.objects.create(
            key=shifr,
            email=data["email"],
            state="step-one",

        )

        return Response({
            "code": code,
            "otp_token": otp_token.key,
        })


class StepTwo(GenericAPIView):
    def post(self, requests, *args, **kwargs):
        data = requests.data

        if "token" not in data:
            return Response({
                "Error": "Token kiritilmagan"
            })

        elif "code" not in data:
            return Response({
                "Error": "Code kiritilmagan"
            })

        otp = OTP.objects.filter(key=data['token']).first()


        if not otp:
            return Response({
                "Error": "bunaqa token mavjud emas"
            })

        if otp.is_expired:
            return Response({
                "Error": "Otp eskirgan"
            })

        now = datetime.datetime.now(datetime.timezone.utc)

        if (now - otp.create_at).total_seconds() >= 120:
            otp.is_expired = True
            otp.save()
            return Response({
                "Error": "Otp eskirgan ya`ni sizga berilgan 2 daqiqa tugagan"
            })

