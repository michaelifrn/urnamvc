from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=32, default='')
    number = models.IntegerField(primary_key = True, default=0)

    def __str__(self):
        return f'Candidato: {self.name}'


class Votes(models.Model):
    name = models.ForeignKey(Candidate, on_delete= models.DO_NOTHING)
    number = models.IntegerField(default= 0)
