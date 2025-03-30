# IAB Categorization Service 🎥

## Project Details
The IAB Categorization Service is a contextual targeting tool designed to enhance content prediction by leveraging the [V3 IAB taxonomies](https://github.com/InteractiveAdvertisingBureau/Taxonomies/blob/develop/Content%20Taxonomies/Content%20Taxonomy%203.1.tsv). This service predicts and categorizes topics within specific content types, such as video transcripts, enabling businesses to refine their content targeting strategies.

The service is a key component of a broader workflow that ingests video content into AWS S3, transcribes it using the open-source Whisper model from Hugging Face, applies IAB categorization based on the transcripts, and finally exports the results to an external system. This automated pipeline streamlines content classification and enhances contextual understanding for digital advertising.

## Key Features
- **IAB V3 Taxonomy Categorization**: Uses industry-standard classifications to categorize content into hierarchical categories, improving targeting precision.

- **Automated Video Processing Workflow**: Ingests video content, transcribes it, applies categorization, and exports the results seamlessly.

- **Text Segmentation Handling**: Implements a text-splitting mechanism using LangChain to process large transcripts efficiently within GumGum’s 20,000-character API limit.

- **Customizable Business Rules**: Enhances category predictions by applying post-processing rules to align with customer expectations.

- **Performance Evaluation & Experimentation**: Conducts extensive benchmarking of different approaches, including LLM-based categorization (ChatGPT Turbo 3.5), a fine-tuned transformer model (BERT), and an external vendor solution ([GumGum Verity](https://gumgum.jira.com/wiki/spaces/VDC/overview?homepageId=1643348113)), using labeled datasets from ProSiebenSat.1’s video content.

- **Prediction Storage & API Access**: Stores categorized predictions in an AWS RDS database, exposing them via a FastAPI service to enable seamless access for other applications and services.

## My Contribution
I led the end-to-end design, development, and deployment of the IAB Categorization Service and topic detection workflow. I designed the system architecture and implemented the workflow, trained a BERT-based model with 110M parameters on AWS SageMaker using 2 GPUs, and conducted experiments with different categorization approaches, including LLM-based few-shot prompting with ChatGPT Turbo 3.5. Additionally, I evaluated the performance of external categorization providers and led the decision-making process that selected GumGum Verity as the best-performing solution. I presented comparative results to management and customers, influencing the final product direction.

## Challenges and Solutions
- **Enhancing Categorization Accuracy**: Certain categories, especially sensitive topics, were not consistently predicted by GumGum. To improve this, we implemented a flexible set of business rules that can be easily toggled on or off, allowing for refined predictions that better align with customer expectations.

- **Handling Large Transcripts**: Since the GumGum API imposes a 20,000-character limit, we implemented a simple text-splitting mechanism using LangChain. This approach ensured that context was preserved across segmented text, and final predictions were aggregated back to the original content.

## Outcome
- **Operational Impact**: The system processes approximately 30 video contents per day from the ProSiebenSat.1 Mediathek, totaling 900 videos monthly.

- **Revenue Impact**: With third-party cookies being deprecated, contextual targeting is projected to offset approximately $15 million in revenue for static and dynamic ad formats. Our solution contributes directly to $3 million of this revenue by improving contextual targeting capabilities for dynamic formats.



## Technologies
`Python`  `Machine Learning` `NLP`  `Classification`  `FastAPI`  `IAB Taxonomy`  `LLMs`  `LangChain`  `Whisper`  `GumGum Verity`  `ChatGPT`  `BERT`  `AWS Step Functions`  `AWS SageMaker`  `AWS ECS`  `AWS ECR`  `AWS RDS`  `AWS SQS`