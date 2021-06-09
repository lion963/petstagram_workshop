from itertools import count

from django.shortcuts import render, redirect

from pets.models import Pet, Like


def pet_all(request):
    context = {
        'pets': Pet.objects.all()
    }
    return render(request, 'pet_list.html', context)

def pet_detail(request, pk):
    pet = Pet.objects.get(pk=pk)
    data = len(Like.objects.filter(pet_id=pk))
    context = {
        'pet': pet,
        'data': data
    }
    return render(request, 'pet_detail.html', context)

def pet_like(request, pk):
    pet = Pet.objects.get(pk=pk)
    like = Like(pet_id=pet.id)
    like.save()
    data = len(Like.objects.filter(pet_id=pk))
    context = {
        'pet': pet,
        'data': data
    }
    # return redirect('pets/details', {pet.id}, context)
    return render(request, 'pet_detail.html', context)