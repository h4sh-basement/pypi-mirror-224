from setuptools import setup

name = "types-pexpect"
description = "Typing stubs for pexpect"
long_description = '''
## Typing stubs for pexpect

This is a PEP 561 type stub package for the `pexpect` package. It
can be used by type-checking tools like
[mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/),
PyCharm, etc. to check code that uses
`pexpect`. The source for this package can be found at
https://github.com/python/typeshed/tree/main/stubs/pexpect. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/main/README.md for more details.
This package was generated from typeshed commit `22b055a147b5d672bf7e1f58cc6bf52cc526b35f` and was tested
with mypy 1.4.1, pyright 1.1.320, and
pytype 2023.7.21.
'''.lstrip()

setup(name=name,
      version="4.8.0.1",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/pexpect.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=[],
      packages=['pexpect-stubs'],
      package_data={'pexpect-stubs': ['ANSI.pyi', 'FSM.pyi', '__init__.pyi', '_async.pyi', 'exceptions.pyi', 'expect.pyi', 'fdpexpect.pyi', 'popen_spawn.pyi', 'pty_spawn.pyi', 'pxssh.pyi', 'replwrap.pyi', 'run.pyi', 'screen.pyi', 'spawnbase.pyi', 'utils.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
