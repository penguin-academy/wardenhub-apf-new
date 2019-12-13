import mysql.connector
from mysql.connector import Error
import configparser

#Load the configuration file
config = configparser.ConfigParser()
config.read('config.ini')

db_config = {
  'user': config.get('db','MYSQL_USER'),
  'password': config.get('db','MYSQL_PASSWORD'),
  'host': config.get('db','MYSQL_HOST'),
  'database': config.get('db','MYSQL_DB'),
  'raise_on_warnings': True
}


def connect():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(**db_config)
        if conn.is_connected():
            return conn
 
    except Error as e:
        print(e)
 
 
if __name__ == '__main__':
    connect()