from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

ext_modules = [
    Extension("henlo",
         ["henloTest.pyx", "includes/henlo.cpp"],
         include_dirs=["includes"],
         depends=["includes/henlo.h"],
        extra_compile_args=['/openmp'],
        extra_link_args=['/openmp'],
    )
]
setup(
    ext_modules=cythonize(ext_modules),
    name='nauka',
    version='0.1',
    packages=['cython'],
    url='lols',
    license='MIT',
    author='kacpe',
    author_email='me@xd',
    description='test'
)
