import os
import django
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE','djangoApplication.settings')
django.setup()


from members.models import Member

def save_users():
    member = Member(firstname='Emil', lastname='Refsnes')
    member1 = Member(firstname='Tobias', lastname='Refsnes')
    member2 = Member(firstname='Linus', lastname='Refsnes')
    member3 = Member(firstname='Lene', lastname='Refsnes')
    member4 = Member(firstname='Stale', lastname='Refsnes')
    member5 = Member(firstname='Jane', lastname='Doe')
    members_list = [member,member1, member2, member3, member4, member5]

    for x in members_list:
        response = x.save()
        print(response)
        
save_users()