from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('job_page/<int:myid>', views.job_page, name="job_page"),
    path('search', views.search, name="search"),
    path('add_job', views.add_job, name="add_job"),
    path('add_job_submit', views.add_job_submit, name="add_job_submit"),
    path('dashboard', views.dashboard, name = "dashboard"),
    path('edit_job/<int:myid>', views.edit_job, name="edit_job"),
    path('edit_path_submit/<int:myid>', views.edit_job_submit, name="edit_job_submit"),
    path('job_delete/<int:myid>', views.job_delete, name="job_delete"),
    path('handleLogin', views.handle_login,name="handleLogin"),
    path('handleLogout', views.handle_logout, name="handleLogout")
]