import pandas as pd

def assign_scores(df, column_name, intervals, scores, new_column_name):
    """
    Assign scores based on specified intervals and store them in a new column.

    Parameters:
    - df: DataFrame
        The DataFrame containing the data.
    - column_name: str
        The name of the column to evaluate.
    - intervals: list of tuples
        List of intervals. Each tuple represents a closed interval (start, end).
    - scores: list
        List of scores corresponding to each interval.
    - new_column_name: str
        The name of the new column to store the assigned scores.

    Returns:
    - DataFrame
        The original DataFrame with the new column added.
    """
    # Validate input lengths
    if len(intervals) != len(scores):
        raise ValueError("Number of intervals must match the number of scores.")

    # Initialize an empty list to store the scores
    assigned_scores = []

    # Iterate through rows in the specified column
    for value in df[column_name]:
        # Check which interval the value falls into and assign the corresponding score
        score = None
        for i, interval in enumerate(intervals):
            if interval[0] <= value <= interval[1]:
                score = scores[i]
                break

        # If no interval is matched, you can set a default score or handle it as needed
        if score is None:
            score = "Not in any interval"

        # Append the assigned score to the list
        assigned_scores.append(score)

    # Add the new column to the DataFrame
    df[new_column_name] = assigned_scores

    return df

# Example usage:
# Create a sample DataFrame
data = {'Value': [5, 15, 25, 35, 45]}
df = pd.DataFrame(data)

# Define intervals and scores
intervals = [(0, 10), (11, 20), (21, 30), (31, 40), (41, 50)]
scores = ['Low', 'Medium', 'High', 'Very High', 'Maximum']

# Call the function to assign scores and store them in a new column
df = assign_scores(df, 'Value', intervals, scores, 'Score')

# Display the updated DataFrame
print(df)