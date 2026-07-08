from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("royxatdan-otish/", views.register_view, name="register"),
    path("kirish/", views.CustomLoginView.as_view(), name="login"),
    path("chiqish/", views.logout_view, name="logout"),
    path("profil/", views.profile_view, name="profile"),
    path("profil/tahrirlash/", views.profile_edit_view, name="profile_edit"),
]
