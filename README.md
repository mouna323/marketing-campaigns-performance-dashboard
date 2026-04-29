# Marketing Campaign Performance Analysis
##  Project Overview
This project analyzes marketing campaign performance across different channels and customer segments to identify opportunities for improving return on investment (ROI) and cost efficiency.
The analysis follows an end-to-end workflow, including data ingestion, transformation, and visualization.

##  Objectives
-  Evaluate campaign performance using ROI and conversion rate
-  Compare effectiveness across campaign types and channels
-  Identify cost-efficiency opportunities
-  Support data-driven marketing decisions

## Tools & Technologies
1. Python:Data ingestion into Snowflake
2. Snowflake:Cloud data warehouse
3. SQL:Data cleaning, transformation, and analysis
4. Tableau:Interactive dashboard visualization

##  Data Ingestion
-  Connected Python to Snowflake using Snowflake connector
-  Uploaded marketing dataset into cloud data warehouse
-  
## Data Preparation
-  Cleaned and transformed raw dataset using SQL
-  Converted text-based cost fields into numeric values
-  Created derived metrics:
    ROI Avg
    Conversion Avg Rate
    Cost Efficiency (ROI per cost)

## Key Insights
1. Campaign performance shows **low variance across types**, indicating a balanced strategy
2. **Influencer campaigns** achieve the highest ROI
3. **Search campaigns** demonstrate better cost efficiency
4. Optimization opportunities lie in **reducing acquisition cost rather than increasing engagement**

##  Dashboard image:


<img width="1919" height="1049" alt="marketing-campaignes-dashboard" src="https://github.com/user-attachments/assets/b3546a89-c59e-4b52-9d7c-4f293305a023" />



## 📂 Project Structure

marketing-campaign-analysis:
  data
  raw_marketing_campaign.csv
  cleaned_marketing_campaign.csv
  scripts
  data_ingestion_snowflake.py
  dashboard
  marketing_dashboard.twbx
  README.md

## Skills Demonstrated
1. Data ingestion and pipeline setup (Python + Snowflake)
2. SQL-based data cleaning and transformation
3. Analytical thinking and business insight generation
4. Interactive dashboard design using Tableau
5. End-to-end data analysis workflow

## Conclusion
This project demonstrates how combining cloud data warehousing, SQL, and visualization tools can support effective marketing analysis and decision-making.
