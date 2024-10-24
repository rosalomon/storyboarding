import streamlit as st
import re

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

# CSS-styling och JavaScript för att simulera en mobilvy
st.markdown(f"""
    <style>
    .main {{
        max-width: 430px;
        margin: 0 auto;
    }}
    .mobile-screen {{
        width: {screen_size['width']}px;
        height: {screen_size['height']}px;
        border: 2px solid #000;
        margin: 20px auto;
        padding: 20px;
        overflow: hidden;
        position: relative;
        box-sizing: border-box;
    }}
    .content-box {{
        font-size: 16px;
        line-height: 1.5;
        white-space: pre-wrap;
    }}
    .dashed-box {{
        border: 2px dashed #999;
        padding: 20px;
        text-align: center;
        color: #666;
        font-style: italic;
        margin-top: 10px;
    }}
    </style>
    
    <script>
    function splitIntoScrolls() {{
        const mobileScreen = document.querySelector('.mobile-screen');
        const contentBox = mobileScreen.querySelector('.content-box');
        const content = contentBox.innerHTML;
        const screenHeight = mobileScreen.clientHeight;
        
        let scrolls = [];
        let currentScroll = '';
        let tempDiv = document.createElement('div');
        tempDiv.style.cssText = window.getComputedStyle(contentBox).cssText;
        tempDiv.style.width = contentBox.offsetWidth + 'px';
        document.body.appendChild(tempDiv);
        
        for (let line of content.split('\\n')) {{
            tempDiv.innerHTML = currentScroll + line + '<br>';
            if (tempDiv.offsetHeight > screenHeight - 100) {{  // 100px för marginal och "ANNAT INNEHÅLL"
                scrolls.push(currentScroll.trim());
                currentScroll = '';
            }}
            currentScroll += line + '\\n';
        }}
        if (currentScroll) {{
            scrolls.push(currentScroll.trim());
        }}
        
        document.body.removeChild(tempDiv);
        return scrolls;
    }}
    
    function displayScrolls() {{
        const scrolls = splitIntoScrolls();
        const container = document.getElementById('scrolls-container');
        container.innerHTML = '';
        scrolls.forEach((scroll, index) => {{
            const scrollDiv = document.createElement('div');
            scrollDiv.className = 'mobile-screen';
            scrollDiv.innerHTML = `
                <div class="content-box">${{scroll.replace(/\\n/g, '<br>')}}</div>
                <div class="dashed-box">ANNAT INNEHÅLL</div>
            `;
            container.appendChild(scrollDiv);
        }});
    }}
    
    window.addEventListener('load', displayScrolls);
    window.addEventListener('resize', displayScrolls);
    </script>
    
    <div id="scrolls-container"></div>
    """, unsafe_allow_html=True)

if input_text:
    st.markdown(f"""
    <div class="mobile-screen">
        <div class="content-box">{input_text}</div>
    </div>
    <script>
    displayScrolls();
    </script>
    """, unsafe_allow_html=True)
