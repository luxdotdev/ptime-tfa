import pandas as pd
import hero_mappings as hm

def cleanMap(df):
    staggers = findStaggers(df)
    firstKills = findFirstKills(staggers)

    # Add hero-role mappings
    final = firstKills.merge(hm.heroes, left_on='victim_hero', right_on='Hero', how='inner')

    # Make it pretty
    final.drop(columns=['Hero'], axis=1, inplace=True)
    final.rename(columns={'Role':'victim_role'}, inplace=True)
    return(final)

def findStaggers(df):

    # Get time since previous kill
    df['time_prev'] = df['match_time'].diff()

    # Get time until next kill
    df['time_next'] = df['time_prev'].shift(-1)

    # Kill is considered a stagger if isolated by 15s both before and after
    df['is_stagger'] = (df['time_prev'] > 15) & (df['time_next'] > 15)

    df['fight_id'] = df.loc[~df['is_stagger'], 'time_prev'].gt(15).cumsum() + 1
    df['fight_id'] = df['fight_id'].fillna(-1).astype(int)
    return(df)

def findFirstKills(df):
    first_deaths = df.groupby('fight_id').first()
    first_deaths = first_deaths[['attacker_team', 'attacker_hero','victim_team', 'victim_hero']]

    # Count kills by each team in each fight
    kills_by_team = df.groupby(['fight_id', 'attacker_team']).size().unstack(fill_value=0)

    # Determine which team had more kills in each fight
    more_kills_team = kills_by_team.idxmax(axis=1)

    # Add a new column 'attacker_team_won' to indicate whether the attacker team won the fight
    first_deaths['attacker_team_won'] = first_deaths['attacker_team'] == more_kills_team
    return(first_deaths)
