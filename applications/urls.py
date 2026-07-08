from django.urls import path
from . import views

app_name = "applications"

urlpatterns = [
    path("til/<str:code>/", views.set_lang, name="set_lang"),
    path("ariza/topshirish/", views.application_create_view, name="create"),
    path("ariza/mening/", views.my_application_view, name="my"),
    path("chek/<str:code>/", views.receipt_view, name="receipt"),
    path("tekshirish/<str:code>/", views.verify_view, name="verify"),
]
