
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Evento, Participante, Ticket, Agenda_Evento, Patrocinador, Evento_Patrocinador, Feedback_Evento
from .forms import EventoForm, ParticipanteForm, TicketForm, AgendaEventoForm, PatrocinadorForm, EventoPatrocinadorForm, FeedbackEventoForm

# Vista para la página de inicio
class HomeView(TemplateView):
    template_name = 'gestion_eventos/home.html'

# Vistas para Evento
class EventoListView(ListView):
    model = Evento
    template_name = 'gestion_eventos/evento_list.html'
    paginate_by = 10

class EventoCreateView(CreateView):
    model = Evento
    form_class = EventoForm
    template_name = 'gestion_eventos/evento_form.html'
    success_url = reverse_lazy('evento_list')

class EventoUpdateView(UpdateView):
    model = Evento
    form_class = EventoForm
    template_name = 'gestion_eventos/evento_form.html'
    success_url = reverse_lazy('evento_list')

class EventoDeleteView(DeleteView):
    model = Evento
    template_name = 'gestion_eventos/evento_confirm_delete.html'
    success_url = reverse_lazy('evento_list')

# Vistas para Participante
class ParticipanteListView(ListView):
    model = Participante
    template_name = 'gestion_eventos/participante_list.html'
    paginate_by = 10

class ParticipanteCreateView(CreateView):
    model = Participante
    form_class = ParticipanteForm
    template_name = 'gestion_eventos/participante_form.html'
    success_url = reverse_lazy('participante_list')

class ParticipanteUpdateView(UpdateView):
    model = Participante
    form_class = ParticipanteForm
    template_name = 'gestion_eventos/participante_form.html'
    success_url = reverse_lazy('participante_list')

class ParticipanteDeleteView(DeleteView):
    model = Participante
    template_name = 'gestion_eventos/participante_confirm_delete.html'
    success_url = reverse_lazy('participante_list')

# Vistas para Ticket
class TicketListView(ListView):
    model = Ticket
    template_name = 'gestion_eventos/ticket_list.html'
    paginate_by = 10

class TicketCreateView(CreateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'gestion_eventos/ticket_form.html'
    success_url = reverse_lazy('ticket_list')

class TicketUpdateView(UpdateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'gestion_eventos/ticket_form.html'
    success_url = reverse_lazy('ticket_list')

class TicketDeleteView(DeleteView):
    model = Ticket
    template_name = 'gestion_eventos/ticket_confirm_delete.html'
    success_url = reverse_lazy('ticket_list')

# Vistas para Agenda_Evento
class AgendaEventoListView(ListView):
    model = Agenda_Evento
    template_name = 'gestion_eventos/agenda_evento_list.html'
    paginate_by = 10

class AgendaEventoCreateView(CreateView):
    model = Agenda_Evento
    form_class = AgendaEventoForm
    template_name = 'gestion_eventos/agenda_evento_form.html'
    success_url = reverse_lazy('agenda_evento_list')

class AgendaEventoUpdateView(UpdateView):
    model = Agenda_Evento
    form_class = AgendaEventoForm
    template_name = 'gestion_eventos/agenda_evento_form.html'
    success_url = reverse_lazy('agenda_evento_list')

class AgendaEventoDeleteView(DeleteView):
    model = Agenda_Evento
    template_name = 'gestion_eventos/agenda_evento_confirm_delete.html'
    success_url = reverse_lazy('agenda_evento_list')

# Vistas para Patrocinador
class PatrocinadorListView(ListView):
    model = Patrocinador
    template_name = 'gestion_eventos/patrocinador_list.html'
    paginate_by = 10

class PatrocinadorCreateView(CreateView):
    model = Patrocinador
    form_class = PatrocinadorForm
    template_name = 'gestion_eventos/patrocinador_form.html'
    success_url = reverse_lazy('patrocinador_list')

class PatrocinadorUpdateView(UpdateView):
    model = Patrocinador
    form_class = PatrocinadorForm
    template_name = 'gestion_eventos/patrocinador_form.html'
    success_url = reverse_lazy('patrocinador_.list')

class PatrocinadorDeleteView(DeleteView):
    model = Patrocinador
    template_name = 'gestion_eventos/patrocinador_confirm_delete.html'
    success_url = reverse_lazy('patrocinador_list')

# Vistas para Evento_Patrocinador
class EventoPatrocinadorListView(ListView):
    model = Evento_Patrocinador
    template_name = 'gestion_eventos/evento_patrocinador_list.html'
    paginate_by = 10

class EventoPatrocinadorCreateView(CreateView):
    model = Evento_Patrocinador
    form_class = EventoPatrocinadorForm
    template_name = 'gestion_eventos/evento_patrocinador_form.html'
    success_url = reverse_lazy('evento_patrocinador_list')

class EventoPatrocinadorUpdateView(UpdateView):
    model = Evento_Patrocinador
    form_class = EventoPatrocinadorForm
    template_name = 'gestion_eventos/evento_patrocinador_form.html'
    success_url = reverse_lazy('evento_patrocinador_list')

class EventoPatrocinadorDeleteView(DeleteView):
    model = Evento_Patrocinador
    template_name = 'gestion_eventos/evento_patrocinador_confirm_delete.html'
    success_url = reverse_lazy('evento_patrocinador_list')

# Vistas para Feedback_Evento
class FeedbackEventoListView(ListView):
    model = Feedback_Evento
    template_name = 'gestion_eventos/feedback_evento_list.html'
    paginate_by = 10

class FeedbackEventoCreateView(CreateView):
    model = Feedback_Evento
    form_class = FeedbackEventoForm
    template_name = 'gestion_eventos/feedback_evento_form.html'
    success_url = reverse_lazy('feedback_evento_list')

class FeedbackEventoUpdateView(UpdateView):
    model = Feedback_Evento
    form_class = FeedbackEventoForm
    template_name = 'gestion_eventos/feedback_evento_form.html'
    success_url = reverse_lazy('feedback_evento_list')

class FeedbackEventoDeleteView(DeleteView):
    model = Feedback_Evento
    template_name = 'gestion_eventos/feedback_evento_confirm_delete.html'
    success_url = reverse_lazy('feedback_evento_list')
