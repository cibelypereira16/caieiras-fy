from rest_framework import serializers

from music.models import Music


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields =('name_music', 'artist', 'genre', 'link_music','comida')
        
