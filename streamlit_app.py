import streamlit as st
import re

# Sätt en titel för appen
st.title("Storyboard - Mobilvy")

# Lägg till en text-area för att användaren ska kunna lägga in text
input_text = st.text_area("Klistra in din text här:", height=300)

# CSS-styling för att simulera en mobilvy och lägga till tunn linje runt varje stycke + ANNAT INNEHÅLL
st.markdown("""
    <style>
    .main {
        max-width: 430px;
        margin: 0 auto;
    }
    .content-box {
        border: 1px solid #ccc;
        padding: 15px;
        margin-bottom: 20px;
        max-width: 400px;
        margin: 10px auto;
        border-radius: 5px;
    }
    .dashed-box {
        border: 2px dashed #999;
        padding: 20px;
        text-align: center;
        color: #666;
        font-style: italic;
        margin-top: 10px;
        border-radius: 5px;
    }
    .text-output {
        font-size: 18px;
        line-height: 1.6;
        max-width: 400px;
        margin: 10px auto;
    }
    </style>
    """, unsafe_allow_html=True)

# Funktion för att dela texten baserat på meningsgränser
def split_text_into_paragraphs(text, max_length=700):
    # Dela texten vid punkt, utropstecken eller frågetecken som avslutas med ett mellanrum
    sentences = re.split(r'(?<=[.!?]) +', text)
    
    paragraphs = []
    current_paragraph = ""
    
    for sentence in sentences:
        # Om vi lägger till en mening och den totala längden fortfarande är under max_length, lägg till den i det nuvarande stycket
        if len(current_paragraph) + len(sentence) <= max_length:
            current_paragraph += sentence + " "
        else:
            # Om det nuvarande stycket är fullt, lägg till det till listan och börja ett nytt stycke
            paragraphs.append(current_paragraph.strip())
            current_paragraph = sentence + " "
    
    # Lägg till sista stycket
    if current_paragraph:
        paragraphs.append(current_paragraph.strip())
    
    return paragraphs

# Kontrollera om någon text har lagts in
if input_text:
    # Dela texten baserat på meningsgränser och max 700 tecken per stycke
    paragraphs = split_text_into_paragraphs(input_text, max_length=700)

    # Loopa över varje stycke och visa det tillsammans med "ANNAT INNEHÅLL"
    for i, paragraph in enumerate(paragraphs):
        # Visa stycket med en tunn linje runt det
        st.markdown(f"""
        <div class='content-box'>
            <div class='text-output'><b>Scroll {i+1}:</b><br>{paragraph}</div>
            <div class="dashed-box">
                ANNAT INNEHÅLL
            </div>
        </div>
        """, unsafe_allow_html=True)
