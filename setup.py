from setuptools import setup, find_packages
from greenart import __version__

setup(name='greenart',
      version=__version__,
      description='Green art is cli tool for drawing on the github green panel',
      author='Sergey Fedchenko',
      author_email='seregayoga@gmail.com',
      url='https://github.com/seregayoga/greenart',
      packages=find_packages(),
      classifiers=[
          'Intended Audience :: Developers',
          'Programming Language :: Python :: 3.6',
      ],
      entry_points={
          'console_scripts': [
              'greenart=greenart.cli:main',
          ],
      },
      install_requires=[
          'docopt==0.6.2',
          'Pillow==8.1.1',
      ],
      )
