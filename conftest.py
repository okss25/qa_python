import pytest

from test_book_collector import BooksCollector
@pytest.fixture
def collector():
    return BooksCollector()