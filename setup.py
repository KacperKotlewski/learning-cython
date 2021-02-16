from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

ext_modules = [
    Extension("henlo.wrapper",
        sources=[
            "henlo/wrapper.pyx",
            "henlo/lib/henlo.cpp"
        ],
        # include_dirs=["henlo/lib"],
        # depends=["henlo/lib/henlo.h"],
        # extra_compile_args=['/openmp'],
        # extra_link_args=['/openmp'],
        # language="c++",
    ),
    Extension("henlo.subpkg.util",
        sources=[
            "henlo/subpkg/util.pyx",
        ],
    )
]
setup(
    ext_modules=cythonize(ext_modules),
    zip_safe=False,
    name='hw',
    version='0.1',
    packages=['cython'],
    url='lols',
    license='MIT',
    author='kacpe',
    author_email='me@xd',
    description='test'
)
