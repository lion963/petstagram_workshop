from django.shortcuts import render, redirect

from common.forms import CommentForm
from common.models import Comment
from pets.models import Pet


def landing_page(request):
    return render(request, 'landing_page.html')


def create_comment(request, pk):
        form = CommentForm(request.POST)
        form.is_valid()
        comment = Comment(pet=Pet.objects.get(pk=pk), comment=form.cleaned_data['comment'])
        comment.save()
        return redirect('details', pk)