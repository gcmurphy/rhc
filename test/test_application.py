import os, sys
from getpass import getpass
sys.path.insert(0, os.path.join("..", "src"))

from nose.tools import *
from rhc.client.api import application 

def test_all():
    
    app_name = "testcase"
    cartridge = application.cartridges[0]
    login = raw_input("rhlogin: ")
    pw = getpass("password: ")

    ctx = { 
        "rhlogin": login, 
        "password": pw, 
        "app_name": app_name, 
        "cartridge": cartridge, 
        "debug": "true"
    }
    print "context : ", str(ctx)

    # create applcation
    res = application.create(**ctx)
    print "CREATE: ", str(res)
    
    # stop application 
    res = application.stop(**ctx)
    print "STOP: ", str(res)

    # start application
    res = application.start(**ctx)
    print "START: ", str(res)

    # restart application
    res = application.restart(**ctx)
    print "RESTART :", str(res)

    # status 
    res = application.status(**ctx)
    print "STATUS :", str(res)

    # delete 
    res = application.delete(**ctx)
    print "DELETE: ", str(res)
    

