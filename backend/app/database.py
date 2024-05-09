import mysql.connector

DB_CONFIG = {
  'user': 'root',
  'password': 'root',
  'host': '127.0.0.1',
  'database': 'Groupbuy',
}

def get_database_connection():
    return mysql.connector.connect(**DB_CONFIG)

def execute_query(query, params=None, fetchall=False):
    try:
        conn = get_database_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)

        if query.strip().upper().startswith('SELECT'):
            if fetchall:
                return cursor.fetchall()
            else:
                return cursor.fetchone()
            
        else:
            conn.commit()
            return True

    except Exception as e:
        print(str(e))
        conn.rollback()
        return None
    
    finally:
        cursor.close()
        conn.close()