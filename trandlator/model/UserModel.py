from django.db import models

class UserItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        app_label = 'model'  # UserItem 모델이 속한 앱 이름
    def __str__(self):
        return self.name