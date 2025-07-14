# 📊 Customer Cancellation Analysis

This project is part of the **"Python Journey"** training by Hashtag Treinamentos. It analyzes customer cancellation behavior in a subscription-based service using real-world-style data, and presents the insights visually using interactive charts.

## 🧠 Project Overview

The script reads data from a CSV file named `cancelamentos_sample.csv`, which contains information about customer behavior and cancellations. The objective is to:

- Identify the main reasons for subscription cancellations
- Generate insightful visualizations to support business decisions

## 📄 Dataset Structure

The dataset includes columns such as:

- `CustomerID` (dropped from the analysis)
- `Age`
- `Gender`
- `Number of Support Calls`
- `Days in Arrears`
- `Subscription Type`
- `Monthly Spending`
- `Cancelled` (`cancelou`) – Indicates whether the customer canceled the subscription

## 📊 Key Findings

- All customers **over 50 years old** canceled their subscriptions.
- **Women** canceled more than men.
- **Every customer** who received more than **4 support calls** canceled.
- **20+ days in arrears** led to cancellations.
- **100%** of customers with **monthly plans** canceled.
- Customers spending **less than $500** all canceled their subscriptions.

## 🛠️ Technologies Used

- [Python 3.x](https://www.python.org/)
- [`pandas`](https://pandas.pydata.org/) – Data analysis and cleaning
- [`plotly`](https://plotly.com/python/) – Interactive data visualization

📈 Visual Output
The program uses plotly.express to generate histograms for each feature in the dataset, comparing customers who canceled vs. those who didn’t. These interactive graphs help uncover patterns and actionable insights.

✅ Highlights
Real-world-style dataset
Interactive data visualization
Detects patterns that lead to customer churn
Excellent use case for data-driven decision-making
