from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="product-home-page"),
    path('create',views.create,name="product-create-page"),
    path('edit/<int:pk>',views.edit,name="product-edit-page"),
    path('dele/<str:name>',views.dele,name="product-delete-page"),
    path('api/single/<int:id>',views.apiGetSingleProduct,name="product-api-page"),
    path('api/plural/<str:str>',views.apiGetMultipleProduct,name="all-product-api-page"),
]