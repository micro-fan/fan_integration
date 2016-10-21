import logging

from django.conf import settings


from rest_framework import viewsets, serializers

from drf_app.models import Author

# Create your views here.


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author



class AuthorViewset(viewsets.ModelViewSet):

    log = logging.getLogger('AuthorViewset')

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def create(self, request, *args, **kwargs):
        self.log.error('RDU: {}'.format(request.META['HTTP_OT_TRACE_ID']))
        return super().create(request, *args, **kwargs)
