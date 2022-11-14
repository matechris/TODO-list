from django.urls import path

from organizer.views import (
    TaskListView, TagListView, TaskCreateView,
    TaskUpdateView, TaskDeleteView, TagCreateView,
    TagUpdateView, TagDeleteView,
    mark_task_as_done,
    mark_task_as_not_done,
)

urlpatterns = [
    path(
        "",
        TaskListView.as_view(),
        name="task-list"
    ),
    path(
        "tags/",
        TagListView.as_view(),
        name="tag-list"
    ),
    path(
        "tasks/create/",
        TaskCreateView.as_view(),
        name="task-create"
    ),
    path(
        "tasks/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "tasks/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path(
        "tags/create/",
        TagCreateView.as_view(),
        name="tag-create"
    ),
    path(
        "tags/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag-update"
    ),
    path(
        "tags/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tag-delete"
    ),
    path(
        "tasks/<int:pk>/mark_as_done",
        mark_task_as_done,
        name="mark-as-done",
    ),
    path(
        "tasks/<int:pk>/mark_as_not_done",
        mark_task_as_not_done,
        name="mark-as-not-done",
    ),
]

app_name = "organizer"
