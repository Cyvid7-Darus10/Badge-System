from django.db import models
from datetime import datetime
from django.db.models.fields import DateTimeField

class Base(models.Model):
    created = DateTimeField(default=datetime.now)
    updated = DateTimeField(default=datetime.now)
    deleted = DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True

class Badge(Base):
    label = models.CharField(max_length=250)
    points = models.IntegerField()
    url = models.CharField(max_length=250)
    date = models.DateField()

    def __str__(self):
        return f"{self.label} on {self.date} with {self.points} points"

class Guilder(Base):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=160)

    def __str__(self):
        return f"{self.id} - {self.name}"

class Claimable(Base):
    badge = models.ForeignKey(
        Badge, on_delete=models.CASCADE, related_name="released_badge")
    code = models.CharField(max_length=50)
    release_on = models.DateTimeField()
    expires_on = models.DateTimeField()

    def __str__(self):
        return f"{self.badge} | {self.code} | {self.release_on} - {self.expires_on}"

class Claimed(Base):
    guilder = models.ForeignKey(
        Guilder, on_delete=models.CASCADE, related_name="completer")
    badge = models.ForeignKey(
        Claimable, on_delete=models.CASCADE, related_name="claimed_badge")
    serial = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.guilder} | {self.badge} | {self.serial}"
