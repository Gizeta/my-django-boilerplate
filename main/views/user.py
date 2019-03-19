from django import forms
from django.views import View
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from ..models import *
from ..utils import *

class UserReg(View):
  def get(self, request, **kwargs):
    return render(request, 'reg.html')

  @validate_args({
    'username': forms.CharField(),
    'password': forms.CharField(),
  })
  def post(self, request, username, password, **kwargs):
    user = User.objects.create(username=username, password=password)
    return HttpResponseRedirect(reverse('main:user:index', kwargs={'user_id': user.id}))

class UserIndex(View):
  @validate_args({
    'user_id': forms.IntegerField(),
  })
  @query_object(User.objects, 'user')
  def get(self, request, user, **kwargs):
    return render(request, 'index.html', {
      'user': user
    })
