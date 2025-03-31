🔍 E-Commerce Recommendation System
This project is a content-based recommendation system that suggests similar products based on their names, categories, and descriptions. It leverages Sentence Transformers (SBERT) for generating text embeddings and cosine similarity to find the most relevant products.

🚀 Features
Uses SBERT (all-MiniLM-L6-v2) to generate product embeddings.

Calculates cosine similarity between products to recommend the most similar ones.

Interactive UI built with Streamlit to select a product and view recommendations.

Displays recommended product names and images for a smooth user experience.

🛠️ Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/ecommerce-reco-system.git
cd ecommerce-reco-system
Install the required packages:

bash
Copy
Edit
pip install -r requirements.txt
Download the pre-trained model:
The system automatically downloads the SBERT model (all-MiniLM-L6-v2).

Run the app:

bash
Copy
Edit
streamlit run app.py
🗃️ Dataset
Make sure to have the cleaned dataset in the root directory:

cleaned_ecommerce_data_final.csv

The dataset should have the following columns:

product_name

category

about_product

short_name

img_link

📝 How It Works
Load the product data and preprocess it.

Generate embeddings using SBERT.

Calculate cosine similarity between product embeddings.

Select a product from the dropdown to view similar recommendations.

💡 Usage
Start the app using the command provided above.

Choose a product from the dropdown.

Click "Recommend Similar Products" to see suggestions.

![Screenshot 2025-03-31 182429](https://github.com/user-attachments/assets/706f3d43-2a98-48d6-a360-31eaf90195a0)


![Screenshot 2025-03-31 182438](https://github.com/user-attachments/assets/e1e3fb9d-921f-4a7c-9aa7-a0186ee26cf5)




📂 File Structure
bash
Copy
Edit
├── app.py                   # Main Streamlit application  
├── cleaned_ecommerce_data_final.csv  # Dataset file  
├── requirements.txt         # Dependencies  
└── README.md                # Project documentation  
📝 Requirements
Python 3.x

pandas

streamlit

sentence-transformers

scikit-learn
