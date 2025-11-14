from django.db import models

class Tournament(models.Model):
    STATUS_CHOICES = [
        ('UPCOMING', 'Próximo'),
        ('DONE', 'Realizado'),
    ]

    nombre = models.CharField(max_length=150)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(max_length=80)
    ciudad = models.CharField(max_length=80)
    costo_inscripcion = models.DecimalField(max_digits=8, decimal_places=2)
    descripcion = models.TextField(blank=True)
    num_juegos_estimados = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='UPCOMING')

    class Meta:
        verbose_name = "Torneo"
        verbose_name_plural = "Torneos"

    def __str__(self):
        return f"{self.nombre} ({self.ciudad})"


class Team(models.Model):
    nombre = models.CharField(max_length=120)
    ciudad = models.CharField(max_length=80)
    estado = models.CharField(max_length=80)

    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"

    def __str__(self):
        return self.nombre


class Participant(models.Model):
    equipo = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='participantes')
    nombre = models.CharField(max_length=120)

    class Meta:
        verbose_name = "Participante"
        verbose_name_plural = "Participantes"

    def __str__(self):
        return f"{self.nombre} - {self.equipo.nombre}"


class Registration(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pendiente'),
        ('APPROVED', 'Aprobado'),
        ('REJECTED', 'Rechazado'),
    ]

    torneo = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='registros')
    equipo = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='registros')
    responsable_nombre = models.CharField(max_length=120)
    responsable_telefono = models.CharField(max_length=20)
    responsable_email = models.EmailField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Registro de equipo"
        verbose_name_plural = "Registros de equipos"
        unique_together = ('torneo', 'equipo')

    def __str__(self):
        return f"{self.equipo.nombre} en {self.torneo.nombre}"


class Match(models.Model):
    STATUS_CHOICES = [
        ('SCHEDULED', 'Programado'),
        ('PLAYED', 'Jugado'),
    ]

    torneo = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='partidos')
    equipo_a = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='partidos_como_a')
    equipo_b = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='partidos_como_b')
    fecha_hora = models.DateTimeField()
    cancha = models.CharField(max_length=50, blank=True)
    marcador_a = models.PositiveIntegerField(default=0)
    marcador_b = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='SCHEDULED')

    class Meta:
        verbose_name = "Partido"
        verbose_name_plural = "Partidos"

    def __str__(self):
        return f"{self.equipo_a} vs {self.equipo_b} ({self.torneo.nombre})"
