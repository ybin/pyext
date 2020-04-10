from distutils.core import setup, Extension

module1 = Extension('demo',
                    sources=['demo_module.c'])

setup(name='a demo extension module',
      version='1.0',
      description='This is a demo package',
      ext_modules=[module1])
