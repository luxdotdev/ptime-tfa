import db_connection as db
from cleaning import *
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv(".env")
url = os.getenv("prod_url")

conn = db.createConnection(db.parseURL(url))

# Find all scrim IDs by teamId
teamId = 1

mapIdsByTeam = f"""
SELECT m."mapId"
FROM "MapData" m
INNER JOIN 
"Scrim" s
ON s."teamId" = {teamId}
AND m."mapId" IS NOT NULL
AND m."scrimId" = s."id"
"""

mapsDf = db.sqlSearch(conn, mapIdsByTeam)

maps = [mapid for mapid in mapsDf['mapId']]

for id in range(len(maps)):
    currId = maps[id]
    query = f"""
    SELECT "match_time",
        "attacker_team",
        "attacker_hero",
        "attacker_name",
        "victim_team",
        "victim_hero",
        "victim_name"
    FROM "Kill"
    WHERE "MapDataId" = {currId}
    """
    if id == 0:
        df = db.sqlSearch(conn, query)
        df = cleanMap(df)
    else:
        new = cleanMap(db.sqlSearch(conn,query))
        df = pd.concat([df, new])

print(df)