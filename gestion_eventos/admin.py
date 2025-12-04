
from django.contrib import admin
from .models import Evento, Participante, Ticket, Agenda_Evento, Patrocinador, Evento_Patrocinador, Feedback_Evento

class EventoAdmin(admin.ModelAdmin):
    search_fields = ['nombre_evento']

class ParticipanteAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'apellido']

class PatrocinadorAdmin(admin.ModelAdmin):
    search_fields = ['nombre_patrocinador']

class TicketAdmin(admin.ModelAdmin):
    autocomplete_fields = ['id_evento', 'id_participante']

class AgendaEventoAdmin(admin.ModelAdmin):
    autocomplete_fields = ['id_evento']

class EventoPatrocinadorAdmin(admin.ModelAdmin):
    autocomplete_fields = ['id_evento', 'id_patrocinador']

class FeedbackEventoAdmin(admin.ModelAdmin):
    autocomplete_fields = ['id_evento', 'id_participante']

admin.site.register(Evento, EventoAdmin)
admin.site.register(Participante, ParticipanteAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Agenda_Evento, AgendaEventoAdmin)
admin.site.register(Patrocinador, PatrocinadorAdmin)
admin.site.register(Evento_Patrocinador, EventoPatrocinadorAdmin)
admin.site.register(Feedback_Evento, FeedbackEventoAdmin)
