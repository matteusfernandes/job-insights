import pytest
from src.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {"max_salary": 5000, "min_salary": 1200, "date_posted": "2020-05-07"},
        {"max_salary": 10000, "min_salary": 200, "date_posted": "2020-06-12"},
        {"max_salary": 15000, "min_salary": 500, "date_posted": "2020-06-19"},
    ]

    error = "wrong_criteria"

    with pytest.raises(ValueError, match=f'invalid sorting criteria: {error}'):
        sort_by(jobs, error)
