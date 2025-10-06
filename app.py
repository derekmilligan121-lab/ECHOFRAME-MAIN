import streamlit as st

def load_known_words(language):
    samples = {
        "Latin": {"sol": "sun", "aqua": "water", "terra": "earth", "caelum": "sky", "ignis": "fire"},
        "Nahuatl": {"tonatiuh": "sun", "atl": "water", "tlalli": "earth", "ilhuicatl": "sky", "tletl": "fire"},
        "Old Norse": {"sól": "sun", "vatn": "water", "jörð": "earth", "himinn": "sky", "eldr": "fire"}
    }
    return samples.get(language, {"sola": "sun", "nara": "water", "kuma": "earth", "tira": "sky", "belo": "fire"})

def predict_missing_words():
    return {
        "zuma": "moon",
        "elka": "wind",
        "voro": "spirit",
        "shira": "mountain"
    }

def generate_sentence(known_words):
    actions = ["rises", "flows", "holds", "watches", "burns"]
    return ", ".join([f"{word} {action}" for word, action in zip(known_words.keys(), actions)]) + "."

def translate_sentence(known_words):
    actions = ["rises", "flows", "holds", "watches", "burns"]
    return ", ".join([f"{meaning} {action}" for meaning, action in zip(known_words.values(), actions)]) + "."

# Streamlit UI
st.title("EchoFrame Language Revival Core")
language = st.selectbox("Choose a language", ["Latin", "Nahuatl", "Old Norse", "Default"])

known_words = load_known_words(language)
predicted_words = predict_missing_words()

st.subheader("Known Words")
for word, meaning in known_words.items():
    st.write(f"{word} → {meaning}")

st.subheader("Predicted Words")
for word, meaning in predicted_words.items():
    st.write(f"{word} → {meaning}")

st.subheader("Reconstructed Sentence")
st.write(generate_sentence(known_words))

st.subheader("English Translation")
st.write(translate_sentence(known_words))
