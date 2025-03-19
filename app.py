import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("cleaned_ecommerce_data_final.csv")
    df["combined_text"] = df["product_name"] + " " + df["category"] + " " + df["about_product"]
    return df

df = load_data()

# Load SBERT Model
@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

model = load_model()

# Generate Embeddings
@st.cache_data
def generate_embeddings(texts):
    return model.encode(texts, convert_to_tensor=True)

embeddings = generate_embeddings(df["combined_text"].astype(str).tolist())
cosine_sim = cosine_similarity(embeddings.cpu().numpy())

# Recommendation Function
def recommend_products(product_index, top_n=5):
    scores = list(enumerate(cosine_sim[product_index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    top_products = scores[1:top_n+1]  # Exclude itself
    return top_products

# Streamlit UI
st.title("🔍 E-Commerce Recommendation System")
st.write("Find similar products based on content similarity.")

# Use short names for the dropdown
selected_short_name = st.selectbox("Choose a product:", df["short_name"].tolist())

# Get full product name based on the short name
full_product_name = df[df["short_name"] == selected_short_name]["product_name"].values[0]

if st.button("Recommend Similar Products"):
    product_index = df[df["product_name"] == full_product_name].index[0]
    recommendations = recommend_products(product_index)

    st.subheader(f"Recommended Products for: {full_product_name}")
    for idx, score in recommendations:
        st.write(f"✅ **{df.iloc[idx]['product_name']}** (Similarity: {score*100:.2f}%)")
        st.image(df.iloc[idx]["img_link"], width=150)
