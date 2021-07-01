# Getting Started

Follow the instructions below to activate virtual environment and set up the renaming configurations.

Setup up virtual environment and install libraries
```
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
```

Edit the renaming configrations in `rename_conf.yml`
```
- paths: 
    - path1
    - path2
  renaming_rules:
    - regex: ".*file name 1.*"
      target_filename: "new_file_name_1.csv"
    - regex: ".*file name 2.*"
      target_filename: "new_file_name_1.csv"

- path: path3
  renaming_rules:
    - regex: ".*file name 3.*"
      target_filename: "new_file_name_3.csv"
```

After setting up the configuration file. You can run the server by executing the `run.bat` file.
