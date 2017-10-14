from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from app.models import Richiedente, Oggetto

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

from app.serializers import RichiedenteSerializer, OggettoSerializer


@csrf_exempt
def richiedenti_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        richiedente = Richiedente.objects.all()
        serializer = RichiedenteSerializer(richiedente, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RichiedenteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class ListRichiedente(APIView):
    """
    View to list all richiedenti in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        nome = [Richiedente.nome for Richiedente in Richiedente.objects.all()]
        return Response(nome)


############# oggetto


@csrf_exempt
def oggetti_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        oggetto = Oggetto.objects.all()
        serializer = OggettoSerializer(oggetto, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = OggettoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class ListaOggetti(APIView):
    """
    View to list all richiedenti in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAdminUser,)

