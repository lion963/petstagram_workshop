from itertools import count

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from accounts.models import UserProfile
from common.forms import CommentForm
from common.models import Comment
from pets.forms import PetCreateForm
from pets.models import Pet, Like


def pet_all(request):
    context = {
        'pets': Pet.objects.all()
    }
    return render(request, 'pet_list.html', context)

def pet_detail(request, pk):
    liked = False
    pet = Pet.objects.get(pk=pk)
    user = request.user
    profile = UserProfile.objects.get(user=user)
    likes = Like.objects.filter(user=profile)
    for like in likes:
        if pet.id == like.pet_id:
            liked = True
    data = len(Like.objects.filter(pet_id=pk))
    form = CommentForm()
    data_comments = Comment.objects.filter(pet_id=pk)
    comments = []
    for comment in data_comments:
        comments.append(comment.comment)
    context = {
        'pet': pet,
        'data': data,
        'form': form,
        'comments': comments,
        'profile': profile,
        'liked': liked
    }
    return render(request, 'pet_detail.html', context)


def pet_like(request, pk):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    pet = Pet.objects.get(pk=pk)
    # if pet.profile in Like.objects.filter(user=profile):
    #     pass
    # else:
    like = Like(pet_id=pet.id, user=profile)
    like.save()
    data = len(Like.objects.filter(pet_id=pk))
    context = {
        'pet': pet,
        'data': data,
    }
    return redirect('details', pk)
    # return render(request, 'pet_detail.html', context)


@login_required(login_url='login')
def create_pet(request):
    if request.method == 'GET':
        form = PetCreateForm()
        return render(request, 'pet_create.html', {'form': form})
    form = PetCreateForm(request.POST, request.FILES)
    if form.is_valid():
        pet = form.save(commit=False)
        pet.user = UserProfile.objects.get(user=request.user)
        pet.save()
        return redirect('/pets')
    return render(request, 'pet_create.html', {'form': form})

def edit_pet(request, pk):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        form = PetCreateForm(instance=pet)
        return render(request, 'pet_edit.html', {'form': form})
    form = PetCreateForm(request.POST, request.FILES, instance=pet)
    if form.is_valid():
        pet = form.save(commit=False)
        pet.user = profile
        pet.save()
        return redirect('details', pk)
    return render(request, 'pet_edit.html', {'form': form})

def delete_pet(request, pk):
    if request.POST.get('delete button'):
        pet = Pet.objects.get(pk=pk)
        pet.delete()
        return redirect('pet all')
    return render(request, 'pet_delete.html')