from rest_framework import viewsets
from .models import Issue
from .serializers import IssueSerializer

class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all() 
    serializer_class = IssueSerializer

    def get_queryset(self):
        queryset = Issue.objects.all()
        status = self.request.query_params.get('status')

        if status:
            queryset = queryset.filter(status=status)

        return queryset

# Create your views here.
