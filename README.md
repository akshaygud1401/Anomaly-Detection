API Security: Anomaly Detection App

> [!WARNING]
> All the metrics, plots, and insights are made up and taken from the internet

![network header](assets/header.png)

## Dataset

This dataset was found on [Kaggle](https://www.kaggle.com/datasets/tangodelta/api-access-behaviour-anomaly-dataset/data) (licensed under GPL-2).

Distributed micro-services based applications are typically accessed via APIs. The authors of this dataset have collected sequences of API calls from an application or accessed programmatic means and put them into a graph format. For this graph, they've generated common API access patterns (i.e. sequences of API calls) and have calculated user access metrics that can be used to classify these behaviors. They have also manually labelled a set of these behavior patters (our training set) and have provided the remaining sequences for us to classify.

## Objectives

The main objective of this project is:

> **To develop a system that will be able to detect anomalous behaviour from the API calls**

To achieve this objective, it was further broken down into the following 5 technical sub-objectives:

1. To perform in-depth exploratory data analysis of the both datasets (tabular and graph)
2. To engineer new predictive features from the available graphs
3. To develop a supervised model solely from the engineered features to classify behaviour into normal and anomalous
4. To recommend a threshold that will maximize model performance in terms of F1 score
5. To create an API endpoint for the trained model and deploy it

## Main Insights

From the exploratory data analysis, we found out that anomalous behavior patterns are characterized by:

* IP's that are of *datacenter* type are anomalous
* Longer sequences with faster inter API access ruations are not more likely to be anomalous
* Longer sequences with more distinct APIs in the behavior group are more likely to be anomalous

## Engineered Features

From the provided networks, the following 9 features were extracted:
 * Graph level features
   * *n_connection*s: measures number of edges for a behavior and can indicate anomalous behavior if too large/small
 * Node level features
   * Global: measures node attributes across all the graphs in the data, and can indicate anomalous behavior if very high
     * *avg_global_source_degrees*
     * *std_global_source_degrees*
     * *min_global_source_degrees*
     * *max_global_source_degrees*
     * *avg_global_dest_degrees*
     * *min_global_dest_degrees*
     * *max_global_dest_degrees*
   * Local: measures node attributes across a specific graph, and can indicate anomalous behavior if very high
     * *std_local_source_degrees*

The engineered features were able to produce a ROC-AUC of nearly 0.99, and hasa improved F1 score from the baseline statistical model by 0.15


## Model Selection
Models performance was measured using ROC AUC because we are doing a binary classification task. I used a Histogram Gradient Boosting Model because of its tree-based struture (accounting for label imbalance). The HGBT was tuned for 20 iterations. The best performing model contained the following parameters:

```json
{
    learning_rate: 0.1,
    max_iter: 99, 
    max_leaf_nodes: 14, 
    max_depth: 9, 
    l2_regularization: 8.14695639097796,
    class_weight: 'balanced'
}
```

![ROC curve](assets/roc_auc.png)

![PR curve](assets/pr_curve.png)

The HGBT model performs well, achieving ROC AUC and PR scores >0.97

### Model Explainability

![Shap](assets/shap.png)

The final model has a well balaned feature importance distribution, with 2 notable features being *n_connections* and *std_local_source_degrees*. The SHAP distributions are intuitive, as having a low number of connections and having low variation in the number of edges that come from a node could indicate that the behavior is a bot behavior to try to expose business logic, or could be part of a continuous attack of small behaviors to expose the API.

## Business Metrics

Determining the achieved business metrics can be done by first setting the model's threshold.

![Threshold](assets/thresholds.png)

From the threshold analysis, we can see that F1 is the highest at the threshold of 0.33, and the maximum F1 score is 0.927

| Threshold  | 0.33 |
|------------|------|
| Precision  | 0.927|
| Recall     | 0.927|
| F1 Score   | 0.927|





