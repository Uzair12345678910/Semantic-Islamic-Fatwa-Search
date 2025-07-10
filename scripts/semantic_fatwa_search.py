from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

#Loads the fine tuned model
print("Loading fine tuned model...")
model = SentenceTransformer("trained_afra_model") 

#Below loads the dataset
print("Loading dataset...")
df = pd.read_excel("merged_fatwas.xlsx")
df['combined'] = df['question'].astype(str) + " " + df['answer'].astype(str)

#Asks if user wants to filter by topic
available_topics = df['topic'].dropna().unique().tolist()

print("\nAvailable Topics:")
for i, topic in enumerate(available_topics):
    print(f"{i+1}. {topic}")

selected = input("\nDo you want to filter by topic? (yes/no): ").strip().lower()

if selected == "yes":
    topic_choice = input("Type the topic name exactly as shown above: ").strip()
    if topic_choice not in available_topics:
        print("Invalid topic. Proceeding without filter.")
        topic_filter = None
    else:
        topic_filter = topic_choice
        print(f"Filtering by topic: {topic_filter}")
else:
    topic_filter = None
    print("No topic filter applied.")

#Below function applies the topic filter
filtered_df = df[df['topic'] == topic_filter] if topic_filter else df
filtered_df = filtered_df.reset_index(drop=True)

#Generate embeddings for the filtered dataset
print("Encoding fatwas...")
embeddings = model.encode(filtered_df['combined'].tolist(), show_progress_bar=True)

#Main loop below
while True:
    query = input("\nAsk your question (or type 'exit' to quit):\n> ")
    if query.lower() == "exit":
        print("Exiting. BarakAllahu feek!")
        break

    query_embedding = model.encode([query])
    similarities = cosine_similarity(query_embedding, embeddings)[0]
    top_n = 3
    top_indices = similarities.argsort()[-top_n:][::-1]

    print(f"\nTop {top_n} results:\n")
    for idx in top_indices:
        print(f"Question: {filtered_df.iloc[idx]['question']}")
        print(f"Answer: {filtered_df.iloc[idx]['answer']}")
        print(f"Topic: {filtered_df.iloc[idx]['topic']}")
        print("—" * 50)
