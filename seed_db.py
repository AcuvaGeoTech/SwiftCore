import pandas as pd
import geopandas as gpd
import psycopg2

# Read stops data from CSV using pandas
STOPS_DATAFRAME = pd.read_csv('/home/qodestackr/Desktop/data-analysis/gtfs & csv/GTFS_FEED_2019/stops.txt')

# Create a GeoDataFrame with geometry column
STOPS_GEO_DATAFRAME = gpd.GeoDataFrame(STOPS_DATAFRAME, geometry=gpd.points_from_xy(STOPS_DATAFRAME['stop_lon'], STOPS_DATAFRAME['stop_lat']))

# Configure database connection
DATABASE_URL = 'postgresql://postgres:local@localhost:5432/swift_transit'

# Connect to the database
conn = psycopg2.connect(DATABASE_URL)
print(conn)
cur = conn.cursor()

# Define the table schema and create the stops table with PostGIS extension
cur.execute('''
    CREATE EXTENSION IF NOT EXISTS postgis;
    CREATE TABLE IF NOT EXISTS stops (
        stop_id VARCHAR PRIMARY KEY,
        stop_name VARCHAR,
        location GEOMETRY(Point, 4326)
    )
''')
conn.commit()

# Insert data into the stops table
for _, row in STOPS_GEO_DATAFRAME.iterrows():
    values = (row['stop_id'], row['stop_name'], row['geometry'])
    cur.execute('INSERT INTO stops (stop_id, stop_name, location) VALUES (%s, %s, ST_SetSRID(%s::geometry, 4326))', values)

conn.commit()

# Close the database connection
cur.close()
conn.close()
