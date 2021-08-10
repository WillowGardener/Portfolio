from django.db import models

class Card(models.Model):
    name = models.CharField(max_length=50, null=True)
    text = models.TextField(default="", null=True)

    # def __str__(self):
    #     return self.name

class Link(models.Model):
    text = models.TextField()
    card = models.ForeignKey(Card,default=None, on_delete=models.CASCADE)
    # def __str__(self):
    #     return self.text


    