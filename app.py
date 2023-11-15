import streamlit as st

# This is your main app file for the Streamlit multipage app.
# Streamlit will automatically add navigation to the sidebar for each page in the 'pages' folder.

def main():
    st.title('VAZ Aerospace ✈️🛰️')

    # Any general instructions or app-wide information can go here.
    st.write("AI studiranje na Mašincu")

if __name__ == "__main__":
    main()

with st.sidebar:
    st.header('Slajdovi objasnjeni sa AI')
    st.info('Klikci meni za predmete')
