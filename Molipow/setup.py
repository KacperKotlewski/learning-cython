from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

ext_modules = [
    Extension("cwork",
              ["barf/cwork.pyx", "barf/cpp_code/work.cpp"],
              #include_dirs=[""],
              #depends=["work.h"],
              #extra_compile_args=['/openmp'],
              #extra_link_args=['/openmp'],
              )
]

setup(
    name='jebaczycie',
    version='N/A',
    packages=[''],
    url='N/A',
    license='N/A',
    author='NOIDEA',
    author_email='N/A',
    ext_modules = cythonize(ext_modules),
    description='N/A'
)
