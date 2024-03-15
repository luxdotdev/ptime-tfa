import collect_data as dat

grouped = dat.df.groupby(['attacker_team', 'attacker_team_won'])
print(grouped.size())