from setuptools import setup

setup(
    name='rawdata',
    version='0.0.5',
    author='Duncan Murray',
    author_email='djmurray@acutesoftware.com.au',
    packages=['rawdata'],
    url='https://github.com/acutesoftware/rawdata',
    license='GNU General Public License v3 (GPLv3)',
    description='Generate realistic raw datasets with optional DQ issues',
    long_description=open('README.rst').read(),
    classifiers = [
    'Development Status :: 2 - Pre-Alpha',
    'Environment :: Web Environment',
    'Programming Language :: Python :: 3.4',
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Games/Entertainment :: Simulation',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],

)