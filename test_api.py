import pytest
from unittest.mock import patch
from api import lookup, minimum_price, maximum_price

@pytest.fixture
def mock_api_key():
    return "HEKMRH828HI04N23"

@patch("requests.get")
def test_lookup(mock_get, mock_api_key):
    mock_get.return_value.status_code = 200  # Mock successful response
    mock_get.return_value.json.return_value = {
        "Meta Data": {"Information": "Some Info"},
        "Time Series (Daily)": {
            "2025-03-28": {
                "1. open": "100",
                "2. high": "105",
                "3. low": "95",
                "4. close": "100",
                "5. volume": "10000"
            }
        }
    }
    result = lookup("IBM", "2025-03-28", mock_api_key)
    assert "Meta Data" in result
    assert "Time Series (Daily)" in result
    assert "2025-03-28" in result["Time Series (Daily)"]
    assert result["Time Series (Daily)"]["2025-03-28"]["1. open"] is not None

@patch("requests.get")
def test_min_price(mock_get, mock_api_key):
    mock_get.return_value.status_code = 200  # Mock successful response
    mock_get.return_value.json.return_value = {
        "Meta Data": {"Information": "Some Info"}, # Needed or function will fail
        "Time Series (Daily)": {
            "2025-03-28": {
                "3. low": "95"
            },
            "2025-03-27": {
                "3. low": "90"
            },
            "2025-03-26": {
                "3. low": "85"
            },
            "2025-03-25": {
                "3. low": "80"
            },
            "2025-03-24": {
                "3. low": "75"
            }
        }
    }
    result = minimum_price("IBM", 5, mock_api_key)
    assert isinstance(result, float)

@patch("requests.get")
def test_max_price(mock_get, mock_api_key):
    mock_get.return_value.status_code = 200  # Mock successful response
    mock_get.return_value.json.return_value = {
        "Meta Data": {"Information": "Some Info"}, 
        "Time Series (Daily)": {
            "2025-03-28": {
                "2. high": "105"
            },
            "2025-03-27": {
                "2. high": "110"
            },
            "2025-03-26": {
                "2. high": "115"
            },
            "2025-03-25": {
                "2. high": "120"
            },
            "2025-03-24": {
                "2. high": "125"
            }
        }
    }
    result = maximum_price("IBM", 5, mock_api_key)
    assert isinstance(result, float)

