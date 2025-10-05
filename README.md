Dataset description (What is the dataset about?): This is a dataset of stats from the VNL for mens volleyball in 2023

Input features (What do the features represent?): Positions: OH: Outside Hitter OP: Opposite Hitter MB: Middle Blocker S: Setter L: Libero
Attack : A player's overall average during each game in the offense factor
Block : A player's overall average during each game in the defense factor.
Defense on the net includes direct points, errors and touching the ball without changing points.
Serve : Except for the libero player, the rest of the players serve during each turn to start the game. Each player's service average during the match is listed here.
Set : The setter is responsible for setting the players. But in special cases, the rest of the players cooperate in this matter, and in the data analysis, we will find out which position the players have the most participation in setting after the setter.
Set feature represent the average of successful sets, errors and attempts for each ball during a rally.
Dig : the average of digs, errors and receptions
Receive : Receive feature also represents the average of successful receptions, errors and attempts per mach.

Output labels (What does the dataset predict?): The dataset predicts efficiency and effectiveness in each category

Dataset source (Where did you find it?): This dataset is found on Kaggle and used data from volleyballworld.com

How to run the code?: Git clone repo, cd into lab3 the run this in the terminal: python Lab3.py --file ..\DATA\VNL2023.csv

Group member contributions: Bryant Truong did everything for this lab

Part 6: Added statistical analysis to find mean, max, min, and correlations
some findings were that the oldest player that year was 41. The correlation is if youre older youre less efficent at attacking and if you set it tends to correlate into being bad at attacking
