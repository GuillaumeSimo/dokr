import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='dokr_gsimo',  
     version='0.1',
     scripts=['dokr'] ,
     author="Guillaume Simo",
     author_email="guillaume.simo@hotmal.fr",
     description="A AWS utility package",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/guillaumesimo/dokr",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )