import pytest
import unittest.mock as mock
import requests
import src.app as app


@mock.patch('src.app.requests.get')                                     # replaces'requests.get' with 'mock_get', and passes that mock object as argument
def test_get_password(mock_get):
    mock_response = mock.Mock()                                         # creates mock response object
    mock_response.status_code = requests.codes.ok                       # simulates successful HTTP response
    mock_response.json.return_value = {'random_password': "X4s$g?3F"}   # simulates JSON payload returned by API
    mock_get.return_value = mock_response                               # any call to 'requests.get' within this test returns 'mock_response' object
    data = app.get_password(8)                                          # call function under test
    assert data == "X4s$g?3F"                                           # asserts that the result from function under test is equal to specified string


@mock.patch('src.app.requests.get')
def test_get_password_error(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = requests.codes.bad_request              # simulates unsuccessful HTTP response
    mock_response.raise_for_status.side_effect = requests.HTTPError     # simulates raising HTTPError when raise_for_status is called
    mock_get.return_value = mock_response                               
    with pytest.raises(requests.HTTPError):                             # assert that function under test raises HTTPError
        app.get_password(8)
