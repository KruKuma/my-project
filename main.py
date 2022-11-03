import os
import mysql.connector
import yaml

sys_info = os.uname()
# print(sys_info)

user = ''
config_file_path = ''

# Determining which user is using the code
if sys_info[1] == 'DESKTOP-J6K5D38':
    user = 'james'
elif sys_info[1] == 'MacBook-Noussaiba.local':
    user = 'noussaiba'
elif sys_info[1] == 'NaphatskornsAir':
    user = 'earth'

# Writing the path to the user's config file
if user == 'james':
    config_file_path = "C:/Users/james/Documents/.ssh/"
elif user == 'noussaiba':
    config_file_path = "/Users/privatedeal/"
elif user == 'earth':
    config_file_path = "/Users/naphatsakornkhotsombat/Documents/Databases/"

# Load config file for server connection
yaml_value = yaml.load(open(f"{config_file_path}config.yml", 'r'), Loader=yaml.FullLoader)

_DBNAME = yaml_value['default']['montega_dev']['dbname']
_HOST = yaml_value['default']['montega_dev']['host']
_PORT = yaml_value['default']['montega_dev']['port']
_USER = yaml_value['default']['montega_dev']['user']
_PASSWORD = yaml_value['default']['montega_dev']['pwd']

# print(f"\nDBName: {_DBNAME}"
#       f"\nHost: {_HOST}"
#       f"\nPort: {_PORT}"
#       f"\nUsername: {_USER}"
#       f"\nPassword: {_PASSWORD}")

montega = mysql.connector.connect(
    database=_DBNAME,
    host=_HOST,
    port=_PORT,
    user=_USER,
    passwd=_PASSWORD
)

def main():
    print("Hello World")


if __name__ == '__main__':
    main()
