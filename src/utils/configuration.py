import os
import configparser

config_file = '../config/conf.ini'
config = configparser.ConfigParser()
config.read(config_file)

### Configuration

DIR_DATA_TOP = config['path']['DIR_DATA_TOP']
DIR_MODEL_TOP = config['path']['DIR_MODEL_TOP']

# Define Directories

DIR_DATA       = os.path.join(DIR_DATA_TOP, 'cache')
DIR_VOCAB      = os.path.join(DIR_DATA_TOP, 'vocab')
DIR_TOKEN      = os.path.join(DIR_MODEL_TOP, 'trained')

# Setup Directories

DIRs = {key:value for key, value in globals().items()}
for key, value in DIRs.items():
    if 'DIR_' in key:
        if os.path.isdir(value):
            print(f"Directory {value} exists.")
        else:
            print(f"Creating {value}...")
            os.makedirs(value)
            print(f" Succeeded!!!")
            
# Global Variables

SEED = config.getint('global', 'SEED')
