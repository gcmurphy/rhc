import os, sys
from getpass import getpass
sys.path.insert(0, os.path.join("..", "src"))

from nose.tools import *
from openshift.client.api import user

def test_userinfo():
    
    print ""
    login = raw_input("rhlogin:")
    pw = getpass("password: ")
    u = user.info(rhlogin=login, 
            password=pw,
            debug="true")

    for app in u.data.app_info:
        print "Application: ", str(app)
        print "--------------------------------------"

    print "User is VIP: ", u.data.user_info.vip







