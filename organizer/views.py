from django.shortcuts import render
from django.views import generic

from organizer.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task


class TagListView(generic.ListView):
    model = Tag
