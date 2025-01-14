#!/usr/bin/env python
# setup.py generated by flit for tools that don't yet use PEP 517

from distutils.core import setup

packages = \
['pyconverters_newsml']

package_data = \
{'': ['*']}

package_dir = \
{'': 'src'}

install_requires = \
['pymultirole-plugins>=0.5.0,<0.6.0',
 'pandas>=1.2.3,<=1.3.5',
 'openpyxl==3.0.7',
 'beautifulsoup4',
 'inscriptis==1.2']

extras_require = \
{'dev': ['flit', 'pre-commit', 'bump2version'],
 'docs': ['sphinx',
          'sphinx-rtd-theme',
          'm2r2',
          'sphinxcontrib.apidoc',
          'jupyter_sphinx'],
 'test': ['pytest>=7.0.0',
          'pytest-cov',
          'pytest-flake8',
          'pytest-black',
          'requests_cache',
          'flake8==3.9.2',
          'tqdm',
          'tox',
          'pymongo',
          'ssh_pymongo',
          'scikit-learn',
          'requests_cache==0.7.5',
          'requests-futures==1.0.0',
          'bidict',
          'pyenchant',
          'deepl',
          'reverso-api',
          'python-Levenshtein',
          'thefuzz[speedup]']}

entry_points = \
{'pyconverters.plugins': ['newsml = '
                          'pyconverters_newsml.newsml:NewsMLConverter']}

setup(name='pyconverters-newsml',
      version='0.5.197',
      description='NewsML converter (AFP news)',
      author='Olivier Terrier',
      author_email='olivier.terrier@kairntech.com',
      url='https://github.com/oterrier/pyconverters_newsml/',
      packages=packages,
      package_data=package_data,
      package_dir=package_dir,
      install_requires=install_requires,
      extras_require=extras_require,
      entry_points=entry_points,
      python_requires='>=3.8',
     )
