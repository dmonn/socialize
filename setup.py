from setuptools import setup, find_packages

setup(
    name='socialize',
    version='1.0.4',
    description='The official command-line client of socialize',
    author='Dominic Monn',
    author_email='monn.dominic@gmail.com',
    url='http://socialize.dmonn.ch',
    zip_safe=False,
    license='BSD',
    platforms=['OS Independent'],
    py_modules=['socialize'],
    packages=find_packages(),
    install_requires=[
        'Click',
        'requests',
    ],
    entry_points='''
        [console_scripts]
        socl=socialize.router:init
    ''',
)
