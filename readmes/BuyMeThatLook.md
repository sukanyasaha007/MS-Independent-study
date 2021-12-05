# Buy Me That Look

## Summery

The research paper states, in short, is to detects all products in an image and retrieves similar fashion clothes from the database with a product buy link.
Online business has become important in day-to-day life for everyone. Virtual stores allow people to shop from the comfort of their homes without the pressure of a salesperson. In this paper, the authors focus on the retrieval of multiple fashion items at once and propose an architecture that detects all products from an image and recommends similar kinds of products.

## Method

Stage 1: (Pose Estimation)
In this stage, We will detect whether the image is a Full-Front-pose image or not. So this will be a binary classifier (Yes/No)
Stage 2: (Localization and Article Detection)
In this stage, we detect all the articles (clothes) and particular places the article is placed or located. This will be Both a classification and Regression Problem. Classification because of Article Detection and Regression because of Localization (Bounding Box Co-ordinates)
Stage 3: (Image_embeddings)
In this stage, we will generate the embedding ( dense vectors ) for the images as discussed below.
Stage 4: (Getting similar Images)
In this stage, we will use Faiss library to fetch similar clothes based on search query.
