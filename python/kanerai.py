import sys
# All info about what they're going to ask about
#
# 1. Down

# Make a Python script to download a file
import requests
import os

def download_file_demo():
    file_url = "https://699340.youcanlearnit.net/image001.jpg"

    response = requests.get(file_url)
    filename = os.path.basename(file_url)
    with open(f"./{filename}", "wb") as f:
        f.write(response.content)

# String/file manipulation
'''
readline vs readlines
'''
def file_demo():

    filename = "test.txt"

    # readlines() - reads the whole file

    # Loop through each line in a file
    lines = []
    with open(filename, 'r') as f:
        for l in f:
            lines.append(l.strip())
    #print(lines)
    lines = None

    # spin loop that processes for 30 seconds
    # might need a lot of memory

    # Read the file 5 bytes at a time 5 bytes = 5 ASCII characters
    lines = []
    with open(filename, 'r') as f:
        while True:
            part = f.read(5) # .read(n) reads n number bytes at the time counting the /n as one byte
            if not part:
                break
            lines.append(part)

    # List of file functions:
    # |-----------------+----------------------------------------------------|
    # | function        | notes                                              |
    # |-----------------+----------------------------------------------------|
    # | f.readlines()   | reads whole file, returns list of lines            |
    # | f.readline([n]) | reads n bytes or until EOL/EOF, returns text       |
    # | f.read([n])     | reads n bytes or until EOF, returns text           |
    # |-----------------+----------------------------------------------------|
    # | f.seek(n)       | moves read position to n bytes into file           |
    # | f.tell()        | returns current position in file                   |
    # | f.close()       | closes file, good to do if you're not a psychopath |
    # |-----------------+----------------------------------------------------|
    
    # A file has one the following structure
    # len_metadata(will always be an integer) + '\n'
    # meta \n
    # data meta \n
    # metadata
    # data
    #
    # Print out the metadata and data separately
    lines = []
    with open(filename, 'r') as f:
        len_metadata = f.readline().strip() # "100"
        offset_metadata = len(len_metadata) + 1 # seek also considers /n as one byte
        print(f'f.tell() = {f.tell()}')
        print(f'offset_metadata = {offset_metadata}')
        f.seek(offset_metadata)

        metadata = f.read(int(len_metadata))
        # metadata = ""
        # for l in f:
        #     if len(metadata) < int(len_metadata):
        #         metadata += l
        #     if len(metadata) == int(len_metadata):
        #         break

        print("metadata:", metadata)


        offset = int(len_metadata) + len(len_metadata) + 1

        print(f'f.tell() = {f.tell()}')
        print(f'offset = {offset}')
        
        f.seek(offset)
        data = f.read()
        print(f"'{data}'")

        #for l in f:
        #    lines.append(l)
    
    print(lines)

def parse_csv(filename):
    """
    Read {filename} as csv data and return a list of lists representing the data
    
    Assume there is a header row
    """
    data = []
    with open(filename, 'r') as f:
        fields = f.readline()
        for l in f:
            values = l.strip()
            data.append(values.split(","))
    return data

# describe memory allocation of a program 
'''
in python, memory is allocated in a heap
python objects like variables and data are stored on this heap and once in while, garbage collector cleans up unused objects 
'''

# What is a generator in Python?
'''
a function that returns an iterator containing items (or iterable collection of items). Each item is generated as needed using keyword yield
'''

class A:
   pass

if __name__ == '__main__':
    #download_file_demo()
    #file_demo()
    #print(parse_csv('test.csv'))

    a = dict()
    #b = a
    #c = [b, b, b]

    #a_obj = A()
    #a_obj.v = a

    print(sys.getrefcount(a))
    
