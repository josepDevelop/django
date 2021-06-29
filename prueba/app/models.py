from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name = "Pregunta")
    pub_date = models.DateTimeField(verbose_name = "Creado")

    class Meta:
        verbose_name = "Pregunta"
        verbose_name_plural = "Preguntas"

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name = "Pregunta")
    choice_text = models.CharField(max_length=200, verbose_name = "Texto")
    votes = models.IntegerField(default=0, verbose_name = "Votos")

    class Meta:
        verbose_name = "Opción"
        verbose_name_plural = "Opciones"

    def __str__(self):
        return self.choice_text