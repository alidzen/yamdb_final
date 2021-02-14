from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError

from api.models import Review, Title


def uniq_review(context, data):
    request = context.get('request')
    author = request.user
    title_id = request.parser_context['kwargs']['title_id']
    title = get_object_or_404(Title, pk=title_id)

    if Review.objects.filter(title=title, author=author).exists():
        raise ValidationError({'title': 'Author may have only one review for title'})
    return data
