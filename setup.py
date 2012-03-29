from distutils.core import setup
import sys
sys.path.append('fvisgallery')
import fvisgallery

setup(name='fvisgallery',
      version='1.0',
      author='Daniel Ampuero Anca',
      author_email='danielmaxx@gmail.com',
      url='www.lol.com',
      download_url='www.lol.com/download',
      description='An special implementation for uploading zipped pictures',
      packages=['fvisgallery'],
      requires=['django (>=1.3)'],
      keywords='gallery zipped files',
      license='GPL',
      classifiers=['Development Status :: Alpha',
                   'Intended Audience :: Developers',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 2.6+',
                   'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
                   'License :: OSI Approved :: GNU Affero General Public License v3',
                   'Topic :: Internet',
                   'Topic :: Scientific/Engineering :: GIS',
                  ],
     )
