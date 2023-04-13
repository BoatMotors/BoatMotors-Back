from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

# ctg bn, sub_ctg, product bn
from sayt.base.format import productFormat, subctgFormat
from sayt.models import Sub_ctg, Category, Product


class ProductView(GenericAPIView):

    def get(self, requests, sub=None, ctg=None, pk=None, *args, **kwargs):

        if ctg:
            ctg_one = Category.objects.filter(pk=ctg).first()

            if not ctg_one:
                return Response({
                    "Error": "Bunaqa id li ctg topilmadi"
                })

            prod = Product.objects.filter(pk=ctg)
            l = []

            for i in prod:
                l.append(productFormat(i))

            return Response({
                "result": l
            })


        elif sub:

            subcategory = Sub_ctg.objects.filter(pk=sub).first()

            if not subcategory:
                return Response({
                    "Error": "Bunaqa id li subctg topilmadi"
                })

            subprod = Product.objects.filter(pk=sub)

            l = []
            for i in subprod:
                l.append(productFormat(i))

            return Response({
                "result": l
            })


        elif pk:
            product = Product.objects.filter(pk=pk).first()

            return Response({
                "result": product
            })
        else:
            return Response({
                "Error": "Kerakli malumotlar berilmadi"
            })
