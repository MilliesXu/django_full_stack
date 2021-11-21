from django.db.models.query import QuerySet
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.response import Response

from .models import Note
from .serializers import NoteSerializer


# Create your views here.

@api_view(['GET'])
def get_routes(request):
    routes = [
        {
            'Endpoint': 'api/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': 'api/notes/id/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': 'api/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': 'api/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': 'api/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]

    return Response(routes)

class GetNotes(ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class GetNote(RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class UpdateNote(UpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class DeleteNote(DestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class CreateNote(CreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

