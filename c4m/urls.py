from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.contrib import admin
from app.models import Richiedente, Oggetto
from app.serializers import OggettoSerializer
from django.conf.urls.static import static

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RichiedenteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Richiedente
        fields = ('nome', 'cognome', 'email', 'telefono')

class RichiedenteViewSet(viewsets.ModelViewSet):
    queryset = Richiedente.objects.all()
    serializer_class = RichiedenteSerializer

#class OggettoSerializer(serializers.HyperlinkedModelSerializer):
#   class Meta:
#        model = Oggetto
#        richiedente = Oggetto.richiedente
#        fields = ('titolo', 'regione', 'citta', 'descrizione','prezzo')
#        #extra_kwargs = {'url': {'view_nome': 'richiedente', 'lookup_field': 'richiedente_nome'},}


class OggettoViewSet(viewsets.ModelViewSet):
    queryset = Oggetto.objects.all()
    serializer_class = OggettoSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'richiedente',RichiedenteViewSet)
router.register(r'oggetti',OggettoViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]