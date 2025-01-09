# https://pypi.org/project/cassandra-driver/
# https://docs.datastax.com/en/developer/python-driver/3.24/getting_started/
from cassandra.cluster import Cluster

cluster = Cluster(['cassandra-manager', 'cassandra-worker1', 'cassandra-worker2'])
session = cluster.connect('urlshortner')

def save(short, long):
    insert_statement = "INSERT INTO bitly (shorturl, longurl) VALUES (%s, %s);"
    session.execute(insert_statement, (short, long))

def load(short):
    query = "SELECT longurl FROM bitly WHERE shorturl = %s"
    row = session.execute(query, (short,)).one()
    if row:
        return row.longurl
    else:
        return None
