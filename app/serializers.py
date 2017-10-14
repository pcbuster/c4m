from rest_framework import serializers
from app.models import Richiedente, Oggetto
from django.http import JsonResponse


##class RichiedentetSerializer(serializers.Serializer):
##    idRichiedente = serializers.IntegerField(read_only=True)
##    nome = serializers.CharField(required=False, allow_blank=True, max_length=100)
##    cognome = serializers.CharField(style={'base_template': 'textarea.html'})
##    email = serializers.EmailField(required=False)
##    indirizzo = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#
#class RichiedenteSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Richiedente
#        Oggetti = serializers.StringRelatedField(many=True)
#        fields = ('nome', 'cognome', 'email', 'indirizzo', 'telefono')
#
#
#
#
#
#    def create(self, validated_data):
#        """
#        Create and return a new `Snippet` instance, given the validated data.
#        """
#        return Richiedente.objects.create(**validated_data)
#
#    def update(self, instance, validated_data):
#        """
#        Update and return an existing `Snippet` instance, given the validated data.
#        """
#        instance.nome = validated_data.get('nome', instance.nome)
#        instance.cognome = validated_data.get('cognome', instance.cognome)
#        instance.email = validated_data.get('email', instance.email)
#        instance.indirizzo = validated_data.get('indirizzo', instance.indirizzo)
#        instance.save()
#        return instance
#
#class OggettoSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Oggetto
#        fields = ('richiedente', 'titolo', 'regione', 'citta', 'descrizione', 'prezzo')
#
#
#
#
#    def create(self, validated_data):
#        """
#        Create and return a new `Snippet` instance, given the validated data.
#        """
#        return Oggetto.objects.create(**validated_data)
#
#    def update(self, instance, validated_data):
#        """
#        Update and return an existing `Snippet` instance, given the validated data.
#
#        """
#        instance.richiedente = validated_data.get('richiedente', instance.richiedente)
#        instance.titolo = validated_data.get('titolo', instance.titolo)
#        instance.regione = validated_data.get('regione', instance.regione)
#        instance.citta = validated_data.get('citta', instance.citta)
#        instance.descrizione = validated_data.get('descrizione', instance.descrizione)
#        instance.prezzo = validated_data.get('prezzo', instance.prezzo)
#        instance.save()
#        return instance


class RichiedenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Richiedente
        Oggetti = serializers.StringRelatedField(many=True)
        fields = ('nome', 'cognome', 'email', 'indirizzo', 'telefono')


    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Richiedente.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.nome = validated_data.get('nome', instance.nome)
        instance.cognome = validated_data.get('cognome', instance.cognome)
        instance.email = validated_data.get('email', instance.email)
        instance.indirizzo = validated_data.get('indirizzo', instance.indirizzo)
        instance.save()
        return instance

class OggettoSerializer(serializers.ModelSerializer):
    nome_r = serializers.SerializerMethodField()
    class Meta:
        model = Oggetto
        fields = ('nome_r', 'titolo', 'regione', 'citta', 'descrizione', 'prezzo')

    # Aggiunto
        rich_nome = RichiedenteSerializer(many=False)


    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Oggetto.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.

        """
        instance.richiedente = validated_data.get('richiedente', instance.richiedente)
        instance.titolo = validated_data.get('titolo', instance.titolo)
        instance.regione = validated_data.get('regione', instance.regione)
        instance.citta = validated_data.get('citta', instance.citta)
        instance.descrizione = validated_data.get('descrizione', instance.descrizione)
        instance.prezzo = validated_data.get('prezzo', instance.prezzo)
        instance.save()
        return instance

    def get_nome_r(self, obj):
        return obj.richiedente.cognome + ' ' + obj.richiedente.nome