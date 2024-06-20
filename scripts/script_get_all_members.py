import os
import django
import sys
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE','djangoApplication.settings')
django.setup()


from members.models import Member

memberList = Member.objects.all()
randomLastNameList = ['Smith' ,'Johnson', 'Williams','Brown','Jones','Garcia','Miller','Davis','Rodriguez','Martinez']

def get_all_changed_members(excludingname:str=''):
    changedmemberlist = []
    for member in memberList:
        fields = member._meta.get_fields()
        field_values = dict()
        for field in fields:
            if field.concrete:  # To exclude related fields and only include concrete fields
                field_name = field.name
                field_value = getattr(member, field_name, 'N/A')
                
                if field_name == 'lastname' and field_value == excludingname:
                    field_value = randomLastNameList[random.randint(0,9)]

            field_values[field_name] = field_value
        changedmemberlist.append(field_values)
        
    return changedmemberlist
    
    
print(get_all_changed_members())