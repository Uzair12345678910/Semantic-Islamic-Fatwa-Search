import pandas as pd

#Load the Excel file
df = pd.read_excel("merged_fatwas.xlsx")  #also can upload file

#Greets user first
gender = input("Are you a man or woman? ").strip().lower()
if gender == "man":
    print("Salam Ustadh!\n")
elif gender == "woman":
    print("Salam Ustadha!\n")
else:
    print("Salam!\n")

#Then shows available topics from a dropdown list
unique_topics = df['topic'].dropna().unique()
print("Available topics:")
for idx, topic in enumerate(unique_topics, start=1):
    print(f"{idx}. {topic}")

#The user can choose a topic
topic_choice = input("\nEnter the topic name from above: ").strip().lower()

#Fatwas are then filtered to that selected topic
df_topic = df[df['topic'].str.lower() == topic_choice]

if df_topic.empty:
    print("No fatwas found for that topic.")
else:
    #keyword search
    query = input("\nEnter your question or keyword to search within that topic: ").strip().lower()

    matches = df_topic[
        df_topic['question'].str.lower().str.contains(query) |
        df_topic['answer'].str.lower().str.contains(query)
    ]

    if matches.empty:
        print("No matching fatwas found in this topic.")
    else:
        print(f"\nFound {len(matches)} result(s):\n")
        for idx, row in matches.iterrows():
            print(f"Question: {row['question']}")
            print(f"Answer: {row['answer']}")
            print(f"Topic: {row['topic']}")
            print("-" * 50)
