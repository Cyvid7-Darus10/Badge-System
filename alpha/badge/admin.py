from django.contrib import admin
from .models import Badge, Guilder, Claimable, Claimed

admin.site.register(Badge)
admin.site.register(Guilder)
admin.site.register(Claimable)
admin.site.register(Claimed)