from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('about/history/', views.history, name='history'),

    path('about/vision-mission/', views.vision, name='vision'),

    path('about/principal/', views.principal_page, name='principal'),

    path('about/facilities/', views.facilities, name='facilities'),

    path('academics/intermediate/', views.intermediate, name='intermediate'),
    path('academics/adp/', views.adp, name='adp'),
    path('academics/bs/', views.bs, name='bs'),
    path('academics/departments/', views.departments_page, name='departments_page'),
    path('faculty/', views.faculty, name='faculty'),
    path('downloads/', views.downloads, name='downloads'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('notices/', views.notices, name='notices'),
    path('academic-calendar/', views.academic_calendar, name='academic_calendar'),
    path('departments/<str:slug>/', views.department_detail, name='department_detail'),
    path('news/admissions-2026/', views.news_admissions, name='news_admissions'),
    path('news/academic-calendar/', views.news_calendar, name='news_calendar'),
    path('news/college-event/', views.news_event, name='news_event'),

]