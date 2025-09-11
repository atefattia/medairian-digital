# Time Series Forecasting 📈

## Project Details

This project enhances TV ad attribution by introducing a forecasting-based baseline model for website traffic. The system trains a model to predict the expected website traffic without TV effects, capturing normal user behavior influenced only by seasonality and trends. This predicted traffic — the baseline — is then compared against actual website visits. Any significant uplift beyond the baseline is attributed to TV campaigns, enabling a more accurate measurement of spot performance.

We used [Prophet](https://facebook.github.io/prophet/docs/quick_start.html), an open-source forecasting model, to capture complex seasonality and trend patterns while supporting additional features. The end-to-end pipeline was developed and deployed using [Metaflow](https://metaflow.org/), Netflix’s open-source framework for orchestrating machine learning workflows.

![Time Series Forecasting - MLOps](/static/images/projects/sailly.svg)

The system retrains models daily with the last 6 weeks of traffic data, ensuring forecasts incorporate the latest behavioral trends.

## Key Features

- **Scalable ML Pipelines**: Thanks to Metaflow, the system can scale vertically (handling high-volume customers by using larger instances) and horizontally (training and predicting for many customers simultaneously).
- **Dynamic Pipeline Configuration**: Supports config-driven pipeline construction similar to scikit-learn Pipelines. This allows easy experimentation with different models, features, and hyperparameters by simply editing a YAML config file.
- **Automated Retraining**: A daily retraining mechanism ensures models adapt to the most recent traffic data. Orchestrated with _AWS EventBridge_ and _AWS Step Functions_, each pipeline uses the last 6 weeks of data to stay current.

## My Contribution

I contributed to the design and development of the abstraction layer that dynamically builds machine learning pipelines from configuration files, enabling flexible experimentation and deployment. As part of this, I developed three core pipelines: a training pipeline to train new models and register them in MLflow, an inference pipeline to load trained models from MLflow and generate website traffic predictions, and an evaluation pipeline to run multiple experiments in parallel with different configurations while tracking results in MLflow. I also played a key role in selecting the best-performing model, tuning its hyperparameters, and engineering features to improve its performance. Finally, I productionalized the training and inference pipelines in AWS, ensuring the system could run automatically and scale to meet the demands of daily operations.

## Challenges and Solutions

- **Scalability**: Needed to retrain models daily for ~50 customers with very different traffic volumes, ranging from a few hundred to several million visits per day. Solved by leveraging Metaflow’s ability to scale both vertically (larger instances) and horizontally (parallel training and inference across many customers).

- **Local Development vs. Cloud Deployment**: Required fast experimentation on small datasets locally while seamlessly transitioning to large-scale cloud execution for production. Addressed by Metaflow’s flexibility to run the same code in both environments with minimal changes via its CLI.

- **Experimentation Speed**: Developers needed to test different models, features, and hyperparameters quickly. Solved by building a config-driven pipeline generator, enabling easy modification of YAML files to create new experiments and compare performance results efficiently.

## Outcome

- Produced a **more accurate** baseline by incorporating seasonality and long-term trends.
- Improved attribution of TV spot impact by considering a **longer context window** (6 weeks) instead of just a few minutes.
- Increased **transparency and robustness** in measuring TV ad performance.
- Trade-off: The new solution introduced additional **maintenance overhead**, as separate training and inference pipelines need to be operated and monitored.

## Technologies

`Python`  `Time Series`  `Forecasting`  `Website Traffic`  `Prophet` `Metaflow`  `Pandas`  `Scikit-Learn`  `Evaluation`  `MLflow`  `Preprocessing` `AWS EventBridge` `AWS Step Functions`
