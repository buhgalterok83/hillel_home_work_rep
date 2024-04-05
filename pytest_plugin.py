import pytest

def pytest_configure(config):
    config.addinivalue_line(
        "markers", "webtest: mark the test as a web test"
    )
#запустить тесты с помощью команды: python setup.py test 



