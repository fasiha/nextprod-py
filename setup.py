from setuptools import setup

setup(
    name='nextprod',
    version='1.0',
    description="Port of Julia's nextprod",
    author='Ahmed Fasih',
    author_email='ahmed@aldebrn.me',
    url='https://github.com/fasiha/nextprod-py',
    license='Unlicense',
    py_modules=['nextprod'],
    test_suite='nose.collector',
    tests_require=['nose'],
    zip_safe=True,
)