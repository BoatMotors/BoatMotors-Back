from django.urls import path

from api.v1.category.views import CategoryView

urlpatterns = [
    path('category/', CategoryView.as_view()),
    path('category/<int:pk>/', CategoryView.as_view()),

]