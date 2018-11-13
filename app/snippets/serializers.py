from rest_framework import serializers

from .models import STYLE_CHOICES, Snippet, LANGUAGE_CHOICES

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = (
            'pk',
            'title',
            'code',
            'linenos',
            'language',
            'style',
        )