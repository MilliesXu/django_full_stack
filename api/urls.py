from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_routes, name="routes"),

    path('notes/', views.GetNotes.as_view(), name="notes"),
    path('note/create', views.CreateNote.as_view(), name="create-note"),
    path('note/<str:pk>/update/', views.UpdateNote.as_view(), name="update-note"),
    path('note/<str:pk>/delete/', views.DeleteNote.as_view(), name="delete-note"),
    path('note/<str:pk>/', views.GetNote.as_view(), name="note"),
]
