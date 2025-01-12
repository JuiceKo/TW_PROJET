from django.db import models
from django.contrib.auth.models import User


# Modèle pour les canaux de discussion
class Channel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)  # La description peut être optionnelle
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Modèle pour les groupes
class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)  # La description peut être optionnelle
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Modèle pour les amis
class Friend(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Modèle pour les messages (lié aux canaux ou aux groupes)
class Message(models.Model):
    channel = models.ForeignKey(
        Channel, on_delete=models.CASCADE, related_name='messages', blank=True, null=True
    )  # Les messages peuvent être associés à un canal
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name='messages', blank=True, null=True
    )  # Ou bien à un groupe
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Affiche le contenu et le nom du groupe ou canal
        if self.channel:
            return f"[Canal: {self.channel.name}] {self.sender.username}: {self.content[:20]}"
        elif self.group:
            return f"[Groupe: {self.group.name}] {self.sender.username}: {self.content[:20]}"
        return f"{self.sender.username}: {self.content[:20]}"



class Emoji(models.Model):
    name = models.CharField(max_length=100)  # Nom de l'emoji, ex : "sourire"
    symbol = models.CharField(max_length=10)  # Symbole de l'emoji, ex : "😊"
    category = models.CharField(max_length=50)  # Catégorie, ex : "smileys"

    def __str__(self):
        return f"{self.symbol} ({self.name})"
    
