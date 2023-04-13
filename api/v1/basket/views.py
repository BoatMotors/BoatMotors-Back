from django.shortcuts import redirect
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from register.models import User
from sayt.models import Product


class BasketView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def post(self, requests, *args, **kwargs):
        data = requests.data



        if not User:
            return Response({
                "Error": "Siz ro`yxatdan o`tmagansiz"
            })



        if 'pro_id' not in data:
            return Response({
                "Error": "id topilmadi"
            })

        product = Product.objects.filter(pk="pro_id")


        return Response("natija")

