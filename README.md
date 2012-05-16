
pyrhc: Openshift Client Rest API
==================================

About
-----

Provides a low level access 
to the OpenShift Rest Client API 
from Python. This allows you to 
create, control and configure 
applications for OpenShift using 
Python. 


Status
------
Still very rough around the edges. Was 
also trying out "no classes" using python

Usage
-----
    
    from rhc.client.api import user 

    info = user.info( **{
            "rhlogin": Your-Login, 
            "password": Your-Password, 
            "debug": "true"
            })

    # List application names for the  user
    for app in info.data.app_info:
        print str(app)

Installing
----------

At the moment you should be able to install as follows: 
    
    pip install --upgrade git+git://github.com/gcmurphy/pyrhc

I'll get things up on readthedocs.org when I get closer to being 
finished..

