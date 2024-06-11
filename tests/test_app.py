import pytest
import unittest.mock as mock
import requests
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import src.app as app


@mock.patch('requests.get') # replaces/intercepts 'requests.get' with 'mock_get'
def test_get_password(mock_get):
    mock_response = mock.Mock() # creates mock response object
    mock_response.status_code = 200 # simulates successful HTTP response
    mock_response.json.return_value = {'random_password': "X4s$g?3F"} # simulates JSON payload returned by API
    mock_get.return_value = mock_response # any call to 'requests.get' within this test returns 'mock_response' object
    data = app.get_password(8) # call function under test
    assert data == "X4s$g?3F" # asserts that the result from function under test is equal to specified string


@mock.patch('requests.get')
def test_get_password_error(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 400
    mock_get.return_value = mock_response
    with pytest.raises(requests.HTTPError):
        app.get_password(8)
