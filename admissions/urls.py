from django.urls import path
from . import views

urlpatterns = [

    path('', views.admission_portal, name='admission_portal'),

    path('register/', views.register, name='register'),

    path('login/', views.login_user, name='login'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('apply/adp/', views.adp_apply, name='adp_apply'),
    path('logout/', views.logout_user, name='logout'),
    path('opening-soon/', views.opening_soon, name='opening_soon'),
    path(
    "my-application/",
    views.my_application,
    name="my_application",
),
path("fee-voucher/", views.fee_voucher, name="fee_voucher"),
path("merit-list/", views.merit_list, name="merit_list"),

]