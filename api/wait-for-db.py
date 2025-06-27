import os
import sys
import time
import MySQLdb

def wait_for_db():
    db_host = os.environ.get('DB_HOST', 'db')
    db_name = os.environ.get('MYSQL_DATABASE', 'teamdb')
    db_user = os.environ.get('MYSQL_USER', 'teamuser')
    db_password = os.environ.get('MYSQL_PASSWORD', 'teampass')
    
    max_retries = 30
    retry_interval = 2
    
    for i in range(max_retries):
        try:
            conn = MySQLdb.connect(
                host=db_host,
                user=db_user,
                passwd=db_password,
                db=db_name
            )
            conn.close()
            print("Database is ready!")
            return True
        except Exception as e:
            print(f"Database not ready yet. Retrying in {retry_interval} seconds... ({i+1}/{max_retries})")
            time.sleep(retry_interval)
    
    print("Failed to connect to database after maximum retries.")
    return False

if __name__ == "__main__":
    if wait_for_db():
        sys.exit(0)
    else:
        sys.exit(1) 