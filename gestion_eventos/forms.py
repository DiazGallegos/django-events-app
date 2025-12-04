
from django import forms
from .models import Evento, Participante, Ticket, Agenda_Evento, Patrocinador, Evento_Patrocinador, Feedback_Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre_evento', 'descripcion', 'fecha_inicio', 'fecha_fin', 'ubicacion', 'tipo_evento', 'capacidad_maxima', 'costo_entrada', 'organizador', 'estado_evento']

class ParticipanteForm(forms.ModelForm):
    class Meta:
        model = Participante
        exclude = ('fecha_registro',)

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        exclude = ('fecha_compra',)
        widgets = {
            'id_evento': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ID del Evento'}),
            'id_participante': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ID del Participante'}),
        }

class AgendaEventoForm(forms.ModelForm):
    class Meta:
        model = Agenda_Evento
        fields = ['id_evento', 'nombre_sesion', 'descripcion_sesion', 'hora_inicio', 'hora_fin', 'orador', 'sala', 'tema']
        widgets = {
            'id_evento': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ID del Evento'}),
        }

class PatrocinadorForm(forms.ModelForm):
    class Meta:
        model = Patrocinador
        fields = ['nombre_patrocinador', 'nivel_patrocinio', 'contacto_persona', 'email_contacto', 'telefono_contacto', 'sitio_web', 'monto_patrocinio']

class EventoPatrocinadorForm(forms.ModelForm):
    class Meta:
        model = Evento_Patrocinador
        fields = ['id_evento', 'id_patrocinador', 'fecha_inicio_acuerdo', 'fecha_fin_acuerdo', 'monto_acordado', 'tipo_beneficio']
        widgets = {
            'id_evento': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ID del Evento'}),
            'id_patrocinador': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ID del Patrocinador'}),
        }

class FeedbackEventoForm(forms.ModelForm):
    class Meta:
        model = Feedback_Evento
        exclude = ('fecha_feedback',)
        widgets = {
            'id_evento': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ID del Evento'}),
            'id_participante': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ID del Participante'}),
        }
