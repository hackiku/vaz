import streamlit as st

# This is your main app file for the Streamlit multipage app.
# Streamlit will automatically add navigation to the sidebar for each page in the 'pages' folder.

def main():
    st.title('CFD pametnica')

    # Any general instructions or app-wide information can go here.
    st.write("Proracunska na masincu AI-stajl")

if __name__ == "__main__":
    main()

with st.sidebar:
    st.header('CFD time baby')
    st.info('Proracunska na masincu AI-stajl')
