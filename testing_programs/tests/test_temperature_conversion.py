from testing_programs import temperature_conversion as temp


def test_temperature_conversion():
    assert temp.Util.temperature_conversion(C) == "1000 X 1"

