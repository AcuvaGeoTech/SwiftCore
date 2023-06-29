# CURRENT SPRINT AND TODOS:

END GOAL: PARSE GTFS DATA WITH CAPABILITIES WE NEED TO EXTRACT:

SMALL GOALS: FILTER DATA BASED ON CONDITIONS E.G ROUTE

```python
# Filter routes with a certain route_type
filtered_routes = df[df['route_type'] == 3]
```

SORT, AGG, ADD/MODIFY COLS

```python
# Sort routes by route_short_name in ascending order
sorted_routes = df.sort_values('route_short_name')


# Calculate the number of routes for each agency_id
route_counts = df['agency_id'].value_counts()


# Add a new column that combines route_short_name and route_long_name
df['route_name'] = df['route_short_name'] + ' - ' + df['route_long_name']


```

<!-- Analyze the data: Perform any analysis or computations required for your project using pandas functions and methods. You can generate insights, visualize the data, or derive meaningful information.


# Calculate the average route_type
average_route_type = df['route_type'].mean()

# Plot a bar chart of route counts by agency_id
df['agency_id'].value_counts().plot(kind='bar')


Save or export the data: If you need to save the modified DataFrame or export it to a different format, you can use pandas' built-in functions.


# Save the DataFrame to a new CSV file
df.to_csv('/path/to/save/file.csv', index=False)

 -->

## Common tasks you can perform on a DataFrame include:

- Accessing and retrieving data from specific rows and columns
- Filtering and subsetting data based on specific conditions
- Aggregating and summarizing data
- Applying mathematical and statistical operations to columns
- Merging, joining, and reshaping data from multiple DataFrames
- Handling missing data and data cleaning
- Visualizing data through various plotting functions
