from setuptools import setup

setup(
    name='socialize',
    version='1.0.0',
    description='The official command-line client of socialize',
    author='Dominic Monn',
    author_email='monn.dominic@gmail.com',
    url='http://socialize.dmonn.ch',
    zip_safe=False,
    license='BSD',
    platforms=['OS Independent'],
    py_modules=['socialize'],
    install_requires=[
        'Click',
        'requests',
    ],
    entry_points='''
        [console_scripts]
        socl=socialize.router:init
    ''',
)
