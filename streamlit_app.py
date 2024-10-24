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
css_and_js = f"""
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
        padding: 0;
        overflow: hidden;
        position: relative;
        box-sizing: border-box;
        font-family: -apple-system, BlinkMacSystemFont, sans-serif;
    }}
    .status-bar {{
        height: 44px;
        background-color: #fff;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0 10px;
        font-size: 14px;
    }}
    .header {{
        height: 50px;
        background-color: #fff;
        border-bottom: 1px solid #e0e0e0;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0 10px;
        font-size: 16px;
    }}
    .content-box {{
        height: calc(100% - 144px);  /* Subtract status bar, header, and footer heights */
        overflow-y: auto;
        padding: 10px;
    }}
    .article-text {{
        font-size: 18px;
        line-height: 1.5;
        color: #333;
    }}
    .fact-box {{
        background-color: #f0f0f0;
        padding: 10px;
        margin: 10px 0;
        font-size: 16px;
    }}
    .footer {{
        height: 50px;
        background-color: #fff;
        border-top: 1px solid #e0e0e0;
        position: absolute;
        bottom: 0;
        width: 100%;
    }}
    </style>
    
    <script>
    function splitIntoScrolls() {{
        const mobileScreen = document.querySelector('.mobile-screen');
        const contentBox = mobileScreen.querySelector('.content-box');
        const content = contentBox.innerHTML;
        const screenHeight = contentBox.clientHeight;
        
        let scrolls = [];
        let currentScroll = '';
        let tempDiv = document.createElement('div');
        tempDiv.style.cssText = window.getComputedStyle(contentBox).cssText;
        tempDiv.style.height = 'auto';
        tempDiv.style.position = 'absolute';
        tempDiv.style.visibility = 'hidden';
        document.body.appendChild(tempDiv);
        
        for (let paragraph of content.split('\\n\\n')) {{
            tempDiv.innerHTML = currentScroll + '<p>' + paragraph + '</p>';
            if (tempDiv.offsetHeight > screenHeight) {{
                scrolls.push(currentScroll);
                currentScroll = '<p>' + paragraph + '</p>';
            }} else {{
                currentScroll += '<p>' + paragraph + '</p>';
            }}
        }}
        if (currentScroll) {{
            scrolls.push(currentScroll);
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
                <div class="status-bar">14:38</div>
                <div class="header">
                    <span>&#8592; Tillbaka</span>
                    <span>Dela artikeln</span>
                </div>
                <div class="content-box">
                    <div class="article-text">${{scroll}}</div>
                </div>
                <div class="footer"></div>
            `;
            container.appendChild(scrollDiv);
        }});
    }}
    
    window.addEventListener('load', displayScrolls);
    window.addEventListener('resize', displayScrolls);
    </script>
    
    <div id="scrolls-container"></div>
"""

st.markdown(css_and_js, unsafe_allow_html=True)

if input_text:
    st.markdown(f"""
    <div class="mobile-screen">
        <div class="content-box">
            <div class="article-text">{input_text.replace('\n', '<br>')}</div>
        </div>
    </div>
    <script>
    displayScrolls();
    </script>
    """, unsafe_allow_html=True)
