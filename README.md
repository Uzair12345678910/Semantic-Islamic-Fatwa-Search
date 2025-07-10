# Semantic-Islamic-Fatwa-Search
AFRA (Automated Fatwa Research Assistant) is a semantic search tool that uses natural language processing (NLP) techniques and was trained on real Islamic fatwa literature. Users may utilize common inquiries to search for fatwas, and it will provide pertinent legal views with scholarly traceability. AFRA develops a context aware fatwa retrieval engine by refining a transformer based model (MiniLM) on selected scholarly texts.


Project Goals:

-Fine-tune a transformer-based model (Sentence-BERT) on Islamic texts

-Enable semantically intelligent retrieval of Islamic legal rulings (fatwas)

-Structure the dataset with traceable question–answer–topic format

-Provide an optional lightweight Streamlit interface for practical use

-Build a project that is accessible to both laymen and researchers


Technologies Used:

-Python 3.9+

-sentence-transformers (all-MiniLM-L6-v2)

-PyTorch, HuggingFace Transformers

-scikit-learn (cosine similarity)

-pandas, numpy, json, openpyxl

-Streamlit (optional frontend)

-Git and GitHub for version control


Repository Structure: 

AFRA/
├── app/                         #Optional Streamlit frontend interface
├── data/                        #JSON/Excel dataset files
├── model/                       #Fine tuned Sentence-BERT model checkpoints
├── scripts/
│   ├── prepare_training_data.py     #Converts XLSX to training examples
│   ├── train_model.py               #Fine tunes the transformer model
│   ├── semantic_fatwa_search.py     #Main semantic search engine
│   └── fatwa_search.py              #Legacy keyword search
├── merged_fatwas.xlsx           #Final cleaned fatwa dataset
├── fatwa_train_examples.pkl     #Serialized training data
├── requirements.txt             #All Python dependencies
├── README.md                    #Project overview
├── LICENSE                      #Apache 2.0 License

Installation:

To run the project locally (All code is run on bash): 

git clone https://github.com/Uzair12345678910/Semantic-Islamic-Fatwa-Search.git

cd Semantic-Islamic-Fatwa-Search

pip install -r requirements.txt

python scripts/fatwa_search.py


Running The Project:

#Semantic Search: 
python scripts/semantic_fatwa_search.py


#Fine Tune The Transformer-Based Model: 
python scripts/train_model.py

#Launch On The Streamlit Local Interface: 
streamlit run app/app.py


Dataset:

The dataset is sourced from IslamQA. Every entry in merged_fatwas.xlsx includes:

question – the user’s or scholar’s inquiry

answer – the corresponding scholarly legal opinion

topic – thematic categorization (Faith, Family, Politics)

All entries are manually reviewed and structured for semantic training. The data is suitable for supervised learning in sentence similarity tasks.


Example Usage:

Select Principles of Fiqh from dropdown

Input: "Can I delay my prayer when travelling?"

Output: Returns the most semantically relevant fatwa using cosine similarity that discusses conditions under which prayers may be delayed during travel, based on sentence embeddings


Model Training Summary:

-852 question and answer pairs used for training

-Training objective was cosine similarity loss using SentenceTransformer

-Embeddings stored and queried efficiently with scikit-learn

-Option to retrain on expanded or more granular classical sources like Sharh Aqeedah Al Tahawiyyah by Ibn Al Izz Al Hanafi


Motivation:

Islamic fatwa databases are predominantly based on keyword searches, returning results that match terms but not the intent of the questions; AFRA uses semantic search to improve precision by understanding the meaning of queries. This project helps students, scholars, and researchers navigate classical legal opinion in a more intuitive way.

Author:

Uzair Ur Rahman
Electrical Engineering and Computer Science Double Degree Student at the University of Western Ontario
Github: github.com/Uzair12345678910


License:

This project is released under the Apache 2.0 License.


Future Work and Updates:

-Expand the dataset with multilingual fatwas in Arabic, Urdu, and Farsi

-Add metadata fields like authorship and school of thought/madhab

-Enable interactive feedback loop to improve ranking

-Deploy a live public demo using Hugging Face Spaces

-Support real time tagging and retraining


Contributing:

Contributions are more than welcome; if you are a researcher or scholar, we especially welcome domain feedback. Please open an issue or submit a pull request to suggest enhancements, corrections, or expansions.
