# from rest_framework.generics import GenericAPIView
# from rest_framework.response import Response
#
#
# class BasketView(GenericAPIView):
#     def get(self,requests, user, product,  *args, **kwargs):
#         data = requests.data
#
#         if product not in data:
#             return Response({
#                 "Error": "Product id berilmagan"
#             })
#
#         if product:
