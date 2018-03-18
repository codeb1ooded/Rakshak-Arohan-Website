from django.contrib.auth.models import User
from django.db.models import Q

from datetime import date

from crimeReporting.models import *



def create_user(user, name):
    query_add_user = USER( USER_REF = user,
                 NAME = name,
                 ) # foreign key need to be done
    query_add_user.save()
    query_check_user_added = USER.objects.filter(USER_REF = user)
    try:
      print(query_check_user_added[0].username)
      return True
    except:
        return False
