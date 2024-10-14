API Security: Anomaly Detection App

> [!WARNING]
> All the metrics, plots, and insights are made up and taken from the internet

![network header](assets/header.png)

## Dataset

[Kaggle](https://www.kaggle.com/datasets/tangodelta/api-access-behaviour-anomaly-dataset/data) (licensed under GPL-2).

Distributed micro-services based applications are typically accessed via APIs. The authors of this dataset have collected sequences of API calls from an application and put them into a graph format. For this graph, they've generated common API access patterns (i.e. sequences of API calls) and have calculated user access metrics that can be used to classify these behaviours. Also, they've manually labelled a set of these behaviour patters (our training set) and have provided the remaining sequences for us to classify.

## Objectives

The main objective of this project is:

> **To develop a system that will be able to detect anomalous behaviour from the API calls for the remaining sequences**

To achieve this objective, it was further broken down into the following 5 technical sub-objectives:

1. To perform in-depth exploratory data analysis of the both datasets (tabular and graph)
2. To engineer new predictive features from the available graphs
3. To develop a supervised model to classify behaviour into normal and anomalous
4. To recommend a threshold that will perform better than the present baseline (ALGO-X) in terms of F1 score
5. To create an API endpoint for the trained model and deploy it

## Main Insights

From the exploratory data analysis, we found out that anomalous behavviour patterns are cahracterised by:

* Insight about anomaly vs normal #1
* Insight about anomaly vs normal #2
* Insight about anomaly vs normal #3

## Engineered Features

From the provided networks, the following features were extracted:

## Model Selection


### Model Explainability


## Business Metrics



