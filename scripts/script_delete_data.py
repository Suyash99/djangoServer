import os
import django
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE','djangoApplication.settings')
django.setup()


from members.models import Member

def delete_members(delete_everything:bool=False, id:int = 0):
    # Get only selected menbers by id, if provided
    # Still we get member list, then loop
    
    if delete_everything and id:
        raise ReferenceError('Cannot Delete Everything as id also passed! Will not execute')

    member_list = Member.objects.all()
    delete_count :int = 0
    for member in member_list:
        delete_member:bool = False
        if delete_everything:
            delete_member = True
            
        if not delete_member and id and member.id == id:
            delete_member = True
                            
        if delete_member:
            delete_res = member.delete()
            delete_count += 1
            print(f'Delete Res- {delete_res}')
    
    return delete_count


print(delete_members(True))
            