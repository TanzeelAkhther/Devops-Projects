import redis
import psycopg2
import os
import time

redis_host = os.getenv("REDIS_HOST", "localhost")
postgres_host = os.getenv("POSTGRES_HOST", "localhost")

r = redis.Redis(host=redis_host, port=6379, db=0)

while True:
    try:
        vote = r.blpop("votes", timeout=5)
        if vote:
            vote_value = vote[1].decode("utf-8")

            conn = psycopg2.connect(
                host=postgres_host,
                user="postgres",
                password="postgres",
                dbname="votes"
            )
            cur = conn.cursor()

            cur.execute("""
                CREATE TABLE IF NOT EXISTS votes (
                    id SERIAL PRIMARY KEY,
                    vote TEXT
                )
            """)

            cur.execute("INSERT INTO votes (vote) VALUES (%s)", (vote_value,))
            conn.commit()

            cur.close()
            conn.close()

            print(f"Processed vote: {vote_value}")

    except Exception as e:
        print("Error:", e)
        time.sleep(5)