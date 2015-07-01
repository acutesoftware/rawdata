from setuptools import setup

setup(
    name='rawdata',
    version='0.1.0',
    author='Duncan Murray',
    author_email='djmurray@acutesoftware.com.au',
    packages=['rawdata', 'rawdata.gather'],
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
    'Development Status :: 3 - Alpha',
    'Environment :: Web Environment',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Topic :: Games/Entertainment :: Simulation',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Topic :: Software Development :: Libraries :: Python Modules',
    ],

)