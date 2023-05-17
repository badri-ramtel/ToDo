from django.db import models
from django.contrib.auth.models import User

# Create your models here.   
# class User(models.Model):
#     first_name = models.CharField(max_length=25)
#     last_name = models.CharField(max_length=25)
#     email = models.EmailField()
#     username = models.CharField(max_length=25)
#     password = models.CharField(max_length=25)

#     def __str__(self):
#         return f'{self.first_name}'
    
#     class Meta:
#         db_table = 'user'

# class LogIn(models.Model):
#     username = models.CharField(max_length=25)
#     password = models.CharField(max_length=25)
#     user = models.OneToOneField(User, on_delete=models.CASCADE, default='NA')

#     # def __str__(self):
#     #     return f'{self.username}'
    
#     class Meta:
#         db_table = 'login'
#         # verbose_value_plural = 'login'

    

class ToDo(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    is_completed = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        db_table = 'todo'
        verbose_name_plural = 'todo'
        ordering = ['updated_date']



