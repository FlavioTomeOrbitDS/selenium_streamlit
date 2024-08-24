import streamlit as st


st.set_page_config(layout="wide")

def page1():
    st.title("Sales IA Bot Assistants")

    # Using "with" notation
    with st.sidebar:
        st.header("Conversas")
        add_radio = st.radio(
            "Choose a shipping method",
            ("Standard (5-15 days)", "Express (2-5 days)")
        )
    

    

    
pg = st.navigation([
    st.Page(page1, title="Home", icon=":material/home:"),
    st.Page("qrcode.py", title="Gerar QR Code", icon=":material/qr_code:"),
])
pg.run()        


