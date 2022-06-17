from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from finalboss.models import User, Reksadana
from finalboss.forms import userForm, reksaDanaForm
from django import forms


def users(request):
    users = User.objects.all()
    usersDict = {'users': users}
    return render(request, 'users.html', context=usersDict)


def userDetail(request, username):
    userDetail = User.objects.get(userName__exact=username)
    return render(request, 'userDetail.html', context={'user': userDetail})


def editProfile(request, username):
    profileDetail = User.objects.get(userName__exact=username)
    form = userForm(instance=profileDetail)
    if request.method == 'POST':
        form = userForm(request.POST, instance=profileDetail)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('../')
        else:
            print('Validation error!')
    return render(request, 'editProfile.html', context={'form': form})


def buyReksaDana(request, username):
    form = reksaDanaForm(initial={'userName': username})
    if request.method == 'POST':
        form = reksaDanaForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('details')
        else:
            print('Validation Error')
    return render(request, 'buyReksadana.html', context={'form': form, 'username': username})


def detailReksaDana(request, username):
    reksaDanaData = Reksadana.objects.all().filter(userName=username)
    return render(request, 'detailReksaDana.html', context={'reksaDana': reksaDanaData, 'username': username})


def sellReksaDana(request, username, id):
    reksaDanaDetail = Reksadana.objects.get(id__exact=id)
    if request.method == 'POST':
        reksaDanaDetail.delete()
        return HttpResponseRedirect('../details')
    return render(request, 'sellReksaDana.html', context={'reksaDana': reksaDanaDetail, 'username': username})
