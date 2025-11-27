# from django.urls import path, include
# from django.contrib import admin

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path(''      , include('web_project.views')),
#     path('home/' , include('web_project.views')),
# ]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    #path('home/', views.home, name="about"),
    #path('hello/<str:username>', views.hello, name="hello"),
    #path('index/', views.index, name="index"),
    #path('login/', views.login, name="login"),
    path('getnames/', views.getNames, name='getNames'),
    path('getinfo/', views.getinfo, name='getInfo'),
    path('getCorrectCharacter/', views.getCorrectCharacter, name='getCorrectCharacter'),
    # path('projects/<int:id>', views.project_detail, name="project_detail"),
    # path('tasks/', views.tasks, name="tasks"),
    # path('create_task/', views.create_task, name="create_task"),
    # path('create_project/', views.create_project, name="create_project"),
]