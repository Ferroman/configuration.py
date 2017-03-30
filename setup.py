from setuptools import setup


def readme():
    try:
        import pypandoc
        description = pypandoc.convert('README.md', 'rst')
    except:
        description = '''Configuration.py is a library for configuration management in python apps. Its goal is to make
      configurations management as human-friendly as possible. It provides a simple `load` function that allows to load
      configuration for given environment from any supported formats.'''

    return description

setup(name='configuration.py',
      version='0.8.1',
      description='Easy config management for python applications',
      long_description=readme(),
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      url='http://github.com/Ferroman/configuration.py',
      author='Frankovskyi Bogdan',
      author_email='bfrankovskyi@gmail.com',
      license='MIT',
      packages=['configuration_py'],
      install_requires=['pyyaml',],
      test_suite='nose.collector',
      tests_require=['nose', 'mock', 'coverage'],
      zip_safe=False)