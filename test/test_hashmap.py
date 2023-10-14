import pytest

try:
    from src.hashmap import Hashmap
    from src.variables import Variable

    variable = Variable()
    hashmap = Hashmap(variable.data_file_path)
except ModuleNotFoundError or ImportError as e:
    pass


class TestHashMap:
    def test_false_find_json_file(self):
        assert hashmap.find_json_file("C:\\Users\\NoFiles") == False

    def test_false_load_json_file(self):
        assert (
            hashmap.load_json_file("C:\\Users\\NoFiles.json")
            == "Error in Loading Json File: File Not Found"
        )

        assert (
            hashmap.load_json_file("C:\\Users\\NoFiles.text")
            == "Error in Loading Json File: File Not Found"
        )

    def test_create_json_file(self):
        file_list = hashmap.create_json_file(
            variable.search_path, variable.data_file_path
        )
        assert not isinstance(file_list, list)
        assert isinstance(file_list, dict)


if __name__ == "__main__":
    pytest.main(["-v", "test\\test_hashmap.py"])
