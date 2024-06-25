from django.urls import path

from cats.views import cat_list, cat_add_many, cat_update
from cats.views import APICat, APICatDetail, CatList, CatDetail

urlpatterns = [
   path('cats/', CatList.as_view()),
   path('cats/add_many/', cat_add_many),
   path('cats/<int:pk>/', APICatDetail.as_view())
]
