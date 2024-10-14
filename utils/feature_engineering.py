import numpy as np
import plotly.express as px
import polars as pl


def aggregate_node_features(
    data: pl.DataFrame, node_features: list[str], by: str = "_id"
) -> pl.DataFrame:
    """Utility function to generate basic aggregation statistics features for node level features

    Args:
        data (pl.DataFrame): input dataframe
        node_features (list[str]): list of node features to aggregate
        by (str, optional): the graph ID column. Defaults to "_id".

    Returns:
        pl.DataFrame: dataframe with aggregated features
    """
    aggs = []
    for f in node_features:
        avg = pl.col(f).mean().alias(f"avg_{f}")
        min_val = pl.col(f).min().alias(f"min_{f}")
        max_val = pl.col(f).max().alias(f"max_{f}")
        std = pl.col(f).std().alias(f"std_{f}")
        aggs += [avg, min_val, max_val, std]
    agg_data = data.group_by(by).agg(aggs)

    return agg_data


def get_graph_features(data: pl.DataFrame, node_features: bool = True) -> pl.DataFrame:
    """Pipeline function to generate graph features

    Args:
        data (pl.DataFrame): dataframe with edges 'from' and 'to'
        node_features (bool, optional): Indicator whether you want to create node level features. Defaults to True.

    Returns:
        pl.DataFrame: dataframe with engineered features
    """
    graph_features = (
        data.group_by("_id")
        .agg(pl.len().alias("n_connections"), pl.col("from"), pl.col("to"))
        .with_columns(
            pl.concat_list("from", "to")
            .list.unique()
            .list.len()
            .alias("n_unique_nodes")
        )
        .select(["_id", "n_connections", "n_unique_nodes"])
    )

    if node_features:
        node_features_agg = aggregate_node_features(
            data,
            node_features=[
                "global_source_degrees",
                "global_dest_degrees",
                "local_source_degrees",
                "local_dest_degrees",
            ],
            by="_id",
        )

        graph_features = graph_features.join(node_features_agg, on="_id")

    return graph_features