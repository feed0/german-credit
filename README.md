# Credit Score Analysis

[Anton Markov et al (Credit scoring methods: Latest trends and points to consider, 2022)](https://www.sciencedirect.com/science/article/pii/S2405918822000095) suggest that University of California Irvine's datasets are among the most popular public sources for credit score modeling. I have chosen the [UCI (Statlog) German Credit Data](https://archive.ics.uci.edu/dataset/144/statlog+german+credit+data) to begin with.

# German Credit Data 

This dataset contains information about 1000 loan applications, including personal and financial data, credit history, and loan characteristics.

# Objective

Train models in order to predict weather a loan is benefitial or not, in other words predict its creditability for the finantial institution.

# Models

## 1. Logistic Regression

![image](https://github.com/user-attachments/assets/2ac102ca-7439-4da3-b8bc-c917d7939e28)

Due to some imbalanced columns, the logreg model presents difficulty in predicting "Bad" loans. To overcome this limitation we might consider oversampling the misrepresented categories in these columns.
