from django.shortcuts import redirect
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from register.models import User
from sayt.base.format import basketFormat
from sayt.models import Product, Basket


class BasketView(GenericAPIView):
    authentication_classes = TokenAuthentication,
    permission_classes = IsAuthenticated,

    def post(self, requests, *args, **kwargs):
        data = requests.data

        if "prod_id" not in data:
            return Response({
                "Error": "Prod id berilmagan"
            })

        prod = Product.objects.filter(pk=data['prod_id']).first()

        if prod:
            baskett = Basket.objects.get_or_create(
                user=requests.user,
                product=prod,
            )[0]

            baskett.quantity = data.get('quantity', baskett.quantity)
            baskett.save()

            return Response({
                "result": basketFormat(baskett)
            })

        else:
            return Response({
                "Error": "Noto'gri prod berilgan"
            })
    # def get(self,request, *args, **kwargs):
    #     print('bu requests', request)
    #     print(request.user.id)
    #     # data = request.query_params
    #     # print('bu data',data)
    #     # user = data['Authorization']
    #     # print('bu user',user)
    #     # print(user.id)
    #     l = []
    #     try:
    #
    #         for i in Basket.objects.filter(user_id=user):
    #             l.append(basketFormat(i))
    #     except:
    #         l='Bu user da maxsulot yo\'q'
    #
    #     return Response({'data':l})
    #     # print(user)
    #     # if pk:
    #     #     basket = Basket.objects.filter(pk=pk, user_id=user).first()
    #     #     return Response({"data": basketFormat(basket)})
    #
    #
