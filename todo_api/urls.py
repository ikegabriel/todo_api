from django.urls import path
from . import views
urlpatterns = [
    path('todos/', views.TodoListAPIView.as_view(), name='todos_list'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('create/', views.TodoCreateView.as_view(), name='create'),
    path('update/<int:id>/', views.TodoUpdateView.as_view(), name='update'),
    path('detail/<int:id>/', views.TodoDetailView.as_view(), name='detail'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('complete/<int:id>/', views.complete, name='complete'),

]
