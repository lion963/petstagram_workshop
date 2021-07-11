from django.shortcuts import render, redirect

from accounts.models import UserProfile
from common.forms import CommentForm
from common.models import Comment
from pets.models import Pet


def landing_page(request):
    return render(request, 'landing_page.html')


def create_comment(request, pk):
        user = request.user
        profile = UserProfile.objects.get(user=user)
        form = CommentForm(request.POST)
        form.is_valid()
        comment = Comment(pet=Pet.objects.get(pk=pk), comment=form.cleaned_data['comment'], user=profile)
        comment.save()
        return redirect('details', pk)