from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()


setup(name='iptoolsjj',
      version='1.4.1',
      description='IP Tools',
      long_description=long_description,
      long_description_content_type='text/markdown',	
      url='https://github.com/jarekj9/iptoolsjj',
      author='Jaroslaw Jankun',
      author_email='jaroslaw.jankun@gmail.com',
      packages=['iptoolsjj'],
      classifiers=[
          'License :: OSI Approved :: MIT License'
      ]
      zip_safe=False)
