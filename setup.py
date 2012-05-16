from setuptools import setup, find_packages 

setup(
    name='openshift', 
    version='0.1.0', 
    author='Grant Murphy', 
    author_email='gmurphy@redhat.com', 
    package_dir={'':'src'}, 
    packages=find_packages('src'),
    url='https://github.com/gcmurphy/openshift',
    license="PSF",
    description='Create, control and configure OpenShift applications using Python', 
    long_description=open('README.md').read(),
    install_requires=[
        "requests", 
        "simplejson",
        "nose"
    ], 
)
