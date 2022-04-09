# Python reduce function
# Pure functions do one thing and one thing alone and has no side effects
# reduce is an implementation of mathematical concept fold or reduction
# often used in functional programming
# reduce() follows the SOLID principle

# reduce used for sum()
# first class object
# input for reduce is a function
# timeit package python

# from operator import add 

# def reduce(func, items):
  
#   val = func(items[0], items[1])
#   for item in items[2:]:
#     val = func(val,item)
#   return val


# import unittest
# class ReduceTestCase(unittest.TestCase):
#   def test_reduce_to_sum(self):
#     self.assrtEqual(13, reduce(add, [4,2,7]))



# The monkeypatch fixture provides these helper methods for safely patching and mocking functionality in tests:

# monkeypatch.setattr(obj, name, value, raising=True)
# monkeypatch.delattr(obj, name, raising=True)
# monkeypatch.setitem(mapping, name, value)
# monkeypatch.delitem(obj, name, raising=True)
# monkeypatch.setenv(name, value, prepend=False)
# monkeypatch.delenv(name, raising=True)
# monkeypatch.syspath_prepend(path)
# monkeypatch.chdir(path)


# # contents of our original code file e.g. code.py
# import os


# def get_os_user_lower():
#     """Simple retrieval function.
#     Returns lowercase USER or raises OSError."""
#     username = os.getenv("USER")

#     if username is None:
#         raise OSError("USER environment is not set.")

#     return username.lower()


# This behavior can be moved into fixture structures and shared across tests:

# # contents of our test file e.g. test_code.py
# import pytest


# @pytest.fixture
# def mock_env_user(monkeypatch):
#     monkeypatch.setenv("USER", "TestingUser")


# @pytest.fixture
# def mock_env_missing(monkeypatch):
#     monkeypatch.delenv("USER", raising=False)


# # notice the tests reference the fixtures for mocks
# def test_upper_to_lower(mock_env_user):
#     assert get_os_user_lower() == "testinguser"


# def test_raise_exception(mock_env_missing):
#     with pytest.raises(OSError):
#         _ = get_os_user_lower()



# REST stands for representational state transfer and is a software architecture style that defines a pattern for client and server communications over a network. REST provides a set of constraints for software architecture to promote performance, scalability, simplicity, and reliability in the system.

# REST defines the following architectural constraints:

# Stateless: The server won’t maintain any state between requests from the client.
# Client-server: The client and server must be decoupled from each other, allowing each to develop independently.
# Cacheable: The data retrieved from the server should be cacheable either by the client or by the server.
# Uniform interface: The server will provide a uniform interface for accessing resources without defining their representation.
# Layered system: The client may access the resources on the server indirectly through other layers such as a proxy or load balancer.
# Code on demand (optional): The server may transfer code to the client that it can run, such as JavaScript for a single-page application.
# Note, REST is not a specification but a set of guidelines on how to architect a network-connected software system.


# HTTP method	API endpoint	Description
# GET	/customers	Get a list of customers.
# GET	/customers/<customer_id>	Get a single customer.
# POST	/customers	Create a new customer.
# PUT	/customers/<customer_id>	Update a customer.
# PATCH	/customers/<customer_id>	Partially update a customer.
# DELETE	/customers/<customer_id>	Delete a customer.



# The Python SQL Toolkit and Object Relational Mapper
# SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.

# It provides a full suite of well known enterprise-level persistence patterns, designed for efficient and high-performing database access, adapted into a simple and Pythonic domain language.


# A flat file is a file containing data with no internal hierarchy and usually no references to external files. Flat files contain human-readable characters and are very useful for creating and reading data. Because they don’t have to use fixed field widths, flat files often use other structures to make it possible for a program to parse text.

# For example, comma-separated value (CSV) files are lines of plain text in which the comma character separates the data elements. Each line of text represents a row of data, and each comma-separated value is a field within that row. The comma character delimiter indicates the boundary between data values.

# SQLAlchemy is a powerful database access tool kit for Python, with its object-relational mapper (ORM) being one of its most famous components, and the one discussed and used here.

# When you’re working in an object-oriented language like Python, it’s often useful to think in terms of objects. It’s possible to map the results returned by SQL queries to objects, but doing so works against the grain of how the database works. Sticking with the scalar results provided by SQL works against the grain of how Python developers work. This problem is known as object-relational impedance mismatch.

# The ORM provided by SQLAlchemy sits between the SQLite database and your Python program and transforms the data flow between the database engine and Python objects. SQLAlchemy allows you to think in terms of objects and still retain the powerful features of a database engine.



#  Database normalization, or the process of breaking apart data to reduce redundancy and increase integrity. When a database structure is extended with new types of data, having it normalized beforehand keeps changes to the existing structure to a minimum.

# Creating a Database Structure
# The brute force approach to getting the author_book_publisher.csv data into an SQLite database would be to create a single table matching the structure of the CSV file. Doing this would ignore a good deal of SQLite’s power.

# Relational databases provide a way to store structured data in tables and establish relationships between those tables. They usually use Structured Query Language (SQL) as the primary way to interact with the data.


# Sample Python code for sqlalchemy
# def main():
#     """Main entry point of program"""
#     # Connect to the database using SQLAlchemy
#     with resources.path(
#         "project.data", "author_book_publisher.db"
#     ) as sqlite_filepath:
#         engine = create_engine(f"sqlite:///{sqlite_filepath}")
#     Session = sessionmaker()
#     Session.configure(bind=engine)
#     session = Session()

#     # Get the number of books printed by each publisher
#     books_by_publisher = get_books_by_publishers(session, ascending=False)
#     for row in books_by_publisher:
#         print(f"Publisher: {row.name}, total books: {row.total_books}")
#     print()

#     # Get the number of authors each publisher publishes
#     authors_by_publisher = get_authors_by_publishers(session)
#     for row in authors_by_publisher:
#         print(f"Publisher: {row.name}, total authors: {row.total_authors}")
#     print()

#     # Output hierarchical author data
#     authors = get_authors(session)
#     output_author_hierarchy(authors)

#     # Add a new book
#     add_new_book(
#         session,
#         author_name="Stephen King",
#         book_title="The Stand",
#         publisher_name="Random House",
#     )
#     # Output the updated hierarchical author data
#     authors = get_authors(session)
#     output_author_hierarchy(authors)