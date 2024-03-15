import psycopg2 as psy
import pandas as pd

def parseURL(url):
    # Split the URL into parts
    parts = url.split("://")[1].split("/")

    # Extract username, password, host, and port
    userinfo, host_port = parts[0].split("@")
    username, password = userinfo.split(":")
    host, port = host_port.split(":")

    # Extract database
    database = parts[1]

    # Create a dictionary to store the extracted values
    parsed_data = {
        "db": database,
        "host": host,
        "user": username,
        "pw": password,
        "port": port
    }

    return parsed_data

def createConnection(parsed_url):
    conn = psy.connect(
        database=parsed_url["db"],
        host=parsed_url["host"],
        user=parsed_url["user"],
        password=parsed_url["pw"],
        port=parsed_url["port"]
    )
    
    return conn

def sqlSearch(conn, query):

    cur = conn.cursor()

    cur.execute(query)

    cur.execute(query)

    rows = cur.fetchall()
    colnames = [desc[0] for desc in cur.description]
    df = pd.DataFrame(rows, columns = colnames)

    return(df)