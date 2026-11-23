# Case Study 47: Sports Tournament Ranking System
# Each match is a tuple: (team1, team2, score1, score2).

teams = ["Tigers", "Eagles", "Sharks", "Falcons"]
matches = [
    ("Tigers", "Eagles", 2, 1),
    ("Sharks", "Falcons", 1, 1),
    ("Tigers", "Sharks", 0, 2),
    ("Eagles", "Falcons", 3, 1),
    ("Tigers", "Falcons", 2, 2),
    ("Eagles", "Sharks", 1, 0)
]

points = [0, 0, 0, 0]
goals_for = [0, 0, 0, 0]
goals_against = [0, 0, 0, 0]

for match in matches:
    team1, team2, score1, score2 = match
    index1 = teams.index(team1)
    index2 = teams.index(team2)
    goals_for[index1] = goals_for[index1] + score1
    goals_against[index1] = goals_against[index1] + score2
    goals_for[index2] = goals_for[index2] + score2
    goals_against[index2] = goals_against[index2] + score1

    if score1 > score2:
        points[index1] = points[index1] + 3
    elif score2 > score1:
        points[index2] = points[index2] + 3
    else:
        points[index1] = points[index1] + 1
        points[index2] = points[index2] + 1

# Select the highest-ranked team one position at a time.
used = [False, False, False, False]
print("FINAL TOURNAMENT TABLE")
for place in range(len(teams)):
    best_index = -1
    best_difference = -999
    for i in range(len(teams)):
        difference = goals_for[i] - goals_against[i]
        if used[i] == False:
            if best_index == -1 or points[i] > points[best_index] or (points[i] == points[best_index] and difference > best_difference):
                best_index = i
                best_difference = difference
    used[best_index] = True
    print(place + 1, teams[best_index], "Points:", points[best_index], "Goal difference:", best_difference)
