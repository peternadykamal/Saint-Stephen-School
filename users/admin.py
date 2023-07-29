from django.contrib import admin

import users.models as models

admin.site.register(models.Profile)
admin.site.register(models.Address)
admin.site.register(models.TalmzaLevel)
admin.site.register(models.SchoolLevel)
admin.site.register(models.MasreefProfileForm)
admin.site.register(models.ProfileFormLog)
