import setuptools
from distutils.core import setup
from timerpy import __version__

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='timerpy',
    version=__version__,
    description=long_description.split('\n')[1],
    author='ChsHub',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ChsHub/timerpy",
    packages=['timerpy'],
    license='MIT License',
    classifiers=['Programming Language :: Python :: 3.3', 'Topic :: Software Development', 'Topic :: Utilities']
)
# C:\Python37\python.exe setup.py sdist bdist_wheel
# C:\Python37\python.exe -m twine upload dist/*