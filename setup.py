from setuptools import setup



setup(name='configuration.py',
      version='0.1',
      description='Easy config management for python applications',
      url='http://github.com/Ferroman/configuration.py',
      author='Frankovskyi Bogdan',
      author_email='bfrankovskyi@gmail.com',
      license='MIT',
      packages=['configuration_py'],
      install_requires=['pyyaml',],
      test_suite='nose.collector',
      tests_require=['sure', 'nose', 'mock', 'coverage'],
      zip_safe=False)