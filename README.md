![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/EStog/fizzbuzz?include_prereleases) ![python|3.9](https://img.shields.io/badge/python-3.9-blue) ![repo size](https://img.shields.io/github/repo-size/EStog/fizzbuzz) ![license|MIT](https://img.shields.io/github/license/EStog/fizzbuzz) ![tests](https://github.com/EStog/fizzbuzz/actions/workflows/tests.yml/badge.svg) ![docs](https://github.com/EStog/fizzbuzz/actions/workflows/docs.yml/badge.svg) ![github-pages](https://img.shields.io/github/deployments/EStog/pathex/github-pages?label=github-pages) [![codecov](https://codecov.io/gh/EStog/fizzbuzz/branch/main/graph/badge.svg?token=JYVFXZ4LYJ)](https://codecov.io/gh/EStog/fizzbuzz)

# FizzBuzz brainstorm!

[FizzBuzz](https://wiki.c2.com/?FizzBuzzTest) is a simple test used in programming interviews. Pleasing the friends from [cuban.engineer](https://cuban.engineer/), this repository is just a personal brainstorming on the subject. You can see the [project documentation](https://estog.github.io/fizzbuzz) for more details.

To use any part of the project first run in project root directory:

```shell
pip install -r ./requirements.txt
```

In case you need to generate offline HTML documentation just run in project root directory:

```shell
pip install -r ./docs/requirements.txt
./build_docs.sh html
```

To see other available formats run `./build_docs.sh`. Documentation is built using [Sphinx](https://www.sphinx-doc.org/).

In case you want to run the tests, execute in project root directory:

```shell
pip install -r ./tests/requirements.txt
./run_tests.sh
```
