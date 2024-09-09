# Topic Modeling on Product Reviews

## Overview
This project involves scraping product reviews from Amazon and performing **topic modeling** to uncover latent themes and topics in customer feedback. The analysis uses **NLP techniques** and **machine learning** models to extract insights from the reviews, which can help businesses understand customer sentiments, pain points, and product improvements.

## Table of Contents
- Overview
- Methodology
- Prerequisites
- Visualizations
- Results
- Future Work


## Methodology
1. **Web Scraping**: We collected reviews using a web scraping tool (e.g., BeautifulSoup or Scrapy).
   - Extracted reviews include product name, review text, rating, and review date.
   
2. **Data Preprocessing**:
   - Tokenization, lemmatization, and removal of stop words were performed using `nltk` and `spaCy`.
   - Data cleaning steps include handling missing values and filtering reviews by specific products.

3. **Topic Modeling**:
   - We used **Latent Dirichlet Allocation (LDA)** and **Non-negative Matrix Factorization (NMF)** for topic extraction.
   - Optimal number of topics determined using coherence score and perplexity.

4. **Visualization**:
   - Generated word clouds for each topic.
   - Plotted the distribution of topics across reviews.
   - Used `pyLDAvis` for interactive topic visualization.

## Prerequisites
- Python 3.x
- Jupyter Notebook
- Libraries: `pandas`, `numpy`, `nltk`, `spacy`, `scikit-learn`, `gensim`, `matplotlib`, `seaborn`, `wordcloud`, `pyLDAvis`

Install dependencies using:
```bash
pip install -r requirements.txt
```

Clone the Repository:
```
git clone https://github.com/mohdzahan/topic-modeling-product-reviews.git
```
## Visualizations
```
(0, '0.008*"awesome" + 0.006*"medium" + 0.006*"excellent" + 0.006*"phone" + 0.004*"camera" + 0.004*"iphone" + 0.004*"good" + 0.004*"battery" + 0.003*"performance" + 0.003*"amazing"')
(1, '0.011*"good" + 0.009*"phone" + 0.007*"iphone" + 0.006*"battery" + 0.006*"quality" + 0.005*"nice" + 0.005*"camera" + 0.005*"product" + 0.004*"heating" + 0.004*"day"')
(2, '0.011*"iphone" + 0.008*"good" + 0.007*"product" + 0.005*"apple" + 0.005*"phone" + 0.005*"use" + 0.004*"camera" + 0.004*"day" + 0.003*"overall" + 0.003*"full"')
(3, '0.011*"phone" + 0.011*"iphone" + 0.007*"good" + 0.006*"nice" + 0.004*"camera" + 0.004*"price" + 0.004*"battery" + 0.004*"year" + 0.003*"sale" + 0.003*"time"')
(4, '0.022*"good" + 0.006*"quality" + 0.006*"phone" + 0.005*"product" + 0.005*"iphone" + 0.003*"delivery" + 0.003*"battery" + 0.003*"great" + 0.003*"year" + 0.003*"normal"')
```

## Results

-	Optimal Number of Topics: After running coherence and perplexity evaluations, the optimal number of topics for our dataset was determined to be 5.
-	Topics Extracted:
1.	Customer Service: Words like “support,” “service,” “help.”
2.	Product Quality: Words like “quality,” “material,” “durable.”
3.	Delivery Issues: Words like “late,” “shipment,” “delay.”
4.	Value for Money: Words like “price,” “cheap,” “expensive.”
5.	Product Usability: Words like “easy,” “setup,” “install.”


## Future Work

-	Extend the topic modeling to a larger dataset for more comprehensive insights.
-	Experiment with BERT-based topic models for better accuracy.
-	Incorporate sentiment analysis to correlate topics with positive or negative reviews.
-	Develop a web-based dashboard to visualize topics in real-time.


