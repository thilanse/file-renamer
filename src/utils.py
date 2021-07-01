import yaml

def read_yaml(file_path):
    """
    Reads yaml file and returns data in python dictionary format.
    """

    with open(file_path, 'r') as yaml_file:
        try:
            return yaml.safe_load(yaml_file)
        except yaml.YAMLError as err:
            print(err)