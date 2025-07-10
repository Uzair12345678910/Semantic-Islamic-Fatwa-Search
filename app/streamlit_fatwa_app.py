import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

#Load the model and data
@st.cache_resource
def load_model():
    return SentenceTransformer("trained_afra_model")  

@st.cache_data
def load_data():
    df = pd.read_excel("merged_fatwas.xlsx")
    df["combined"] = df["question"].astype(str) + " " + df["answer"].astype(str)
    return df

model = load_model()
df = load_data()

st.title("AFRA: Fatwa Semantic Search")
st.markdown("Search Islamic QA with AI powered semantic understanding.")

#Topic filter below
topics = df["topic"].dropna().unique().tolist()
selected_topic = st.selectbox("Filter by Topic (optional):", ["All Topics"] + topics)

if selected_topic != "All Topics":
    filtered_df = df[df["topic"] == selected_topic].reset_index(drop=True)
else:
    filtered_df = df

#Precompute embeddings
@st.cache_data
def compute_embeddings(data):
    return model.encode(data["combined"].tolist(), show_progress_bar=False)

embeddings = compute_embeddings(filtered_df)

# Query input
query = st.text_input("Ask a question:")

if query:
    query_embedding = model.encode([query])
    similarities = cosine_similarity(query_embedding, embeddings)[0]

    top_n = 3
    top_indices = similarities.argsort()[-top_n:][::-1]

    st.subheader(f"Top {top_n} Fatwa Results")
    for idx in top_indices:
        st.markdown("-" * 30)
        st.markdown(f"**Question:** {filtered_df.iloc[idx]['question']}")
        st.markdown(f"**Answer:** {filtered_df.iloc[idx]['answer']}")
        st.markdown(f"**Topic:** {filtered_df.iloc[idx]['topic']}")
        st.markdown(f"**Similarity Score:** {similarities[idx]:.2f}")

