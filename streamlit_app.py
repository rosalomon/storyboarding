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

def split_into_screens(text, screen_height):
    screens = []
    lines = text.split('\n')
    current_screen = []
    current_height = 0
    line_height = 20  # Uppskattad höjd för en textrad i pixlar
    
    for line in lines:
        line_count = max(1, len(textwrap.wrap(line, width=40)))  # Uppskatta antal rader för denna textrad
        line_total_height = line_count * line_height
        
        if current_height + line_total_height > screen_height - 100:  # 100 pixlar för header och footer
            screens.append('\n'.join(current_screen))
            current_screen = [line]
            current_height = line_total_height
        else:
            current_screen.append(line)
            current_height += line_total_height
    
    if current_screen:
        screens.append('\n'.join(current_screen))
    
    return screens

if input_text:
    screen_height = screen_size['height']
    screens = split_into_screens(input_text, screen_height)
    
    for i, screen in enumerate(screens):
        st.markdown(f"""
        <div style="
            width: {screen_size['width']}px;
            height: {screen_size['height']}px;
            border: 2px solid black;
            margin: 20px auto;
            padding: 10px;
            overflow: hidden;
            position: relative;
            font-family: Arial, sans-serif;
        ">
            <div style="
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                height: 40px;
                background-color: #f0f0f0;
                padding: 5px;
                text-align: center;
            ">
                Status bar
            </div>
            <div style="
                margin-top: 50px;
                margin-bottom: 50px;
                height: calc(100% - 100px);
                overflow-y: auto;
                white-space: pre-wrap;
            ">
                {screen}
            </div>
            <div style="
                position: absolute;
                bottom: 0;
                left: 0;
                right: 0;
                height: 40px;
                background-color: #f0f0f0;
                padding: 5px;
                text-align: center;
            ">
                ANNAT INNEHÅLL
            </div>
        </div>
        """, unsafe_allow_html=True)

# Lägg till CSS för att begränsa bredden och centrera innehållet
st.markdown(f"""
    <style>
        .reportview-container .main .block-container{{
            max-width: {screen_size['width']}px;
        }}
    </style>
""", unsafe_allow_html=True)
