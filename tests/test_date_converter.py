from date_converter.date_converter import date_converter


def test_date_converter():
    """Test date_converter"""
    dt1 = '2020-01-01'
    dt_num = date_converter(dt1)
    assert dt1 == date_converter(dt_num), 'Converter failed!'
