# Python reduce function
# Pure functions do one thing and one thing alone and has no side effects
# reduce is an implementation of mathematical concept fold or reduction
# often used in functional programming
# reduce() follows the SOLID principle

# reduce used for sum()
# first class object
# input for reduce is a function
# timeit package python

from operator import add 

def reduce(func, items):
  
  val = func(items[0], items[1])
  for item in items[2:]:
    val = func(val,item)
  return val


import unittest
class ReduceTestCase(unittest.TestCase):
  def test_reduce_to_sum(self):
    self.assrtEqual(13, reduce(add, [4,2,7]))



The monkeypatch fixture provides these helper methods for safely patching and mocking functionality in tests:

monkeypatch.setattr(obj, name, value, raising=True)
monkeypatch.delattr(obj, name, raising=True)
monkeypatch.setitem(mapping, name, value)
monkeypatch.delitem(obj, name, raising=True)
monkeypatch.setenv(name, value, prepend=False)
monkeypatch.delenv(name, raising=True)
monkeypatch.syspath_prepend(path)
monkeypatch.chdir(path)


# contents of our original code file e.g. code.py
import os


def get_os_user_lower():
    """Simple retrieval function.
    Returns lowercase USER or raises OSError."""
    username = os.getenv("USER")

    if username is None:
        raise OSError("USER environment is not set.")

    return username.lower()


This behavior can be moved into fixture structures and shared across tests:

# contents of our test file e.g. test_code.py
import pytest


@pytest.fixture
def mock_env_user(monkeypatch):
    monkeypatch.setenv("USER", "TestingUser")


@pytest.fixture
def mock_env_missing(monkeypatch):
    monkeypatch.delenv("USER", raising=False)


# notice the tests reference the fixtures for mocks
def test_upper_to_lower(mock_env_user):
    assert get_os_user_lower() == "testinguser"


def test_raise_exception(mock_env_missing):
    with pytest.raises(OSError):
        _ = get_os_user_lower()



REST stands for representational state transfer and is a software architecture style that defines a pattern for client and server communications over a network. REST provides a set of constraints for software architecture to promote performance, scalability, simplicity, and reliability in the system.

REST defines the following architectural constraints:

Stateless: The server won’t maintain any state between requests from the client.
Client-server: The client and server must be decoupled from each other, allowing each to develop independently.
Cacheable: The data retrieved from the server should be cacheable either by the client or by the server.
Uniform interface: The server will provide a uniform interface for accessing resources without defining their representation.
Layered system: The client may access the resources on the server indirectly through other layers such as a proxy or load balancer.
Code on demand (optional): The server may transfer code to the client that it can run, such as JavaScript for a single-page application.
Note, REST is not a specification but a set of guidelines on how to architect a network-connected software system.


HTTP method	API endpoint	Description
GET	/customers	Get a list of customers.
GET	/customers/<customer_id>	Get a single customer.
POST	/customers	Create a new customer.
PUT	/customers/<customer_id>	Update a customer.
PATCH	/customers/<customer_id>	Partially update a customer.
DELETE	/customers/<customer_id>	Delete a customer.
