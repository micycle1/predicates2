import ast
from setuptools import setup, Extension
import os
import sys
try:
    from Cython.Build import cythonize
    cython_available = True
except ImportError:
    cython_available = False

if not cython_available:
    raise RuntimeError("Building geompreds requires Cython>=3.0. Use `pip install .` so build dependencies are installed automatically, or install manually with `pip install 'Cython>=3.0'`.")

def get_version():
    """
    Gets the version number. Pulls it from the source files rather than
    duplicating it.
    """
    # we read the file instead of importing it as root sometimes does not
    # have the cwd as part of the PYTHONPATH
    fn = os.path.join(os.path.dirname(__file__), 'src', 'geompreds', '__init__.py')
    try:
        with open(fn, "r", encoding="utf-8") as version_file:
            lines = version_file.readlines()
    except IOError:
        raise RuntimeError("Could not determine version number"
                           "(%s not there)" % (fn))
    version = None
    for l in lines:
        # include the ' =' as __version__ might be a part of __all__
        if l.startswith('__version__ =', ):
            version = ast.literal_eval(l.split("=", 1)[1].strip())
            break
    if version is None:
        raise RuntimeError("Could not determine version number: "
                           "'__version__ =' string not found")
    return version

# Platform specifics
# ==================
# Linux (2.x and 3.x)     'linux2'
# Windows                 'win32'
# Windows/Cygwin          'cygwin'
# Mac OS X                'darwin'
# OS/2                    'os2'
# OS/2 EMX                'os2emx'
# RiscOS                  'riscos'
# AtheOS                  'atheos'
macros = []
args = []
if sys.platform.startswith('win32') or sys.platform.startswith('cygwin'):
    macros = [("CPU86", 1)]
elif sys.platform.startswith('linux'):
    macros = [('LINUX',1), ]
    # for GCC: full ieee754 compliance
    # see: https://gcc.gnu.org/wiki/FloatingPointMath
    args = ["-frounding-math","-fsignaling-nans", "-O0"]

# cythonize the source
ext_modules = cythonize([Extension("geompreds._geompreds",
    define_macros = macros,
    sources = ["src/geompreds/_geompreds.pyx",
        "src/geompreds/pred.c"],
    extra_compile_args=args,
    extra_link_args=args,
    include_dirs=['src/geompreds'])], build_dir="build")


if __name__ == "__main__":
    setup(
        name = "geompreds",
        version = get_version(),
        author = "Martijn Meijers",
        author_email = "b.m.meijers@tudelft.nl",
        description = ("Adaptive Precision Floating-Point Arithmetic and "
                       "Fast Robust Predicates for Computational Geometry "
                       "for Python"),
        license = "MIT license",
        url = "https://github.com/bmmeijers/predicates",
        package_dir = {'':'src'},
        packages = ['geompreds',],
        ext_modules = ext_modules,
        test_suite="geompreds.tests",
        classifiers = [
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "Intended Audience :: Information Technology",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python :: 3.12",
            "Programming Language :: Cython",
            "Topic :: Software Development :: Libraries",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Topic :: Scientific/Engineering :: GIS",
            "Operating System :: POSIX :: Linux",
            "Operating System :: Microsoft :: Windows",
        ],
    )
