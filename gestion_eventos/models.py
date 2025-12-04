
from django.db import models

class Evento(models.Model):
    id_evento = models.AutoField(primary_key=True)
    nombre_evento = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    ubicacion = models.CharField(max_length=255)
    tipo_evento = models.CharField(max_length=50)
    capacidad_maxima = models.IntegerField()
    costo_entrada = models.DecimalField(max_digits=10, decimal_places=2)
    organizador = models.CharField(max_length=100)
    estado_evento = models.CharField(max_length=50)

class Participante(models.Model):
    id_participante = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=20)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    tipo_participante = models.CharField(max_length=50)
    empresa = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)

class Ticket(models.Model):
    id_ticket = models.AutoField(primary_key=True)
    id_evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    id_participante = models.ForeignKey(Participante, on_delete=models.CASCADE)
    fecha_compra = models.DateTimeField(auto_now_add=True)
    precio_pagado = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_ticket = models.CharField(max_length=50)
    estado_ticket = models.CharField(max_length=50)
    metodo_pago = models.CharField(max_length=50)
    codigo_qr = models.CharField(max_length=255)

class Agenda_Evento(models.Model):
    id_sesion = models.AutoField(primary_key=True)
    id_evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    nombre_sesion = models.CharField(max_length=255)
    descripcion_sesion = models.TextField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    orador = models.CharField(max_length=100)
    sala = models.CharField(max_length=50)
    tema = models.CharField(max_length=100)

class Patrocinador(models.Model):
    id_patrocinador = models.AutoField(primary_key=True)
    nombre_patrocinador = models.CharField(max_length=100)
    nivel_patrocinio = models.CharField(max_length=50)
    contacto_persona = models.CharField(max_length=100)
    email_contacto = models.EmailField(max_length=100)
    telefono_contacto = models.CharField(max_length=20)
    sitio_web = models.CharField(max_length=255)
    monto_patrocinio = models.DecimalField(max_digits=10, decimal_places=2)

class Evento_Patrocinador(models.Model):
    id_evento_patrocinador = models.AutoField(primary_key=True)
    id_evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    id_patrocinador = models.ForeignKey(Patrocinador, on_delete=models.CASCADE)
    fecha_inicio_acuerdo = models.DateField()
    fecha_fin_acuerdo = models.DateField()
    monto_acordado = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_beneficio = models.TextField()

class Feedback_Evento(models.Model):
    id_feedback = models.AutoField(primary_key=True)
    id_evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    id_participante = models.ForeignKey(Participante, on_delete=models.CASCADE)
    fecha_feedback = models.DateTimeField(auto_now_add=True)
    calificacion_general = models.IntegerField()
    comentarios_adicionales = models.TextField()
    sugerencias = models.TextField()
    calificacion_oradores = models.DecimalField(max_digits=4, decimal_places=2)
