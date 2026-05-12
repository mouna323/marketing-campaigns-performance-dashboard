# Marketing Campaign Performance Analysis
##  Project Overview
This project presents an end-to-end marketing campaign analysis workflow using Snowflake, SQL, Python, and Tableau.
It evaluates campaign performance across channels and customer segments, focusing on ROI, conversion rate, and cost efficiency to identify optimization opportunities.

##  Objectives
-  Evaluate campaign performance using ROI and conversion rate
-  Compare effectiveness across campaign types and channels
-  Identify cost-efficiency opportunities
-  Support data-driven marketing decisions

## Tools & Technologies
1. Python: used to connect to Snowflake and load dataset (ingest) into cloud warehouse
2. Snowflake:Cloud data warehouse
3. SQL:Data cleaning, transformation, analysis, and KPI calculation
4. Tableau:Interactive dashboard visualization

##  Data Ingestion
-  Connected Python to Snowflake using Snowflake connector
-  Uploaded marketing dataset into cloud data warehouse
-  
## Data Preparation
-  Cleaned and transformed raw dataset using SQL
-  Converted text-based cost fields into numeric values
-  Created derived metrics:
    ROI Avg,
    Conversion Avg Rate,
    Cost Efficiency (ROI per cost)

## Business Problem
Marketing teams need to evaluate campaign performance across multiple channels to optimize ROI and reduce acquisition cost

## Key Insights
1. Campaign performance shows **low variance across types**, indicating a balanced strategy
2. **Influencer campaigns** achieve the highest ROI
3. **Search campaigns** demonstrate better cost efficiency
4. Optimization opportunities lie in **reducing acquisition cost rather than increasing engagement**

##  Dashboard image:


<img width="1919" height="1032" alt="marketing_campaigns_dashboardd" src="https://github.com/user-attachments/assets/db84537f-1723-4a42-8073-1acf387af417" />




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
