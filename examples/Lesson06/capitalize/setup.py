from setuptools import setup 

setup(name="capitalize",
      version="0.0.1",
      packages=["capitalize"],
      # scripts=['bin/cap_script.py'],
      entry_points={'console_scripts': ['cap_script=capitalize.main:main']},
      include_package_data=True,
      package_data={'capitalize': ['cap_data.txt']}
      )




