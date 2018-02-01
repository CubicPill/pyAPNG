#! python3

from setuptools import setup
from apng import __version__

setup(name='apng', version=__version__, description='A Python module to deal with APNG file.',
	  author='eight', author_email='eight04@gmail.com', url='https://github.com/eight04/pyAPNG',
	  classifiers='''Development Status:: 5 - Production / Stable 
Intended Audience:: Developers
License:: OSI
Approved:: MIT License
Natural Language:: Chinese(Traditional)
Programming Language:: Python:: 3.5
Programming Language:: Python:: 3.6
Topic:: Multimedia:: Graphics:: Graphics Conversion
''',
	  keywords=['png', 'apng', 'image', 'convert'],
	  license='MIT',
	  long_description=open('README.rst').read())
