import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

install_requires=[
    "Django >= 1.4",
    "mongoengine",
    "restfulie",
    "buscape"
]

tests_require = ['selenium',
                 'mock']


setup(
    name = "br.mib.quantocustapara",
    version = "0.0.1",
    author = "Thiago Pagonha",
    author_email = "thi.pag@gmail.com",
    description = ("Prototipo do software Quanto Custa Para"),
    license = "Proprietary",
    keywords = "quanto custa para",
    packages=['br.mib.quantocustapara'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: Proprietary",
    ],
    install_requires=install_requires,
    tests_require=tests_require,
    include_package_data=True,
    zip_safe=False,
    dependency_links = [
        "https://github.com/downloads/thiagopa/QuantoCustaParaDjango/buscape.py#egg=buscape"
    ]
)