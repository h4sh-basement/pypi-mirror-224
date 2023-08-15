Before a release.
----------------
# set version number in setup.py, also in the config file of the documentation and init of the package
- [ ] setup.py
- [ ] gempy.__init__
> Note: in the config for sphinx~ this is taken from gempy.__init__

Requirements version
--------------------
- requirements.txt, optional_requirements.txt, dev_requirements.txt should either set minimum version and reject versions

Github release
--------------
    # add new tag
    $ git tag X.X -m "Add X.X tag for PyPI"
    # push git tag
    $ git push --tags origin master

PyPi release
------------
    #  First create the dist
    python3 setup.py sdist bdist_wheel

    # Second upload the distributions
    twine upload dist/*


### Type of commits:

- ENH: Enhancement, new functionality
- BUG: Bug fix
- DOC: Additions/updates to documentation
- TST: Additions/updates to tests
- BLD: Updates to the build process/scripts
- PERF: Performance improvement
- CLN: Code cleanup
