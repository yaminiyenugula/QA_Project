from django.db import models
# Create your models here.



class Options(models.Model):
    option = models.TextField(max_length=250)
    is_true = models.BooleanField(default=False)
    is_selected = models.BooleanField(default=False)

 
    def __str__(self):
        return self.option

class Questions(models.Model):
    question = models.TextField(max_length=250)
    correctOption=models.ForeignKey(
        Options,
        on_delete=models.SET_NULL,
        null=True,
        related_name='correct_question'
    )
    options = models.ManyToManyField(
        Options,
        blank=True,
        related_name='question_options'
    )

    def __str__(self):
        return self.question