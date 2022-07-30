## Notes from [SO post](https://stackoverflow.com/a/67103294)
You need either
* setup.py
* setup.cfg and setup.py
* pyproject.toml
to create an installable Python project.

Tox becomes useful because you can install your project requirements separately from
your test requirements.

Flake8 placed as a pre-commit hook to safeguard the repo. It could be placed within
tox.ini as a testenv, but then it doesn't offer the same protection.

## Notes from [article](https://christophergs.com/python/2020/04/12/python-tox-why-use-it-and-tutorial/)
Tox helps solve the "it works on my machine" problem. So does Docker though right?
Can help test against multiple version of Python. It isolates environment variables too.
You need to explicitly pass environment variables.

Tox creates a series of virtual environments. Then installs dependencies for each, as
specified by the config. Runs the setup commands for the environments (also in config).
And then returns results from each environment to you.

* https://packaging.python.org/en/latest/tutorials/packaging-projects/#packaging-python-projects

## Github PAT stuff

For having terminal use new PAT: https://stackoverflow.com/a/70593153

## Pre-commit hooks

On MacOS run `brew install pre-commit`. Then test with `pre-commit run --all-files`.
You need to also run `pre-commit install` within the repository.


## TODO
- [ ] What other pre-commit hooks are worthwhile? https://pre-commit.com/hooks.html
- [ ] Read this https://christophergs.com/python/2020/04/12/python-tox-why-use-it-and-tutorial/ again
