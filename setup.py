from distutils.core import setup
import pkg_resources

import sys

requires = ['six']
if sys.version_info < (2, 7):
    requires.append('argparse')

version = pkg_resources.require("fitparse")[0].version

setup(
    name='fitparse',
    version=version,
    description='Python library to parse ANT/Garmin .FIT files',
    author='David Cooper, Kévin Gomez',
    author_email='dave@kupesoft.com, contact@kevingomez.fr',
    url='https://github.com/K-Phoen/python-fitparse',
    license=open('LICENSE').read(),
    packages=['fitparse'],
    scripts=['scripts/fitdump'],  # Don't include generate_profile.py
    install_requires=requires,
)
