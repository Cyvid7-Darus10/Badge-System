from django.db import models
from datetime import datetime    

class Badge(models.Model):
    label = models.CharField(max_length=250)
    points = models.IntegerField()
    date = models.DateField()
    added_on = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f"{self.label} on {self.date} with {self.points} points"

class Guilder(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    added_on = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

class Claimable(models.Model):
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE, related_name="released_badge")
    code = models.CharField(max_length=50)
    release_on = models.DateTimeField()
    expires_on = models.DateTimeField()
    added_on = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f"{self.badge} | {self.code} | {self.release_on} - {self.expires_on}"

class Claimed(models.Model):
    guilder = models.ForeignKey(Guilder, on_delete=models.CASCADE, related_name="completer")
    badge = models.ForeignKey(Claimable, on_delete=models.CASCADE, related_name="claimed_badge")
    serial = models.CharField(max_length=50)
    added_on = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f"{self.guilder} | {self.badge} | {self.serial}"
