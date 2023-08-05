from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', TaskList.as_view(), name='task_list'),
    path('login/', CustomLoginView.as_view(), name='login-page'),
    path('logout/', LogoutView.as_view(next_page='login-page'), name='logout-page'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('create/', TaskCreate.as_view(), name='task-create'),
    path('edit/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
]
