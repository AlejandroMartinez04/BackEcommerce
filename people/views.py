from django.shortcuts import render

from django.contrib.auth.models import People
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['PUT'])
def modificar_usuario_por_correo(request):
    email = request.data.get('email')  # Obtiene el correo electrónico del cuerpo de la solicitud
    nuevos_datos = request.data.get('nuevos_datos')  # Obtiene los nuevos datos del cuerpo de la solicitud

    try:
        usuario = People.objects.get(email=email)  # Busca el usuario por su correo electrónico
    except People.DoesNotExist:
        return Response({'mensaje': 'User not found'}, status=404)

    # Realiza la modificación del usuario con los nuevos datos
    # Ejemplo: usuario.username = nuevos_datos['username']
    # Asegúrate de validar y aplicar las modificaciones según tus necesidades

    usuario.save()  # Guarda los cambios realizados en el usuario

    return Response({'mensaje': 'User modified'})
