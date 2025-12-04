
from django.urls import path
from .views import (
    HomeView,
    EventoListView, EventoCreateView, EventoUpdateView, EventoDeleteView,
    ParticipanteListView, ParticipanteCreateView, ParticipanteUpdateView, ParticipanteDeleteView,
    TicketListView, TicketCreateView, TicketUpdateView, TicketDeleteView,
    AgendaEventoListView, AgendaEventoCreateView, AgendaEventoUpdateView, AgendaEventoDeleteView,
    PatrocinadorListView, PatrocinadorCreateView, PatrocinadorUpdateView, PatrocinadorDeleteView,
    EventoPatrocinadorListView, EventoPatrocinadorCreateView, EventoPatrocinadorUpdateView, EventoPatrocinadorDeleteView,
    FeedbackEventoListView, FeedbackEventoCreateView, FeedbackEventoUpdateView, FeedbackEventoDeleteView
)

urlpatterns = [
    # Ruta para la página de inicio
    path('', HomeView.as_view(), name='home'),

    # Rutas para Evento
    path('eventos/', EventoListView.as_view(), name='evento_list'),
    path('eventos/crear/', EventoCreateView.as_view(), name='evento_crear'),
    path('eventos/<int:pk>/editar/', EventoUpdateView.as_view(), name='evento_editar'),
    path('eventos/<int:pk>/eliminar/', EventoDeleteView.as_view(), name='evento_eliminar'),

    # Rutas para Participante
    path('participantes/', ParticipanteListView.as_view(), name='participante_list'),
    path('participantes/crear/', ParticipanteCreateView.as_view(), name='participante_crear'),
    path('participantes/<int:pk>/editar/', ParticipanteUpdateView.as_view(), name='participante_editar'),
    path('participantes/<int:pk>/eliminar/', ParticipanteDeleteView.as_view(), name='participante_eliminar'),

    # Rutas para Ticket
    path('tickets/', TicketListView.as_view(), name='ticket_list'),
    path('tickets/crear/', TicketCreateView.as_view(), name='ticket_crear'),
    path('tickets/<int:pk>/editar/', TicketUpdateView.as_view(), name='ticket_editar'),
    path('tickets/<int:pk>/eliminar/', TicketDeleteView.as_view(), name='ticket_eliminar'),

    # Rutas para Agenda_Evento
    path('agenda/', AgendaEventoListView.as_view(), name='agenda_evento_list'),
    path('agenda/crear/', AgendaEventoCreateView.as_view(), name='agenda_evento_crear'),
    path('agenda/<int:pk>/editar/', AgendaEventoUpdateView.as_view(), name='agenda_evento_editar'),
    path('agenda/<int:pk>/eliminar/', AgendaEventoDeleteView.as_view(), name='agenda_evento_eliminar'),

    # Rutas para Patrocinador
    path('patrocinadores/', PatrocinadorListView.as_view(), name='patrocinador_list'),
    path('patrocinadores/crear/', PatrocinadorCreateView.as_view(), name='patrocinador_crear'),
    path('patrocinadores/<int:pk>/editar/', PatrocinadorUpdateView.as_view(), name='patrocinador_editar'),
    path('patrocinadores/<int:pk>/eliminar/', PatrocinadorDeleteView.as_view(), name='patrocinador_eliminar'),

    # Rutas para Evento_Patrocinador
    path('evento-patrocinador/', EventoPatrocinadorListView.as_view(), name='evento_patrocinador_list'),
    path('evento-patrocinador/crear/', EventoPatrocinadorCreateView.as_view(), name='evento_patrocinador_crear'),
    path('evento-patrocinador/<int:pk>/editar/', EventoPatrocinadorUpdateView.as_view(), name='evento_patrocinador_editar'),
    path('evento-patrocinador/<int:pk>/eliminar/', EventoPatrocinadorDeleteView.as_view(), name='evento_patrocinador_eliminar'),

    # Rutas para Feedback_Evento
    path('feedback/', FeedbackEventoListView.as_view(), name='feedback_evento_list'),
    path('feedback/crear/', FeedbackEventoCreateView.as_view(), name='feedback_evento_crear'),
    path('feedback/<int:pk>/editar/', FeedbackEventoUpdateView.as_view(), name='feedback_evento_editar'),
    path('feedback/<int:pk>/eliminar/', FeedbackEventoDeleteView.as_view(), name='feedback_evento_eliminar'),
]
