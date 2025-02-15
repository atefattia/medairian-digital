# TV Ads Attribution 📺

## Project Details
This tool measures the short-term online impact of TV advertisements by analyzing post-spot visit spikes and calculating website traffic attribution. This system helps businesses evaluate the effectiveness of their TV campaigns by tracking key performance indicators (KPIs) such as website visits and conversions. It supports both internal and external TV spots and integrates seamlessly with multiple user tracking platforms, including [Google Analytics](https://marketingplatform.google.com/about/analytics/), [Mapp](https://mapp.com/), and [Adjust](https://www.adjust.com/), enabling a comprehensive evaluation of TV campaign performance across a wider spectrum.

![TV Ads Attribution Visualization](/static/images/projects/tv_ads_attribution.svg)

## Key Features
- **Comprehensive TV Spot Analysis**: Processes both internal and external TV spots to provide a holistic view of campaign performance.
- **Multi-Platform Integration**: Connects with various analytics tools, including Google Analytics and other third-party tracking platforms.
- **Advanced Attribution Algorithms**: Implements multiple levels of attribution models, including statistical and AI-driven methods, for accurate traffic measurement.

## My Contribution
I started as an Associate, initially assisting with the refactoring and migration of an existing on-premises solution to the Cloud. However, I quickly took ownership of the product, leading the development of new features and enhancements. Notably, I spearheaded the creation of an AI-driven attribution algorithm that significantly improved accuracy. Additionally, I enhanced the codebase by introducing comprehensive test coverage, designed an automated reprocessing mechanism to minimize maintenance efforts, and implemented other optimizations to boost performance, scalability, and reliability.

## Challenges and Solutions
[Discuss any interesting challenges and how they were overcome]

- Multiple data sources (harmonizing them to a common format)
- Handling High-Volume Data Processing: Optimized data pipelines using distributed computing frameworks to ensure efficient processing of large datasets. (around 150GB processed in a daily basis)
- Orchestration and Monitoring (asset arriving at different times)
- Spot chains (visits attribution gets complicated when a visits can be influenced by multiple spots)

## Outcome
T.B.D 🚥
- Enabled more accurate measurement of TV ad impact, leading to better budget allocation and campaign optimization.
- Improved the ability to attribute website traffic spikes to specific TV spots, increasing transparency and effectiveness in media planning.
- Delivered a scalable, high-performance solution that provided real-time insights for marketing teams.

## Technologies
- Python, 
- ETL
- Data Engineering
- PySpark
- AWS