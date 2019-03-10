from setuptools import setup

setup(name='copyfotos',
      version='0.1',
      description='Copia las fotos de una ubicación a ostra organizandolas por carpetas',
      url='https://github.com/albertoperalta/Fotos',
      author='Alberto Peralta',
      author_email='bertvs@gmail.com',
      packages=['funniest'],
      install_requires=[
          'os',
          'sys',
          'getopt',
          'datetime',
          'pandas',
          'collections',
          'shutil'
      ],
      zip_safe=False)
