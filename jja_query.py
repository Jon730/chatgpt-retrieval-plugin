import openai
import qdrant_client
import requests

def describe_collection(collection_name):
    response = requests.get(f"http://localhost:6333/collections/{collection_name}")
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

collection_name = "document_chunks"
collection_config = describe_collection(collection_name)
client = qdrant_client.QdrantClient(
    host="localhost",
    prefer_grpc=True,
)
if collection_config is not None:
    print(collection_config)

def query_qdrant(
        query,
        collection_name,
        #vector_name="vectors",
        top_k=20):
    vector_config = collection_config["result"]["config"]["params"][vector_name]

    # Creates embedding vector from user query
    embedded_query = openai.Embedding.create(
        input=query,
        model="text-embedding-ada-002",
    )["data"][0]["embedding"]

    query_results = client.search(
        collection_name=collection_name,
        query_vector=(
            vector_name, embedded_query
        ),
        limit=top_k,
    )

    return query_results

query_results = query_qdrant("messages about customers", "document_chunks")
for i, article in enumerate(query_results):
    print(f"{i + 1}. {article.payload['title']} (Score: {round(article.score, 3)})")
