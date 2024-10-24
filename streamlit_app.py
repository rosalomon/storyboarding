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

# Funktion för att dela texten baserat på meningsgränser och bevara formateringen
def split_text_into_paragraphs(text, max_length=700):
    paragraphs = []
    current_paragraph = ""
    
    for line in text.split('\n'):
        if len(current_paragraph) + len(line) + 1 <= max_length:  # +1 för eventuell radbrytning
            if current_paragraph:
                current_paragraph += '\n'
            current_paragraph += line
        else:
            if current_paragraph:
                paragraphs.append(current_paragraph)
            current_paragraph = line
    
    if current_paragraph:
        paragraphs.append(current_paragraph)
    
    return paragraphs

# Kontrollera om någon text har lagts in
if input_text:
    paragraphs = split_text_into_paragraphs(input_text, max_length=700)

    for i, paragraph in enumerate(paragraphs):
        formatted_paragraph = paragraph.replace('\n', '<br>')
        st.markdown(f"""
        <div class='content-box'>
            <div class='text-output'><b>Scroll {i+1}:</b><br>{formatted_paragraph}</div>
            <div class="dashed-box">
                ANNAT INNEHÅLL
            </div>
        </div>
        """, unsafe_allow_html=True)
