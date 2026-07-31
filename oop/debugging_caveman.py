import json
import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))

# For the sake of this lab, pretend that you don't already have access to the data in the json file.
"""
create a json file named `debugging_caveman.json` in the same directory.

{
    "pets": ["ada", "Kara", "OLiver", "Rosie", "Ozzie"]
}

"""

def fetch_dataset(source: str = os.path.join(current_dir, 'debugging_caveman.json')) -> list:
    with open(source, 'r') as dataset:
        return json.loads(dataset.read().encode('utf-8'))

def normalize_name(dataset, key: str) -> list:
    ''' Removes white space around the text and converts to title case.
        
        Args:
            dataset | a dictionary-like structure.
            key     | the key to normalize in the dataset.
    '''
    print(dataset) # The dataset displayed to std output unveils the missing key named `pets`
    try:
        return [ name.strip().title() for name in dataset[key] ]
    except KeyError:
        return []
    except Exception as e:
        print(f"Error: {e}")
        raise

if __name__ == '__main__':

    if len(sys.argv) >= 2:
        clean_dataset = normalize_name(fetch_dataset(), sys.argv[1])

        if clean_dataset:
            print('The cleaned dataset: ', end='')
            print(*clean_dataset, sep=', ')
        else:
            print('Data not found')
    else:
        print('Please provide a key to normalize as a command line argument.')
