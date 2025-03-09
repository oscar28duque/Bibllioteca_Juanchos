from django.urls import path
from .views import (
    AutorList, AutorDetail, EditorialList, EditorialDetail, 
    LibroList, LibroDetail, MiembroList, MiembroDetail, 
    PrestamoList, PrestamoDetail
)

urlpatterns = [
    path('autores/', AutorList.as_view(), name='autor-list'),
    path('autores/<int:pk>/', AutorDetail.as_view(), name='autor-detail'),

    path('editoriales/', EditorialList.as_view(), name='editorial-list'),
    path('editoriales/<int:pk>/', EditorialDetail.as_view(), name='editorial-detail'),

    path('libros/', LibroList.as_view(), name='libro-list'),
    path('libros/<int:pk>/', LibroDetail.as_view(), name='libro-detail'),

    path('miembros/', MiembroList.as_view(), name='miembro-list'),
    path('miembros/<int:pk>/', MiembroDetail.as_view(), name='miembro-detail'),

    path('prestamos/', PrestamoList.as_view(), name='prestamo-list'),
    path('prestamos/<int:pk>/', PrestamoDetail.as_view(), name='prestamo-detail'),
]