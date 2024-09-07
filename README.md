# Credit Score Analysis

[Anton Markov et al (Credit scoring methods: Latest trends and points to consider, 2022)](https://www.sciencedirect.com/science/article/pii/S2405918822000095) suggest that University of California Irvine's datasets are among the most popular public sources for credit score modeling. I have chosen the [UCI (Statlog) German Credit Data](https://archive.ics.uci.edu/dataset/144/statlog+german+credit+data) to begin with.

# German Credit Data 

This dataset contains information about 1000 loan applications, including personal and financial data, credit history, and loan characteristics.

# Objective

Train models in order to predict weather a loan is benefitial or not, in other words predict its creditability for the finantial institution.

# Models

## 1. Logistic Regression

![LogRegConfusionMatrix](https://github.com/user-attachments/assets/f7db9635-87d2-498a-9683-e128d0198dc9)
![LogRegClassificationReport](https://github.com/user-attachments/assets/13f612e6-324c-4d53-964d-e466e2e60f12)


Due to some imbalanced columns, the logreg model presents difficulty in predicting "Bad" loans. To overcome this limitation we might consider oversampling the misrepresented categories in these columns.
