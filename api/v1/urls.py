from django.urls import path

from api.v1.auth.views import RegisView, StepOne, StepTwo
from api.v1.category.views import CategoryView
from api.v1.product.views import ProductView
from api.v1.subctg.views import SubCtgView
from api.v1.basket.views import BasketView
from api.v1.auth.viewsss import StepOne

urlpatterns = [
    path('category/', CategoryView.as_view()),
    path('category/<int:pk>/', CategoryView.as_view()),
    path('subctg/', SubCtgView.as_view()),
    path('subctg/<int:pk>/',SubCtgView.as_view()),
    # path('register/', RegisView.as_view()),

    path('product/', ProductView.as_view()),
    path('product/<int:pk>/', ProductView.as_view()),

    path('product/s/<int:sub>/', ProductView.as_view()),
    path('product/c/<int:ctg>/', ProductView.as_view()),


    path("add_pro/<int:pk>/", BasketView.as_view()),

    path('stepone/', StepOne.as_view()),
    path('steptwo/', StepTwo.as_view()),

]