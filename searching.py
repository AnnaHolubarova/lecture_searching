import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    if field not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None
    
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as json_file:
        data = json.load(json_file)
    return data[field]

def linear_search(sequence, number):
    """
    komentar
    """
    result = {"positions":[], "count": 0}
    for idx in range(len(sequence)):
        if sequence[idx] == number:
            result["positions"].append(idx)
            result["count"] = result["count"] + 1
    return result

def pattern_search(sequence, pattern):
    """
    komentar
    """
    result = set()
    for idx in range(len(sequence)):
        if sequence[idx:idx+len(pattern)] == pattern:
            result.add(idx)

    return result

        
                    


def main():
   unordered_data = read_data("sequential.json", "unordered_numbers")
   print(unordered_data)
   dictionary = linear_search(unordered_data, 5)
   print(dictionary)
   dna = read_data("sequential.json", "dna_sequence")
   pattern = pattern_search(dna, "ATA")
   print(pattern)

if __name__ == '__main__':
    main()