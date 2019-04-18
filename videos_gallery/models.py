from django.db import models




class Artical(models.Model):
    video_name=models.CharField(max_length=100)
    video_link = models.CharField(max_length=200)
    image=models.FileField()
    # video_link=models.CharField(max_length=200, default="https://www.youtube.com/embed/")
    posted_on=models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.video_name