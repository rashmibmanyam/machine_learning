# Dataset Notes

## Criteo Click Logs

- Download source: https://huggingface.co/datasets/criteo/CriteoClickLogs/tree/main/data/day%3D2015-03-10
- Downloaded date: 2015-03-10
- Scope included: the first 15 parquet files from the 2015-03-10 folder.

### Dataset overview
Criteo Click Logs is a large-scale advertising-click dataset released by Criteo for click-through-rate (CTR) modeling and online advertising research. The Hugging Face repository presents it as a click-log dataset for advertising and commerce-related machine learning tasks.

### Feature details
The dataset is designed for CTR prediction and contains a mix of:
- anonymized categorical features,
- continuous / numerical features,
- and a binary click label indicating whether an ad impression resulted in a click.

In the standard Criteo benchmark formulation, the data typically includes:
- a set of dense numerical features,
- a set of sparse categorical features represented by anonymized identifiers,
- and a target variable for click/no-click behavior.

These features are intentionally anonymized so that the data can be used for research while preserving user and advertiser privacy.

### Where it is commonly used
This dataset is widely used for:
- CTR prediction,
- click-through-rate estimation in advertising systems,
- feature engineering experiments,
- and benchmarking recommender / ad-ranking models such as factorization machines and deep CTR architectures.

It is one of the most common public benchmarks for evaluating models that learn from sparse high-dimensional features in online advertising.

---

## Tenrec Dataset

- Download source: https://static.qblv.qq.com/qblv/h5/algo-frontend/tenrec_dataset.html
- Dataset type: large-scale multi-scenario recommender-system benchmark dataset.

### Dataset overview
Tenrec is a large-scale, multi-purpose benchmark dataset for recommender systems released by Tencent. The dataset page describes it as a large-scale multi-scenario real-world dataset collected from Tencent’s content recommendation platforms, with the goal of supporting more realistic and comprehensive evaluation of recommender system models.

### Feature details
The dataset is built from multiple recommendation scenarios and contains rich interaction signals. According to the dataset page, it includes:
- four recommendation scenarios: QK-video, QK-article, QB-video, and QB-article,
- user feedback signals such as clicks, likes, shares, and follows,
- real negative samples (items that were exposed but received no user action),
- anonymized user-side demographic features such as gender and age,
- and item-side features such as video type information.

The page also highlights several important characteristics:
- very large scale,
- multi-scenario coverage,
- multiple types of user feedback,
- and some overlap of users and items across scenarios.

### Where it is commonly used
The dataset is intended for research on:
- CTR prediction,
- sequential recommendation,
- transfer learning,
- cold-start recommendation,
- lifelong learning,
- and model acceleration for recommender systems.

The accompanying paper is referenced as:
- Tenrec: A Large-scale Multipurpose Benchmark Dataset for Recommender Systems.

---

## Summary
These two datasets complement each other well for recommender and advertising research:
- Criteo is a classic benchmark for sparse-feature CTR modeling in advertising.
- Tenrec is a newer, large-scale multi-scenario benchmark for broader recommender-system studies, including richer feedback and multiple task settings.
