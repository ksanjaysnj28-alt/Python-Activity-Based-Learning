# Case Study 47: Sports Tournament Ranking System

## Problem statement
Store match results and team scores, calculate total points and tie-break values, and produce rankings under a specified competition policy.

## Objectives
1. Store match outcomes in tuples.
2. Award 3 points for a win, 1 for a draw, and 0 for a loss.
3. Calculate goals for, goals against, and goal difference.
4. Display a ranking using points and goal difference as tie-break values.

## Assumptions
- Each match tuple stores (team 1, team 2, goals by team 1, goals by team 2).
- Every listed match is valid and each team name exists in the team list.
- Ranking is determined by points first, then goal difference.
- The program prints teams in ranking order using repeated selection; equal values retain the earlier team.

## Algorithm
1. Create the team list and a tuple for each match.
2. Create parallel lists for points, goals for, and goals against.
3. For every match, unpack its tuple.
4. Update goals for and goals against for both teams.
5. Award points based on win, loss, or draw.
6. Repeatedly find the best remaining team using points and goal difference.
7. Display the ranking table.

## Flowchart
See `flowchart.png`.

## Pseudocode
```text
START
SET teams and match tuples
SET points, goals_for, goals_against to zero lists
FOR each match tuple: unpack team names and scores
    FIND positions of both teams
    UPDATE goals_for and goals_against
    IF first score > second score: award 3 points to first
    ELSE IF second score > first score: award 3 points to second
    ELSE: award 1 point to both
REPEAT for every ranking position
    FIND unused team with highest points, then highest goal difference
    DISPLAY team and statistics; mark team as used
STOP
```

## Python source code
See `solution.py`.

## Test cases
| Test case | Input/change | Expected result |
|---|---|
| Normal tournament | Use the six supplied match tuples | All four teams receive a ranking based on points and goal difference. |
| Draw match | Change a match score to an equal score | Both teams receive one point for that match. |
| Tie-break | Give two teams equal points but different goal differences | The team with the higher goal difference is ranked first. |

## Sample output
The screenshot `output_screenshot.png` and text file `sample_output.txt` were generated from an execution of `solution.py` using the sample data in that file.

## Conclusion
The program demonstrates tuples, tuple unpacking, lists, conditional statements, and loops. It ranks teams by points and uses goal difference as the tie-break rule.
