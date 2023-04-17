import random
import uuid
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


class StepOne(GenericAPIView):

    def post(self, requests):

        data = requests.data

        if "tel" not in data:
            return Response({
                "Error": "Tel kirgizilmagan"
            })



        parol = random.randint(100000, 999999)
        token = uuid.uuid4().__str__() + (parol) + uuid.uuid4().__str__()

        return Response({
            "parol": parol,
            "token": token
        })



