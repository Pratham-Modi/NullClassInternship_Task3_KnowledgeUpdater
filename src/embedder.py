import wikipedia
from sentence_transformers import SentenceTransformer
import time

model = SentenceTransformer('all-MiniLM-L6-v2')

def fetch_and_embed(topic, chunk_size=1000):
    print(f"\n📚 Fetching data for: {topic}")
    try:
        text = wikipedia.page(topic).content
    except:
        try:
            text = wikipedia.search(topic)[0]
            text = wikipedia.page(text).content
        except Exception as e:
            print(f"❌ Wikipedia fetch failed: {e}")
            return [], []

    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    print(f"🧠 Chunked into {len(chunks)} parts of ~{chunk_size} chars")

    start = time.time()
    embeddings = model.encode(chunks).tolist()
    print(f"✅ Embedding complete in {time.time() - start:.2f}s")
    return chunks, embeddings
