from django.db import models

class Torrents(models.Model):
    choice = [
        ('Torrent', 'Torrent'),
        ('Filme', 'Filme'),
        ('Serie', 'Serie'),
        ('Arquivo', 'Arquivo'),
        ('Jogo', 'Jogo')
    ]

    nome = models.CharField(max_length=100, blank=False)
    magnet = models.TextField(blank=False)
    type = models.CharField(
        max_length=7,
        choices=choice,
        default=choice
    )
