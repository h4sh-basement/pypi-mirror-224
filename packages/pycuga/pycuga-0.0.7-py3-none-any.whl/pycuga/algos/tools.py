import os


def read_files_as_strings(directory_path):
    file_string = " #include <cuda_runtime.h> \n "
    print(directory_path)
    for dirpath, _, filenames in os.walk(directory_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            with open(file_path, 'r') as file:
                file_string+= file.read()
            file_string+="\n"
    return file_string