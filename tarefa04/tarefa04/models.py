from django.db import models

class Missão (models.Model):
    nome = models.CharField(max_length=200)
    status = models.BooleanField()
    prazo = models.DateField()

    class Meta:
        verbose_name = "Missão"
        verbose_name_plural = "Missões"


    def __str__(self):
         if self.status:
            status = "Missão concluída 😊💯"
         else: 
            status="Missão pendente 🥲❌"
         return f"Nome: {self.nome} | Status: {status} | Prazo: {self.prazo}"
