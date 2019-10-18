import file_utils

def test_safe_file_read():
    # yml tests:
    yml_reading = file_utils.safe_file_read("read_test.yml", "yml")
    assert yml_reading == [{"nameOfUser": "Matt-Gleich"}]

    # json tests:
    json_reading = file_utils.safe_file_read("read_test.json", "json")
    assert json_reading == {'nameOfUser': 'Matt-Gleich'}

    # txt tests:
    txt_reading = file_utils.safe_file_read("read_test.txt", "txt")
    assert txt_reading == "Matt-Gleich"
    