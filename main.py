from src.embedder import fetch_and_embed
from src.vector_store import add_topic_to_vector_store, search_index
from src.gemini_bot import get_fallback_response

CHUNK_SIZE = 500  # ✅ Ensure chunking is controlled here

def main():
    while True:
        print("\n1. Fetch Topic")
        print("2. Ask Question")
        print("3. Exit")
        choice = input("Choose: ")

        if choice == "1":
            topic = input("Enter topic name: ")
            chunks, embeddings = fetch_and_embed(topic, chunk_size=CHUNK_SIZE)
            if chunks:
                add_topic_to_vector_store(topic, chunks, embeddings)
        elif choice == "2":
            q = input("Enter your question: ")
            top_chunks = search_index(q, k=3)
            print("🔍 Top Chunks Found:")
            for i, chunk in enumerate(top_chunks):
                print(f"{i+1}. {chunk}\n")
            if top_chunks:
                context = "\n".join(top_chunks)
                ans = get_fallback_response(f"Answer the question using only this:\n{context}\n\nQ: {q}")
            else:
                ans = get_fallback_response(q)
            print(f"\n🧠 Answer:\n{ans}")
        else:
            break

if __name__ == "__main__":
    main()
