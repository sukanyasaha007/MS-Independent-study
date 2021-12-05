# ImageNet database

## Motivation

In an abundance of image data, it was difficult to organize the data for solving crucial problems let alone build robust and sophisticated models and algorithms. Hence, there was a need for annotated images that would have some measure of hierarchy like wordnet. ImageNet was designed to fulfill the need for large-scale, accurate, and diverse data and revolutionize computer vision research. The authors believed that a large-scale ontology of images was important for developing advanced and content-based image search and image understanding algorithms and for providing critical training and benchmarking data for such algorithms.

## Contributions

Some of the claimed contributions of the ImageNet dataset is-
It was claimed to be the central resource for computer vision researchers
ImageNet was designed to contain images of all object classes apart from the most common ones like pedestrians, cars, and faces. It can reduce biases in types of objects covered in prior datasets.
It was intended to be the benchmark dataset after CalTech’s 101/256 and Pascal which played a vital role in the domain of object recognition of scene classification.
Since it has similarities to the wordnet hierarchy of interconnected synsets, it could be used to understand the semantic relations of objects.
The authors also said that it will help researchers understand the human visual system.

## Data Collection

The authors collected the data from several search engines. They started with collecting candidate images for each synset. Since the accuracy of the image search on search engines is only 10% they had approximately 500-1000 clean images from 10k candidate images per synset. Due to constraints on image retrieval, they expanded the query set by adding queries with parent synsets’ words. They diversified the collection by translating queries to other languages. Authors used Amazon Mechanical Truck where they put data for checking accuracy for users to confirm. In that users check images for verifying objects from synsets. They also had majority-based quality control to counter human error.

ImageNet dataset uses the hierarchical structure of wordnet. In wordnet, meaningful concepts are described by multiple words or phrases which is called a synset. Wordnet has 80k noun synsets where ImageNet provides 500-100 images per synset. It has 12 subtrees when the paper was written. Overall it has 5247 synsets and 3.2M images. Like wordnet, ImageNet synsets of images are interlinked by several different types of relationships. Its category labels can be mapped into a semantic hierarchy by using wordnet, though ImageNet is denser eg. It has 147 dog categories.

