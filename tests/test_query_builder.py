#!/usr/bin/python3

from query_builder import QueryBuilder

@pytest.fixture
def first_and_second():
  return 'SELECT * FROM sample WHERE `first` = 1 AND `second` = 2'

def test_empty_get():
    query = QueryBuilder('sample')
    assert(query.to_sql() == 'SELECT * FROM sample')

def test_one_where():
    query = QueryBuilder('sample')
    query.where({'first': 1})
    assert(query.to_sql() == 'SELECT * FROM sample WHERE `first` = 1')

def test_two_where():
    query = QueryBuilder('sample')
    query.where({'first': 1})
    query.where({'second': 2})
    assert(query.to_sql() == first_and_second)

def test_one_where_two_conditions():
    query = QueryBuilder('sample')
    query.where({'first': 1, 'second': 2})
    assert(query.to_sql() == first_and_second)
