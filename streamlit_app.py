import streamlit as st
import textwrap

# Sätt en titel för appen
st.title("Storyboard - Mobilvy")

# Låt användaren välja iPhone-modell
iphone_model = st.selectbox(
    "Välj iPhone-modell:",
    ("iPhone 13", "iPhone 14", "iPhone 15")
)

# Definiera skärmstorlekar för olika iPhone-modeller
iphone_sizes = {
    "iPhone 13": {"width": 390, "height": 844},
    "iPhone 14": {"width": 393, "height": 852},
    "iPhone 15": {"width": 393, "height": 852}
}

# Hämta vald skärmstorlek
screen_size = iphone_sizes[iphone_model]

# Lägg till en text-area för att användaren ska kunna lägga in text
input_text = st.text_area("Klistra in din text här:", height=300)

# Funktion för att dela upp text i "skärmar"
def split_into_screens(text, max_chars=700):
    screens = []
    paragraphs = text.split('\n\n')
    current_screen = ""
    
    for paragraph in paragraphs:
        if len(current_screen) + len(paragraph) <= max_chars:
            current_screen += paragraph + "\n\n"
        else:
            screens.append(current_screen.strip())
            current_screen = paragraph + "\n\n"
    
    if current_screen:
        screens.append(current_screen.strip())
    
    return screens

if input_text:
    screens = split_into_screens(input_text)
    
    for i, screen in enumerate(screens):
        with st.container():
            st.markdown(f"**Skärm {i+1}**")
            col1, col2, col3 = st.columns([1, 6, 1])
            with col2:
                
                st.markdown("Status bar")
                st.markdown("---")
                st.markdown(screen)
                st.markdown("---")
                st.text("ANNAT INNEHÅLL")
            st.markdown("---")

# Lägg till CSS för att begränsa bredden och centrera innehållet
st.markdown(f"""
    <style>
        .reportview-container .main .block-container{{
            max-width: {screen_size['width']}px;
        }}
    </style>
""", unsafe_allow_html=True)
