import threading
import time

import pymssql


def connect_to_database(thread_id):
    conn = pymssql.connect(server="192.168.35.89", user="sa", password="Gmerit@123", database="UAT", port="1433")
    conn.autocommit(False)
    try:
        with conn.cursor() as cursor:
            cursor.execute("BEGIN TRANSACTION")
            cursor.execute("SELECT @@VERSION;")
            row = cursor.fetchone()
            print(f"Thread {thread_id}: {row[0]}")
            time.sleep(3)
            cursor.execute("COMMIT TRANSACTION")
            # cursor.close()
    except Exception as e:
        print(f"Thread {thread_id} error: {e}")
    finally:
        conn.commit()
        conn.close()


def test_connections(num_thread):
    threads = []
    for i in range(num_thread):
        t = threading.Thread(target=connect_to_database, args=(i,))
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()


# 设置并发线程数
num_threads = 1000
test_connections(num_threads)
