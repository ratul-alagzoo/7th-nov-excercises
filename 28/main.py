import json
import polars as pl

data = json.load(open('static/data.json'))
nodes_dict = data['nodes']
nodes_list = list(nodes_dict.values())
pl_df =  pl.DataFrame(nodes_list)
print("Total # of nodes: ", pl_df.height)

# add a column for name length
pl_df = pl_df.with_columns([
    pl.col("name").str.len_chars().alias("name_length")
])

# longest name
max_len = pl_df.select(pl.col("name_length").max()).item()
longest_names = pl_df.filter(pl.col("name_length") == max_len)
print("Longest names: ", longest_names)

# shortest name
min_len = pl_df.select(pl.col("name_length").min()).item()
shortest_names = pl_df.filter(pl.col("name_length") == min_len)
print("Shortest names: ", shortest_names)

# add a column for stats list length
df = pl_df.with_columns([
    pl.col("stats").list.len().alias("stats_count")
])

# max stats count
max_stats = df.select(pl.col("stats_count").max()).item()
most_stats_nodes = df.filter(pl.col("stats_count") == max_stats)
print("Most statistics nodes: ", most_stats_nodes)
