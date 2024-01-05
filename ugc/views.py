from django.shortcuts import render
from rest_framework import generics, permissions
from .models import UGCPost, Location
from .serializers import UGCPostSerializer, LocationSerializer

# Create your views here.


class UGCPostListCreateView(generics.ListCreateAPIView):
    queryset = UGCPost.objects.all()
    serializer_class = UGCPostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UGCPostDetailView(generics.RetrieveAPIView):
    queryset = UGCPost.objects.all()
    serializer_class = UGCPostSerializer


class LocationListCreateView(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
