import networkx as nx

# Define the matches
matches = [('A', 'B'), ('A', 'E'), ('B', 'F'), ('C', 'D'), ('C', 'F')]

# Create a graph where each node is a match
G = nx.Graph()

# Add a node for each match
G.add_nodes_from(matches)

# Add edges between matches that share a team
for i in range(len(matches)):
    for j in range(i+1, len(matches)):
        match1 = matches[i]
        match2 = matches[j]
        if set(match1) & set(match2):  # If the two matches share a team
            G.add_edge(match1, match2)

# Use graph coloring algorithm to schedule matches
# nx.coloring.greedy_color returns a dictionary where the key is the match and the value is the color (week)
schedule = nx.coloring.greedy_color(G, strategy="largest_first")

# Organize matches by week
weeks = {}
for match, week in schedule.items():
    if week not in weeks:
        weeks[week] = []
    weeks[week].append(match)

# Display the schedule
for week, matches in weeks.items():
    print(f"Week {week + 1}: {matches}")
