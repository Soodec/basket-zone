from django.contrib import admin
from .models import Tournament, Team, Participant, Registration, Match

class TournamentAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ciudad', 'estado', 'fecha_inicio', 'fecha_fin', 'status')
    list_filter = ('status', 'estado')
    search_fields = ('nombre', 'ciudad', 'estado')

class TeamAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ciudad', 'estado')
    search_fields = ('nombre', 'ciudad', 'estado')

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'equipo')
    search_fields = ('nombre', 'equipo__nombre')

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('torneo', 'equipo', 'responsable_nombre', 'status', 'fecha_registro')
    list_filter = ('status', 'torneo')
    search_fields = ('equipo__nombre', 'responsable_nombre', 'responsable_email')

class MatchAdmin(admin.ModelAdmin):
    list_display = ('torneo', 'equipo_a', 'equipo_b', 'fecha_hora', 'status')
    list_filter = ('torneo', 'status')

admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Match, MatchAdmin)
