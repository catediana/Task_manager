from django.urls import path, include
from . import views, api # Import api_views as api

urlpatterns = [
    path("", views.home, name="home"),  # Public landing page
    path("register/", views.register_view, name="register"), # Registration page
    path("login/", views.login_view, name="login"), # Login page
    path("logout/", views.logout_view, name="logout"),

    # API Endpoints
    path("api/register/", api.RegisterAPIView.as_view(), name="api_register"),
    path("api/login/", api.LoginAPIView.as_view(), name="api_login"),
    path("api/user-profile/", api.user_profile_api, name="api_user_profile"),

    # Authenticated pages (placeholders for now)
    path('dashboard/', views.dashboard, name='dashboard'),
    path('onboarding/', views.onboarding, name='onboarding'),

    path('tasks/', views.task_list, name='task_list'),
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
