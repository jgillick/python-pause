from distutils.core import setup

setup(
    name='pause',
    version=0.1,
    license=open('LICENSE.txt').read(),
    author='Jeremy Gillick',
    author_email='none@none.com',
    packages=['pause', 'pause.tests'],
    url='https://github.com/jgillick/python-pause',
    description='A timestamp-based sleep function for Python.',
    long_description=open('README.rst').read(),
    platforms='osx, posix, linux, windows',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Environment :: Console'
    ],
    keywords='sleep timestamp datetime'
)
