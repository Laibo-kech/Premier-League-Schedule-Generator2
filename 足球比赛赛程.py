import pandas as pd
from datetime import datetime, timedelta

def generate_schedule(teams, start_date, end_date):
    num_teams = len(teams)
    num_rounds = num_teams - 1
    num_matches_per_round = num_teams // 2

    days_between_matches = (end_date - start_date).days // num_rounds
    schedule = []

    for round in range(num_rounds):
        for match in range(num_matches_per_round):
            home_team = teams[(round + match) % num_teams]
            away_team = teams[(round + num_teams - match) % num_teams]
            match_date = start_date + timedelta(days=round*days_between_matches)
            if match < num_matches_per_round // 2:
                match_date = match_date.strftime('%Y-%m-%d') + " 12:30"
            else:
                match_date = match_date.strftime('%Y-%m-%d') + " 17:30"
            schedule.append((match_date, home_team, away_team))

    return schedule

teams = ["Liverpool", "Manchester City", "Chelsea", "Manchester United", "Leicester City", "Tottenham Hotspur", "Wolverhampton Wanderers", "Arsenal", "Sheffield United", "Burnley", "Southampton", "Everton", "Newcastle United", "Crystal Palace", "Brighton & Hove Albion", "West Ham United", "Aston Villa", "Bournemouth", "Watford", "Norwich City"]
start_date = datetime(2023, 9, 1)
end_date = datetime(2024, 6, 30)

schedule = generate_schedule(teams, start_date, end_date)

# 创建一个 DataFrame 并输出到 Excel
df = pd.DataFrame(schedule, columns=["日期和时间", "主队", "客队"])
df.to_excel("~/Desktop/英超赛程.xlsx", index=False)
