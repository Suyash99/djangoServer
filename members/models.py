from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)

def __str__(self):
    fields = self._meta.get_fields()
    field_values = {}
    for field in fields:
        if field.concrete: 
            field_name = field.name
            field_value = getattr(self, field_name, 'N/A')
            field_values[field_name] = field_value

    return field_values