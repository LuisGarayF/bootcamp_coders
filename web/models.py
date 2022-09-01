
from django.db import models


class Comuna(models.Model):
    codigo_comuna = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True)
    codigo_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='codigo_region', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comuna'
    
        def __str__(self):
         return f'{self.nombre}'

class Curso(models.Model):
    codigo_curso = models.CharField(primary_key=True, max_length=30)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_termno = models.DateField(blank=True, null=True)
    codigo_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='codigo_comuna', blank=True, null=True)
    codigo_plan_formativo = models.ForeignKey('PlanFormativo', models.DO_NOTHING, db_column='codigo_plan_formativo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'curso'

    def __str__(self):
        return f'{self.codigo_curso}'

    
    @property
    def id_estudiante(self):
        return self.codigo_curso.id_estudiante
    
    @property
    def nombre_curso(self):
        return self.codigo_plan_formativo.descripcion
    

    


class CursoModuloTutor(models.Model):
    codigo_curso = models.OneToOneField(Curso, models.DO_NOTHING, db_column='codigo_curso', primary_key=True)
    codigo_modulo = models.ForeignKey('Modulo', models.DO_NOTHING, db_column='codigo_modulo')
    codigo_tutor = models.ForeignKey('Tutor', models.DO_NOTHING, db_column='codigo_tutor')

    class Meta:
        managed = False
        db_table = 'curso_modulo_tutor'
        unique_together = (('codigo_curso', 'codigo_modulo', 'codigo_tutor'),)
        


class Estudiante(models.Model):
    id_estudiante = models.IntegerField(primary_key=True)
    rut = models.CharField(max_length=15, blank=True, null=True)
    nombre = models.CharField(max_length=30, blank=True, null=True)
    apellido_pat = models.CharField(max_length=30, blank=True, null=True)
    apellido_mat = models.CharField(max_length=30, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    codigo_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='codigo_comuna', blank=True, null=True)
    codigo_curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='codigo_curso', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estudiante'
    
    @property
    def descripcion(self):
        return self.codigo_curso.codigo_plan_formativo.descripcion
    
    @property
    def comuna(self):
        return self.codigo_comuna.nombre
    
    @property
    def region(self):
        return self.codigo_comuna.codigo_region.nombre
    

class Modulo(models.Model):
    codigo_modulo = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    duracion_horas = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modulo'


class PlanFormativo(models.Model):
    codigo_plan_formativo = models.CharField(primary_key=True, max_length=30)
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    duracion_horas = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plan_formativo'


class PlanModulo(models.Model):
    codigo_plan_formativo = models.OneToOneField(PlanFormativo, models.DO_NOTHING, db_column='codigo_plan_formativo', primary_key=True)
    codigo_modulo = models.ForeignKey(Modulo, models.DO_NOTHING, db_column='codigo_modulo')

    class Meta:
        managed = False
        db_table = 'plan_modulo'
        unique_together = (('codigo_plan_formativo', 'codigo_modulo'),)


class Region(models.Model):
    codigo_region = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'region'
    
    def __str__(self):
        return f'{self.nombre}'


class Tutor(models.Model):
    codigo_tutor = models.IntegerField(primary_key=True)
    rut = models.CharField(max_length=15, blank=True, null=True)
    nombre = models.CharField(max_length=30, blank=True, null=True)
    apellido_pat = models.CharField(max_length=30, blank=True, null=True)
    apellido_mat = models.CharField(max_length=30, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    cargo = models.CharField(max_length=20, blank=True, null=True)
    codigo_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='codigo_comuna', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tutor'

    