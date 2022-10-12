from django.urls import path
from todolist.views import delete_task, register_account, user_login, user_logout, show_todolist, create_task, change_status, delete_task, show_json, add_task_ajax, delete_task_ajax

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register_account, name='register_account'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('create-task/', create_task, name='create_task'),
    path('change-status/', change_status, name='change_status'),
    path('delete-task/', delete_task, name='delete_task'),
    path('json/', show_json, name='show_json'),
    path('add/', add_task_ajax, name='add_task_ajax'),
    path('delete/<int:id>', delete_task_ajax, name='delete_task_ajax'),
]