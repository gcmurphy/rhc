
from getpass import getpass
import os, sys
sys.path.insert(0, os.path.join("..", "src"))

from nose.tools import *
from openshift.client.api import domain

def test_create():
    
    pubkey = open(os.path.expanduser("~/.ssh/libra_id_rsa.pub"), "r")
    librsa_id_pub = pubkey.read().split(" ")[1]
    login = raw_input("rhlogin: ")
    pw = getpass("password: ")
    namespace = raw_input("namespace: ")
    r = domain.create(rhlogin=login, 
            password=pw,
            ssh=librsa_id_pub, 
            namespace=namespace, 
            debug="true", 
            alter="true")

    print r







