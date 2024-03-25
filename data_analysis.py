"""
Python exercise from "Python Journey" Python training by Hashtag.

Challenge: given a CSV file ("cancelamentos_sample.csv") containing various information about customers and
subscription cancellation of a hypothetical service provided by a hypothetical company, analyse the data contained
in the file and find out what are the main reasons for subscription cancellation. Plot graphs in order to make the
problems easy to visualize.

Important: the program must use the following libraries - pandas; Plotly.
"""

import pandas as pd
import plotly.express as px

# reading the file and creating a table with pandas
table = pd.read_csv("cancelamentos_sample.csv")

# excluding "customerID" from the table as it will not help our analysis
table = table.drop(columns="CustomerID")

# printing info to check if the database has problems
print(table.info())
# some lines have NaN values. Excluding them from the table to avoid problems with our analysis
table = table.dropna()

# printing "cancelou" column in order to know how many clients cancelled the subscription
print(table["cancelou"].value_counts())

# in percentages
print(table["cancelou"].value_counts(normalize=True))

# generating graphs with plotly
for column in table.columns:
    graph = px.histogram(table, x=column, color="cancelou")

    # display the o graphs
    graph.show()

# RESULTS OF THE ANALYSIS
    # Every single customer over 50 years old cancelled the subscription.
    # Women tend to cancel the subscription more than men.
    # After the fourth call-center call customers always cancel the subscription.
    # Customers cancel the subscription after 20 days of payment delay.
    # Every customer who had a montlhy subscription plan cancelled.
    # Every customer who spent less than $500 cancelled the subscription.
