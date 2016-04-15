from distutils.core import setup

import os.path
import sys

requires = ['six']
if sys.version_info < (2, 7):
    requires.append('argparse')

# Get __version__ from fitparse.version without importing
with open(os.path.join('fitparse', 'version.py')) as f:
    exec(f.read())

setup(
    name='fitparse',
    version=__version__,
    description='Python library to parse ANT/Garmin .FIT files',
    author='David Cooper, Kévin Gomez',
    author_email='dave@kupesoft.com, contact@kevingomez.fr',
    url='https://github.com/K-Phoen/python-fitparse',
    license=open('LICENSE').read(),
    packages=['fitparse'],
    scripts=['scripts/fitdump'],  # Don't include generate_profile.py
    install_requires=requires,
)
