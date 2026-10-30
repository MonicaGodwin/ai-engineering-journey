Vectors and Matrices in AI Engineering

1. What Is a Vector?
A vector is an ordered collection of numbers.

In simple terms, a vector can represent a point, a direction, or a set
of measurements.

2. What Is an Embedding?
An embedding is a numerical vector that represents the meaning or
characteristics of something, such as a word, sentence, image, or
product.

For example, an AI model may represent the words apple and orange
with vectors that are closer to each other than the vectors for apple
and car.

This is because apples and oranges are both fruits, while a car is a
different concept.

The numbers are learned by the model; they are not manually chosen
descriptions of the words.

Embeddings help AI systems with tasks such as:
- Finding information by meaning rather than exact keyword matches.
- Comparing how similar two pieces of information are.
- Building recommendation and search systems.
- Retrieving relevant information for Retrieval-Augmented Generation
  (RAG).
- Storing and searching representations in vector databases.
Important: raw image pixels and image embeddings are not the same
thing. Pixels are the image's raw numerical data. An image embedding is
a vector produced by a model to capture useful features of the image.

3. Understanding Vector Magnitude
The magnitude of a vector tells us its length.

For a two-dimensional vector [x, y], calculate its magnitude using:

\(`\text{magnitude}`{=tex} = `\sqrt{x^2 + y^2}`{=tex}\)