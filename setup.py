from setuptools import setup

setup(name='configuration.py',
      version='0.1',
      description='Easy config management for python applications',
      url='http://github.com/Ferroman/configuration.py',
      author='Frankovskyi Bogdan',
      author_email='bfrankovskyi@gmail.com',
      license='MIT',
      packages=['configuration_py'],
      test_suite='nose.collector',
      tests_require=['behave', 'sure', 'nose', 'mock'],
      zip_safe=False)