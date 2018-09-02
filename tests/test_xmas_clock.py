from datetime import datetime

from xmasclock import get_next_xmas, count_days_til_xmas, count_seconds_til_xmas

before_xmas = datetime(2000, 1, 1)
xmas_eve = datetime(2000, 12, 24)
xmas_day = datetime(2000, 12, 25)
after_xmas = datetime(2000, 12, 26)
next_xmas_day = datetime(xmas_day.year + 1, xmas_day.month, xmas_day.day)


def test_get_next_xmas():
    assert xmas_day == get_next_xmas(before_xmas)
    assert xmas_day == get_next_xmas(xmas_eve)
    assert next_xmas_day == get_next_xmas(xmas_day)
    assert next_xmas_day == get_next_xmas(after_xmas)


def test_count_days_til_xmas():
    assert 1 == count_days_til_xmas(xmas_eve)
    assert 365 == count_days_til_xmas(xmas_day)
    assert 364 == count_days_til_xmas(after_xmas)


def test_count_seconds_til_xmas():
    assert 86400 == count_seconds_til_xmas(xmas_eve)
    assert 31536000 == count_seconds_til_xmas(xmas_day)
    assert 31449600 == count_seconds_til_xmas(after_xmas)
