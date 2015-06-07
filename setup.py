from setuptools import setup, find_packages

setup(
    name='rawdata',
    version='0.0.6',
    author='Duncan Murray',
    author_email='djmurray@acutesoftware.com.au',
    packages=['rawdata'],
    include_package_data = True,
    package_data = {
        # If any package contains *.txt files, include them:
        '': ['*.txt'],
        # And include any files found in the 'data' subdirectory
        # of the 'rawdata' package, also:
        'rawdata': ['data/*.*'],
    },    
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