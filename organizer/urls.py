from django.urls import path

from organizer.views import TaskListView

urlpatterns = [
    path(
        "",
        TaskListView.as_view(),
        name="task-list"
    )
]

app_name = "organizer"
