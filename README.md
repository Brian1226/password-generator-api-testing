# Password Generator API Testing

This project involves testing the Password Generator API provided by [API Ninjas](https://api-ninjas.com/api/passwordgenerator). It uses the Requests library to send a GET request to the API and leverages pytest for unit testing. Testings include mocking to simulate API responses and validating the functionality of the function under test, and ensuring proper error handling.

## Project Structure

- `src/app.py`: Contains the implementation of the password generation function using the API.
- `tests/test_app.py`: Contains the test cases for verifying the functionality of the `get_password` function.

## Installation
1. Get a free API key at https://api-ninjas.com/
2. Clone the repository
   ```bash
   git clone https://github.com/Brian1226/password-generator-api-testing.git
   ```
3. Install these dependencies
   ```bash
   pip install requests python-dotenv pytest
   ```
4. Create a `.env` file in the root directory and enter your API key
   ```bash
   API_KEY = your_api_key_here
   ```

## Usage
- To run the application and generate a random password, use `python src/app.py`
- To run the tests, use `python -m pytest`

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
