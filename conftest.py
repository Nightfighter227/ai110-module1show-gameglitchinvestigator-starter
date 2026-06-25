# Placing a conftest.py at the project root makes pytest add this directory to
# sys.path, so tests under tests/ can `import logic_utils` no matter how pytest is
# invoked (`pytest`, `python -m pytest`, or the IDE test runner).
