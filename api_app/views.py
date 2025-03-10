from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Autor, Editorial, Libro, Miembro, Prestamo
from .serializers import AutorSerializer, EditorialSerializer, LibroSerializer, MiembroSerializer, PrestamoSerializer

# Vistas para Autor
class AutorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class AutorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

# Vistas para Editorial
class EditorialList(generics.ListCreateAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

class EditorialDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

class LibroList(generics.ListCreateAPIView):
    serializer_class = LibroSerializer

    def get_queryset(self):
        queryset = Libro.objects.all()
        autor_id = self.request.query_params.get('autor')
        editorial_id = self.request.query_params.get('editorial')

        if autor_id:
            queryset = queryset.filter(autor_id=autor_id)
        if editorial_id:
            queryset = queryset.filter(editorial_id=editorial_id)
        
        if not queryset.exists():  # Si no hay libros, lanza NotFound
            raise NotFound('No se encontraron libros.')

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({'success': True, 'detail': 'Listado de libros.', 'data': serializer.data}, status=status.HTTP_200_OK)


class LibroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

# Vistas para Miembro
class MiembroList(generics.ListCreateAPIView):
    queryset = Miembro.objects.all()
    serializer_class = MiembroSerializer

class MiembroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Miembro.objects.all()
    serializer_class = MiembroSerializer

# Vistas para Préstamo con filtros
class PrestamoList(generics.ListCreateAPIView):
    serializer_class = PrestamoSerializer

    def get_queryset(self):
        queryset = Prestamo.objects.all()
        miembro_id = self.request.query_params.get('miembro')
        fecha_prestamo = self.request.query_params.get('fecha')

        if miembro_id:
            queryset = queryset.filter(miembro_id=miembro_id)
        if fecha_prestamo:
            queryset = queryset.filter(fecha_prestamo=fecha_prestamo)

        return queryset

class PrestamoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer
