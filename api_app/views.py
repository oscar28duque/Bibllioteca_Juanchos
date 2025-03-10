from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Autor, Editorial, Libro, Miembro, Prestamo
from .serializers import AutorSerializer, EditorialSerializer, LibroSerializer, MiembroSerializer, PrestamoSerializer

# 📚 Vistas para Autor
class AutorList(generics.ListCreateAPIView):
    serializer_class = AutorSerializer

    def get_queryset(self):
        queryset = Autor.objects.all()
        if not queryset.exists():
            raise NotFound('No se encontraron autores.')
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({'success': True, 'detail': 'Listado de autores.', 'data': serializer.data}, status=status.HTTP_200_OK)

class AutorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

# 🏢 Vistas para Editorial
class EditorialList(generics.ListCreateAPIView):
    serializer_class = EditorialSerializer

    def get_queryset(self):
        queryset = Editorial.objects.all()
        if not queryset.exists():
            raise NotFound('No se encontraron editoriales.')
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({'success': True, 'detail': 'Listado de editoriales.', 'data': serializer.data}, status=status.HTTP_200_OK)

class EditorialDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

# 📖 Vistas para Libro
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

        if not queryset.exists():
            raise NotFound('No se encontraron libros.')
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({'success': True, 'detail': 'Listado de libros.', 'data': serializer.data}, status=status.HTTP_200_OK)

class LibroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

# 🧑‍🤝‍🧑 Vistas para Miembro
class MiembroList(generics.ListCreateAPIView):
    serializer_class = MiembroSerializer

    def get_queryset(self):
        queryset = Miembro.objects.all()
        if not queryset.exists():
            raise NotFound('No se encontraron miembros.')
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({'success': True, 'detail': 'Listado de miembros.', 'data': serializer.data}, status=status.HTTP_200_OK)

class MiembroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Miembro.objects.all()
    serializer_class = MiembroSerializer

# 🔄 Vistas para Préstamo con filtros
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

        if not queryset.exists():
            raise NotFound('No se encontraron préstamos.')
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({'success': True, 'detail': 'Listado de préstamos.', 'data': serializer.data}, status=status.HTTP_200_OK)

class PrestamoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer
