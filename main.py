
def books_collector():
    return BooksCollector()


NAME = 'Book Name'
WRONG_NAME = 'Wrong Name'


def test_add_book(books_collector):
    books_collector.add_new_book(NAME)
    assert books_collector.favorites == []
    assert books_collector.books_rating == {NAME: 1}


def test_add_book_twice(books_collector):
    books_collector.add_new_book(NAME)
    books_collector.add_new_book(NAME)
    assert books_collector.favorites == []
    assert books_collector.books_rating == {NAME: 1}


def test_add_rating_to_absent_book_fails(books_collector):
    books_collector.add_new_book(NAME)
    books_collector.set_book_rating(WRONG_NAME, 5)
    assert books_collector.favorites == []
    assert books_collector.books_rating == {NAME: 1}


def test_cant_set_rating_less_than_one(books_collector):
    books_collector.add_new_book(NAME)
    books_collector.set_book_rating(NAME, 0)
    assert books_collector.favorites == []
    assert books_collector.books_rating == {NAME: 1}


def test_cant_set_rating_greater_than_ten(books_collector):
    books_collector.add_new_book(NAME)
    books_collector.set_book_rating(NAME, 11)
    assert books_collector.favorites == []
    assert books_collector.books_rating == {NAME: 1}


def test_absent_book_has_no_rating(books_collector):
    books_collector.add_new_book(NAME)
    rating = books_collector.get_book_rating(WRONG_NAME)
    assert rating is None


def test_add_to_favorites(books_collector):
    books_collector.add_new_book(NAME)
    books_collector.add_book_in_favorites(NAME)
    assert books_collector.favorites == [NAME]
    assert books_collector.books_rating == {NAME: 1}


def test_add_to_favorites_fails_if_not_in_ratings(books_collector):
    books_collector.add_book_in_favorites(NAME)
    assert books_collector.favorites == []
    assert books_collector.books_rating == {}


def test_delete_from_favorites(books_collector):
    books_collector.add_new_book(NAME)
    books_collector.add_book_in_favorites(NAME)
    books_collector.delete_book_from_favorites(NAME)
    assert books_collector.favorites == []
    assert books_collector.books_rating == {NAME: 1}


def test_get_list_of_favorites_books(books_collector):
    books_collector.add_new_book(NAME)
    books_collector.add_book_in_favorites(NAME)
    assert books_collector.get_list_of_favorites_books() == [NAME]


def test_get_books_rating(books_collector):
    books_collector.add_new_book(NAME)
    assert books_collector.get_books_rating() == {NAME: 1}


def test_set_book_rating(books_collector):
    books_collector.add_new_book(NAME)
    books_collector.set_book_rating(NAME, 7)
    assert books_collector.books_rating == {NAME: 7}


def test_get_books_with_specific_rating(books_collector):
    books_collector.add_new_book(NAME)
    books_collector.add_new_book(WRONG_NAME)
    books_collector.add_new_book('Another Name')
    books_collector.set_book_rating(WRONG_NAME, 7)
    result = books_collector.get_books_with_specific_rating(1)
    assert [NAME, 'Another Name'] == result


def test_get_books_with_specific_rating_fails_if_no_books(books_collector):
    result = books_collector.get_books_with_specific_rating(1)
    assert [] == result


def test_get_books_with_specific_rating_fails_if_no_books_with_same(books_collector):
    books_collector.add_new_book(NAME)
    result = books_collector.get_books_with_specific_rating(9)
    assert [] == result


def test_get_books_with_specific_rating_fails_if_wrong_rating(books_collector):
    books_collector.add_new_book(NAME)
    result = books_collector.get_books_with_specific_rating(0)
    assert [] == result
