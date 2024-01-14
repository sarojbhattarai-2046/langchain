## Embeddings

Embeddings are representations of values or objects like text, images, and audio that are designed to be consumed by machine learning models and semantic search algorithms. They translate objects like these into a mathematical form according to the factors or traits each one may or may not have, and the categories they belong to.

Essentially, embeddings enable machine learning models to find similar objects. Given a photo or a document, a machine learning model that uses embeddings could find a similar photo or document. Since embeddings make it possible for computers to understand the relationships between words and other objects, they are foundational for artificial intelligence (AI).



An embedding is a list of numbers between -1 and 1 that score how much a piece of text is talking about some particular quality.

These embeddings only rate 2 qualities, but real embeddings frequently have 700 to 1500 "dimenesions" or qualities that they score.

1. Squared L2: Using the distance between two points to figure out how similar they are;
2. Cosine Similarity: Using the angle between two vectors to figure out how similar they are;

Embedding Model:
1. SentenceTransformer(all-mpnet-base-v2) -> 768 dimension
2. OpenAI Embeddings -> 1536 dimensions