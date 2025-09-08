from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import ValidationError


class BaseRepository:
    
    def __init__(self, model: models.Model):
        self.model = model
        
        
    def get_all(self):
        return self.model.objects.all()
    
    def get_by_id(self, obj_id):
        
        try:
            return self.models.objects.get(id=obj_id)
        except ObjectDoesNotExist:
            return ValidationError(f"{self.model.__name__} with id {obj_id} does not exist.")
        
    def create(self, *args, **kwargs):
        
        return self.models.objects.create(*args, **kwargs)
    
    def update(self, obj_id,*args, **kwargs):
        
        try:
            obj = self.models.objects.get(id=obj_id)
            
            for key, value in kwargs.items():
                setattr(obj, key, value)
            obj.save()
            return obj
        
        except ObjectDoesNotExist:
            return ValidationError(f"{self.model.__name__} with id {obj_id} does not exist.")
        
        return obj.update(*args, **kwargs)
    
    def delete( self, obj_id):
        try:
            obj = self.models.ojects.get(id=obj_id)
            obj.delete()
            return True
        except ObjectDoesNotExist:
            return ValidationError(f"{self.model.__name__} with id {obj_id} does not exist.")