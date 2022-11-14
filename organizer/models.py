from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, default="")
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(
        to=Tag, related_name="tasks"
    )

    class Meta:
        ordering = ["is_done", "created_at"]
