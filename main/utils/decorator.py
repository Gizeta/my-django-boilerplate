from functools import wraps

from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.http import QueryDict

def validate_args(myargs):
  def decorator(func):
    @wraps(func)
    def inner(self, request, *args, **kwargs):
      if request.method == 'GET':
        data = request.GET
      elif request.method == 'POST':
        data = request.POST
      else:
        data = QueryDict(request.body)
      for k, v in myargs.items():
        try:
          if k in kwargs:
            request_value = kwargs.get(k)
          else:
            request_value = data.get(k) or request.FILES[k]
          kwargs[k] = v.clean(request_value)
        except KeyError:
          if v.required:
            return err_response_miss_param(k)
        except ValidationError as e:
          return err_response_value_err(
            k, request_value, ','.join(e)
          )
      return func(self, request, *args, **kwargs)
    return inner
  return decorator

def query_object(model, object_name, arg_name=None):
  def decorator(func):
    @wraps(func)
    def inner(*args, **kwargs):
      arg = arg_name or (object_name + '_id')
      if arg in kwargs:
        obj_id = kwargs.pop(arg)
        try:
          obj = model.get(pk=obj_id)
        except ObjectDoesNotExist:
          return err_response_pk(arg, obj_id)
        else:
          kwargs[object_name] = obj
      return func(*args, **kwargs)
    return inner
  return decorator
