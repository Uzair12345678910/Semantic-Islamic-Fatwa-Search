from sentence_transformers import SentenceTransformer, InputExample, losses
from torch.utils.data import DataLoader
import pickle

#Load training examples from .pkl
with open("fatwa_train_examples.pkl", "rb") as f:
    train_examples = pickle.load(f)

#Initialize the model
model = SentenceTransformer('all-MiniLM-L6-v2')

#DataLoader
train_dataloader = DataLoader(train_examples, shuffle=True, batch_size=16)

#Loss function
train_loss = losses.MultipleNegativesRankingLoss(model)

#Train model function
model.fit(
    train_objectives=[(train_dataloader, train_loss)],
    epochs=1,  # Increase to 2–4 for better results
    show_progress_bar=True
)

#Save the model
model.save("trained_afra_model")
print("Model saved to 'trained_afra_model'")
