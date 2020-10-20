import json
from stage2.test_material import combined_standardized_result_sample

def store_list_to_file():
    ans = combined_standardized_result_sample()
    ans = json.dumps(ans)
    with open("fucku.txt", "w+", encoding="utf-8") as result_file:
        result_file.write(ans)

def read_file_to_list():
    with open("fucku.txt", "r", encoding="utf-8") as result_file:
        data = json.load(result_file)
        print(data)

# print(len(combined_standardized_result_sample()))
# read_file_to_list()


