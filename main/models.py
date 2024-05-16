from django.db import models

class Todo(models.Model):
    name = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now_add=True)
    create_at= models.DateTimeField(auto_now=True)


class Item(models.Model):
    updated_at = models.DateTimeField(auto_now_add=True)
    create_at = models.DateTimeField(auto_now=True)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name="items")
    text = models.TextField()
    complete = models.BooleanField(default=False)

def __str__(self):
    return f"{self.id} | {self.text}"