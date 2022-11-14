from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from organizer.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")


class TaskCreateView(generic.CreateView):
    model = Task
    fields = ["content", "deadline", "tags"]
    success_url = reverse_lazy("organizer:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = ["content", "deadline", "tags"]
    success_url = reverse_lazy("organizer:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("organizer:task-list")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("organizer:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("organizer:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("organizer:tag-list")


def mark_task_as_done(request, pk):
    task = Task.objects.get(id=pk)
    if not task.is_done:
        task.is_done = True
    task.save()
    return HttpResponseRedirect(
        reverse_lazy("organizer:task-list")
    )


def mark_task_as_not_done(request, pk):
    task = Task.objects.get(id=pk)
    if task.is_done:
        task.is_done = False
    task.save()
    return HttpResponseRedirect(
        reverse_lazy("organizer:task-list")
    )
