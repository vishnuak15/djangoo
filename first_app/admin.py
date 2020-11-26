from django.contrib import admin
from first_app.models import Entity,Program,UserProfileInfo
#,Topic,Grid,HighLevelActors,HighLevelFunctions,Actor,Funtions,Combination

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Entity)
admin.site.register(Program)