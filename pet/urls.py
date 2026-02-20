from django.urls import path, include
from .views import *

app_name = "pet"

urlpatterns = [
    path("", index, name="index"),
    path("pet_detail/<pk>", PetDetail.as_view(), name="pet_detail"),
    # 领养申请提交路由
    path('apply/', submit_adoption_application, name='submit_adoption'),

    path('my_pets/', UserAdoptedPetListView.as_view(), name='my_adopted_pets'),
    path('all_pet/', PetListView.as_view(), name='all_pet'),
    path('pets/<int:pet_id>/upload_photo/', PetPhotoUploadView.as_view(), name='pet_photo_upload'),
]
