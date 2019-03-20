import setuptools
from distutils.core import setup
from src import __version__

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='timerpy',
    version=__version__,
    description=long_description.split('\n')[1],
    author='ChsHub',
    author_email='christian1193@web.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ChsHub/timerpy",
    packages=['src'],
    license='MIT License',
    classifiers=['Programming Language :: Python :: 3']
)
# C:\Python37\python.exe setup.py sdist bdist_wheel
# C:\Python37\python.exe -m twine upload dist/*