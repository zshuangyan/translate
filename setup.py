from setuptools import setup

setup(name='translate',
      packages=['translate'],
      entry_points = {
          'console_scripts': ['translate=translate.translate:command_line_runner']
      }
)
