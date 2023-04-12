from django.urls import path

from api.v1.category.views import CategoryView
from api.v1.subctg.views import SubCtgView

urlpatterns = [
    path('category/', CategoryView.as_view()),
    path('category/<int:pk>/', CategoryView.as_view()),
    path('subctg/', SubCtgView.as_view()),
    path('subctg/<int:pk>/',SubCtgView.as_view()),


]