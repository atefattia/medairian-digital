# TV Ads Attribution 📺
<a href="/projects" class="inline-flex items-center px-4 py-2 bg-sky-50 text-sky-700 hover:bg-sky-100 rounded-full text-sm font-medium transition-colors duration-300 ease-in-out shadow-sm hover:shadow-md border border-sky-100">← Back to Projects</a>

## Project Details
This tool measures the short-term online impact of TV advertisements by analyzing post-spot visit spikes and calculating website traffic attribution. This system helps businesses evaluate the effectiveness of their TV campaigns by tracking key performance indicators (KPIs) such as website visits and conversions. It supports TV spots from various sources and integrates seamlessly with user tracking platforms like [Google Analytics](https://marketingplatform.google.com/about/analytics/), [Mapp](https://mapp.com/), and [Adjust](https://www.adjust.com/), enabling a comprehensive evaluation of TV campaign performance across multiple channels.

![TV Ads Attribution Visualization](/static/images/projects/tv_ads_attribution.svg)

The system hypothesizes that within 8 minutes of a TV spot airing, the business partner’s webpage will see a surge in visits. Ideally, traffic spikes immediately after the ad, then gradually declines, returning to pre-ad levels by the 8-minute mark. All visits exceeding the baseline during this window are attributed to the TV spot, assuming they were influenced by it.

## Key Features
- **Comprehensive TV Spot Analysis**: Processes both internal and external TV spots to provide a holistic view of campaign performance.
- **Multi-Platform Integration**: Connects with various analytics tools, including Google Analytics and other third-party tracking platforms.
- **Advanced Attribution Algorithms**: Implements multiple levels of attribution models, including statistical and AI-driven methods, for accurate traffic measurement.

## My Contribution
I began as an Associate, assisting with the refactoring and cloud migration of an on-premises solution. I quickly took ownership of the product, leading feature development and enhancements. Notably, I designed an AI-driven attribution algorithm that significantly improved accuracy. I also strengthened the codebase by implementing comprehensive test coverage, a command-line interface for streamlined reprocessing, and various optimizations to enhance performance, scalability, and reliability. After four years leading the project, I am recognized as the company's expert in this field.

## Challenges and Solutions

- **Multiple Data Sources**: Standardized and harmonized diverse data formats into a common schema for seamless integration.
- **High-Volume Data Processing**: Optimized data pipelines using distributed computing frameworks, enabling efficient daily processing of ~150GB.
- **Orchestration and Monitoring**: Implemented event-based processing to handle asynchronous data arrivals, and used a real-time reporting dashboard for monitoring.
- **Spot Chains**: Developed a weighted attribution model using channel shares to account for visits influenced by multiple TV spots.

## Outcome
- Enabled more accurate measurement of TV ad impact, leading to better **budget allocation** and **campaign optimization**.
- Improved the ability to attribute website traffic spikes to specific TV spots, increasing **transparency** and **effectiveness** in media planning.
- Adopted by over **500 customers** for TV ad analysis.
- Reduced infrastructure costs by approximately **60%** following cloud migration.
- Integrated into partner TV campaign packages, with budgets ranging from **€100K to several million**.

## Technologies
`Python`  `ETL`  `Data Engineering`  `PySpark`  `AWS Glue`  `AWS DynamoDB`  `AWS Athena`  `AWS Lambda`  `AWS EC2`  `AWS S3`  `AWS Kinesis`  `AWS Step Functions`  `AWS CloudWatch`  `AWS SNS`  `Google BigQuery`  `Google Analytics`  `Mapp`  `Adjust`  `Nielsen`