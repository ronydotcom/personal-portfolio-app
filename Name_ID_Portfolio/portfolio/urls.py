from django.urls import path
from portfolio.views import *

urlpatterns=[
    path('',register_page,name='register_page'),
    path('login/',login_page,name='login_page'),
    path('logout/',logout_page,name='logout_page'),

    path('dashboard/',dashboard_page,name='dashboard_page'),

    path('profile/',profile_page,name='profile_page'),

    path('resume/',resume_page,name='resume_page'),

    path('projects/',project_page,name='project_page'),
    path('add-project/',add_project_page,name='add_project_page'),
    path('update-project/<int:id>/',update_project_page,name='update_project_page'),
    path('delete-project/<int:id>/',delete_project_page,name='delete_project_page'),

    path('skills/',skill_page,name='skill_page'),
    path('add-skill/',add_skill_page,name='add_skill_page'),
    path('update-skill/<int:id>/',update_skill_page,name='update_skill_page'),
    path('delete-skill/<int:id>/',delete_skill_page,name='delete_skill_page'),

    path('education/',education_page,name='education_page'),
    path('add-education/',add_education_page,name='add_education_page'),
    path('update-education/<int:id>/',update_education_page,name='update_education_page'),
    path('delete-education/<int:id>/',delete_education_page,name='delete_education_page'),

    path('experience/',experience_page,name='experience_page'),
    path('add-experience/',add_experience_page,name='add_experience_page'),
    path('update-experience/<int:id>/',update_experience_page,name='update_experience_page'),
    path('delete-experience/<int:id>/',delete_experience_page,name='delete_experience_page'),

    path('contact/',contact_page,name='contact_page'),
]