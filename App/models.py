from django.db import models

# Create your models here.

class Album(models.Model):
    album_name = models.TextField()
    artist = models.TextField()
    image = models.ImageField()
    release_year = models.CharField(max_length=4,blank=True,null=True)

    def __str__(self):
        return self.album_name
        


class Song(models.Model):
    title= models.TextField()
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, null = True)    
    audio_file = models.FileField(blank=True,null=True)
    audio_link = models.CharField(max_length=200,blank=True,null=True)
    duration=models.CharField(max_length=20)
    paginate_by = 2

    def __str__(self):
        return self.title

        