import printing_utils

def test_print_with_time():
    """Test for the print_with_time function in the /src/printing_utils.py file
    """
    printing_utils.print_with_time("Here is a message in blue font", 0, "blue")
    assert True == True # Required to have assert. We aren't checking output for this function, just that it runs