from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView


# from webapp.views import IndexView, TaskView, TaskUpdateView, TaskDeleteView, TypeView, TypeCreateView, \
#     TypeUpdateView, TypeDeleteView, StatusView, StatusCreateView, StatusUpdateView, StatusDeleteView
# from webapp.views.project_views import ProjectsListView, ProjectView, ProjectCreateView, ProjectUpdateView, \
#     ProjectDeleteView, ProjectsDelete
# from webapp.views.status_views import StatusDelete
# from webapp.views.task_views import TasksDelete, TaskForProjectCreateView
# from webapp.views.type_views import TypeDelete
from webapp.views import IndexView, PhotoView, PhotoCreateView, PhotoUpdateView, PhotoDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('photo/<int:pk>/', PhotoView.as_view(), name='photo_view'),
    path('photo/add/', PhotoCreateView.as_view(), name='photo_create'),
    path('photo/<int:pk>/edit/', PhotoUpdateView.as_view(), name='photo_update'),
    path('photo/<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo_delete'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # path('massdelete/', TasksDelete.as_view(), name='mass_delete'),
    # path('types/', TypeView.as_view(), name='types_view'),
    # path('types/add/', TypeCreateView.as_view(), name='type_create'),
    # path('types/<int:pk>/edit/', TypeUpdateView.as_view(), name='type_update'),
    # path('types/<int:pk>/delete/', TypeDeleteView.as_view(), name='type_delete'),
    # path('massdeletetypes/', TypeDelete.as_view(), name='mass_delete_types'),
    # path('statuses/', StatusView.as_view(), name='status_view'),
    # path('status/add/', StatusCreateView.as_view(), name='status_create'),
    # path('status/<int:pk>/edit/', StatusUpdateView.as_view(), name='status_update'),
    # path('status/<int:pk>/delete/', StatusDeleteView.as_view(), name='status_delete'),
    # path('massdeletestatus/', StatusDelete.as_view(), name='mass_delete_status'),
    # path('projects/', ProjectsListView.as_view(), name='projects_view'),
    # path('project/<int:pk>/', ProjectView.as_view(), name='project_view'),

    # path('project/add/', ProjectCreateView.as_view(), name='project_create'),
    # path('project/<int:pk>/edit/', ProjectUpdateView.as_view(), name='project_update'),
    # path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    # path('massdeleteprojects/', ProjectsDelete.as_view(), name='mass_delete_projects'),
]

app_name = 'webapp'