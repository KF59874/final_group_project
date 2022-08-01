# Final Group Project - Second Segment

Welcome to the final group project of the Data Analytics Bootcamp. This final project has been designed to showcase the skills learned in the bootcamp.
Each team member has been assigned a role to complete for the project: 

Group members and their respective roles are as follows:
- Circle: Katrin Freitag
- Square: Boakye Twum
- Triangle: Matthew Lao
- X: Anand Bajaj

As a group, we have decided to anlayze whether negative reviews can give insight as to why Italian restaurants closed in California by looking at frequently used words in reviews.  

## Second Segment Requirements

### Project Information 
For this project, we have decided to analyze customers preference for Italian restaurants in the State of California. To help analyze customer preferences, we are using the [Yelp Dataset](https://www.yelp.com/dataset/), as it provides a large amount of information regarding American and Canadian businesses. It provides information regarding users, business reviews, star ratings, rating counts, and tips. Each business is also categorized, making it easier to filter out the required data for the analysis. The dataset has been cleaned, organized and exported into csv files for future analysis:

- [Italian Restaurants in California](Sample%20Data/BusinessTop1000.csv)
- [Italian Restaurant Reviews](Sample%20Data/ReviewTop1000.csv)

The relationship between each dataset has been visualized using and ERD model:
![ERD](Sample%20Data/Yelp_ERD.png)

Usind this data, we are trying to gather more information to analzye the following **Business Problem**: 
*Why have Italian restaurants closed in California? Are there common words that describe closed restaurants?*

### GitHub 
To complete the GitHub requirements for the second segment, the [project page](https://github.com/KF59874/final_group_project) includes the following: 
1. Main Branch
2. A README.md
3. Separate branch for each group member

### Database
A database has been created using AWS and accomplishes the following:
- The final data structure for Italian Restaurants in California
- Draft [machine learning module](Machine_learning.png) is connected to the database

### Machine Learning Model
A [machine learning model](https://drive.google.com/file/d/1_wmv60re-pS7dPL-D9dmgqGSHH5POJXZ/view?usp=sharing) has been created to analyse the reviews for Italian restaurants in California. It includes the following:

- Dataset: Yelp Academic Dataset
- Analysis: Machine Learning
- Type: Supervised
- Branch: Classification model


The following models have been explored in the model:
- Logistic Regression Model
- Support Vector Model
- Random Forest Model

In the event we run into the problem of class imbalances, then the following models can be explored to arrive at the best model that yields the best results:

- **Random Over Sampler** and **SMOTE algorithms** for over sample
- **Cluster Centroids algorithms** for under sample
- **SMOTEEN** for both over and under sample
- **Balanced Random Forest Classifier** and **Easy Ensemble Classifier** for bias reduction

![Models](Models.png)

### Dashboard 
A [Google Slide](https://docs.google.com/presentation/d/1H_uyNrVu5GQB9j9eYNoXr4UrZ_MOYtHKkx7B3Pkjguo/edit?usp=sharing) has been created to showcase the preliminary presentation requirements. It includes the following visualizations: 

![20 frequently used words](Sample%20Data/Yelp_ERD.png)

![Star rating distribution](Sample%20Data/Yelp_ERD.png)

![Text length distribution](Sample%20Data/Yelp_ERD.png)
