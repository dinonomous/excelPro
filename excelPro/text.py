import pandas as pd

# Input string
input_string = "hi, bro"

# Convert the string into a DataFrame
df = pd.DataFrame([input_string], columns=["Text"])

# Write the DataFrame to a CSV file
df.to_csv("output.csv", index=False)

print("String written to output.csv")
