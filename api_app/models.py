from django.db import models

# Create your models here.

# Modelo de Autor
class Autor(models.Model):
    id_autor = models.AutoField(primary_key=True, editable=False, db_column='T001IdAutor')
    nombre = models.CharField(max_length=100, db_column='T001Nombre')
    apellido = models.CharField(max_length=100, db_column='T001Apellido')
    biografia = models.TextField(blank=True, null=True, db_column='T001Biografia')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        db_table = 'T001Autor'
        verbose_name = 'Autor'
        verbose_name_plural = 'autores'

# Modelo de Editorial
class Editorial(models.Model):
    id_editorial = models.AutoField(primary_key=True, editable=False, db_column='T002IdEditorial')
    nombre = models.CharField(max_length=100, db_column='T002Nombre')
    direccion = models.TextField(db_column='T002Direccion')
    telefono = models.CharField(max_length=15, blank=True, null=True, db_column='T002Telefono')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'T002Editorial'
        verbose_name = 'Editorial'
        verbose_name_plural = 'editoriales'

# Modelo de Libro 
class Libro(models.Model):
    id_libro = models.AutoField(primary_key=True, editable=False, db_column='T003IdLibro')
    titulo = models.CharField(max_length=200, db_column='T003Titulo')
    resumen = models.TextField(db_column='T003Resumen')
    isbn = models.CharField(max_length=13, unique=True, db_column='T003ISBN')
    anio_publicacion = models.CharField(max_length=10, db_column='T003AnioPublicacion')
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros', db_column='T003IdAutor')
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, related_name='libros', db_column='T003IdEditorial')

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = 'T003Libro'
        verbose_name = 'Libro'
        verbose_name_plural = 'libros'

# Modelo de Miembro
class Miembro(models.Model):
    id_miembro = models.AutoField(primary_key=True, editable=False, db_column='T004IdMiembro')
    nombre = models.CharField(max_length=100, db_column='T004Nombre')
    apellido = models.CharField(max_length=100, db_column='T004Apellido')
    email = models.EmailField(unique=True, db_column='T004Email')
    fecha_membresia = models.DateField(auto_now_add=True, db_column='T004FechaMembresia')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        db_table = 'T004Miembro'
        verbose_name = 'Miembro'
        verbose_name_plural = 'miembros'

# Modelo de Préstamo
class Prestamo(models.Model):
    id_prestamo = models.AutoField(primary_key=True, editable=False, db_column='T005IdPrestamo')
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='prestamos', db_column='T005IdLibro')
    miembro = models.ForeignKey(Miembro, on_delete=models.CASCADE, related_name='prestamos', db_column='T005IdMiembro')
    fecha_prestamo = models.DateField(auto_now_add=True, db_column='T005FechaPrestamo')
    fecha_devolucion = models.DateField(blank=True, null=True, db_column='T005FechaDevolucion')

    def __str__(self):
        return f"{self.libro.titulo} prestado a {self.miembro.nombre} {self.miembro.apellido}"

    class Meta:
        db_table = 'T005Prestamo'
        verbose_name = 'Prestamo'
        verbose_name_plural = 'prestamos'

