from django.db import models

class Torrents(models.Model):
    choice = [
        ('to', 'Torrent')
    ]

    nome = models.CharField(max_length=100, blank=False)
    magnet = models.TextField(blank=False)
    type = models.CharField(
        max_length=2,
        choices=choice,
        default=choice
    )
