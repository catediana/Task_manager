from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="user_login"),
    path("logout/", views.user_logout, name="user_logout"),
    path('', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),
    path('task/<int:task_id>/detail/', views.task_detail, name='task_detail'),
    path('task/<int:task_id>/update/', views.update_task, name='update_task'),
    path('task/<int:task_id>/delete/', views.delete_task, name='delete_task'),
    path('task/<int:task_id>/add-comment/', views.add_comment, name='add_comment'),
    path('task/<int:task_id>/archive/', views.archive_task, name='archive_task'),
    path('task/<int:task_id>/unarchive/', views.unarchive_task, name='unarchive_task'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/add/', views.add_category, name='add_category'),
    path('categories/update/<int:category_id>/', views.category_update, name='category_update'),
    path('categories/delete/<int:category_id>/', views.category_delete, name='category_delete'),
    path('ajax/update-status/', views.update_task_status_ajax, name='update_task_status_ajax'),
    path('ajax/reorder-tasks/', views.reorder_tasks_ajax, name='reorder_tasks_ajax'),
    path('task/<int:task_id>/add-subtask/', views.add_subtask, name='add_subtask'),
    path('subtask/toggle/<int:subtask_id>/', views.toggle_subtask_complete, name='toggle_subtask_complete'),
    path('subtask/delete/<int:subtask_id>/', views.delete_subtask, name='delete_subtask'),
    path('profile/', views.profile_settings, name='profile_settings'),
]
