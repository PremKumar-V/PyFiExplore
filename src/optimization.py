from variables import Variable
from hashmap import Hashmap

variable = Variable()


def search_file(search_term):
    hashmap = Hashmap(variable.data_file_path, variable.search_path)

    file_list = hashmap.create_json_file()

    return file_list[search_term]
