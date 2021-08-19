import setuptools


def readme():
    try:
        with open('docs/README.md') as f:
            return f.read()
    except IOError:
        return ''


setuptools.setup(
    name="dearpygui_ext",
    version="0.1.1",
    author="Jonathan Hoffstadt and Preston Cothren",
    author_email="jonathanhoffstadt@yahoo.com",
    description='Dear PyGui Extensions: Extensions for Dear PyGui',
    long_description=readme(),
    long_description_content_type="text/markdown",
    url='https://github.com/hoffstadt/DearPyGui',          # Optional
    packages=['dearpygui_ext'],
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Education',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ),
)