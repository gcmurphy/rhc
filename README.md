pyrhc
==================================
Python bindings to the  Openshift Client Rest API 

About
-----

Provides a thin Python layer over the OpenShift 
Rest Client API.  Allows you to create, control 
and configure applications for OpenShift using 
Python. 

Status
------

Tried to fly as close to the json as possible. 
All interfaces are implemented with validation for 
key elements and results are essentially just unmarshaled
json dictionaries that have been converted to a Bunch. 

__Todo__
 * Documentation 
 * More unit testing 
 * Create Python packaging

Examples
-----
    
List application names for the user:

    from rhc.client.api import user 

    creds = { 
        "rhlogin" : "Your-Login", 
        "password": "Your-Password" 
    }
    info = user.info(**creds)

    for app in info.data.app_info:
        print str(app)


Create a new application:

    from rhc.client.api import application

    creds = { 
        "rhlogin" : "Your-Login", 
        "password": "Your-Password"
    }

    r = application.create(cartridge="nodejs-0.6", app_name="example", **creds)
    print "Result: %s", r.result


List available embedded cartridges: 
    
    from rhc.client.api import cartridges

    cartlist = cartridges.list()
    for cart in cartlist.data.carts: 
        print cart
        
Installing
----------

As a temporary measure you install this via pip. I'll register it 
as a proper Python package at a later date. 
    
    pip install --upgrade git+git://github.com/gcmurphy/pyrhc



