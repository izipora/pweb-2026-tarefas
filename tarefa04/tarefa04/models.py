from django.db import models

class Missão (models.Model):
    nome = models.CharField(max_length=200)
    status = models.BooleanField()
    prazo = models.DateField()

    def __str__(self):
         if self.status:
            status = "Missão concluída 😊💯"
         else: 
            "Missão pendente 🥲❌"
         return f"Nome: {self.nome} | Status: {status} | Prazo: {self.prazo}"
