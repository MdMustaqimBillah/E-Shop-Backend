from django.db import models
from djagno.core.exceptions import ObjectDoesNotExitst
from django.core.validators import ValidationError


class BaseRepository:
    
    def __init__(self, model: models.Model):
        self.model = model
        
        
    def get_all(self):
        return self.model.objects.all()
    
    def get_by_id(self, obj_id):
        
        try:
            return models.objects.get(id=obj_id)
        except ObjectDoesNotExitst:
            return ValidationError(f"{self.model.__name__} with id {obj_id} does not exist.")
        
    def create(self, *args, **kwargs):
        
        return self.model.objects.create(*args, **kwargs)
    
    def update(self, obj_id,*args, **kwargs):
        
        try:
            obj = models.objects.get(id=obj_id)
        except ObjectDoesNotExist:
            return ValidationError(f"{self.model.__name__} with id {obj_id} does not exist.")
        
        return obj.update(*args, **kwargs)
    
    def delete( self, obj_id):
        try:
            obj = models.bojects.get(id=obj_id)
        except ObjectDoesNotExist:
            return ValidationError(f"{self.model.__name__} with id {obj_id} does not exist.")
        
        return object.delete()
