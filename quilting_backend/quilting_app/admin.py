from django.contrib import admin

from .models import Tutorial, TutorialStep, User


class TutorialStepInline(admin.TabularInline):
    model = TutorialStep


class TutorialAdmin(admin.ModelAdmin):
    inlines = [
        TutorialStepInline,
    ]


admin.site.register(Tutorial, TutorialAdmin)
admin.site.register(User)
