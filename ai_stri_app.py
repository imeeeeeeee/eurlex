import streamlit as st
import pandas as pd

st.title("Changes in the EU Legal Database")

# Fichiers
file_1_path = "changes.csv"
file_2_path = "filtered_celex_data_cleaned.csv"
file_3_path = "filtered_celex_dir_data.csv"
#file_4_path = "newsect_changes.csv"

# Options de sélection
st.sidebar.header("Show files")
show_file_1 = st.sidebar.checkbox("Show changes", value=True)
show_file_2 = st.sidebar.checkbox("Show new regulations", value=True)
show_file_3 = st.sidebar.checkbox("Show new directives", value=True)
show_file_4 = st.sidebar.checkbox("Show new sector changes", value=False)

# Affichage dans des colonnes si les deux sont cochés
# Determine which files are selected
selected_files = [show_file_1, show_file_2, show_file_3, show_file_4]
num_selected = sum(selected_files)

if num_selected == 0:
    col1 = col2 = col3 = col4 = st.container()
elif num_selected == 1:
    col1 = st.container()
    col2 = col3 = col4 = col1
elif num_selected == 2:
    col1, col2 = st.columns(2)
    col3 = col4 = st.container()
elif num_selected == 3:
    col1, col2, col3 = st.columns(3)
    col4 = st.container()
else:
    col1, col2, col3, col4 = st.columns(4)

# Affichage du premier fichier
with col1:
    if show_file_1:
        st.subheader("Changes")
        try:
            df = pd.read_csv(file_1_path)
            st.dataframe(
                df.style.set_properties(**{
                    'background-color': '#f9f9f9',
                    'color': '#222',
                    'border-color': '#ccc',
                    'font-size': '16px'
                }).set_table_styles([
                    {'selector': 'th', 'props': [('background-color', '#e3e3e3'), ('color', '#222'), ('font-size', '17px')]}
                ]),
                width=900,
                height=500
            )
        except Exception as e:
            st.error(f"Erreur lors du chargement de changes.csv : {e}")

# Affichage du deuxième fichier
with col2:
    if show_file_2:
        st.subheader("New data")
        try:
            df2 = pd.read_csv(file_2_path)
            st.dataframe(
                df2.style.set_properties(**{
                    'background-color': '#f9f9f9',
                    'color': '#222',
                    'border-color': '#ccc',
                    'font-size': '16px'
                }).set_table_styles([
                    {'selector': 'th', 'props': [('background-color', '#e3e3e3'), ('color', '#222'), ('font-size', '17px')]}
                ]),
                width=900,
                height=500
            )
        except Exception as e:
            st.error(f"Erreur lors du chargement de filtered_celex_data_cleaned.csv : {e}")

# Affichage du troisième fichier
with col3:
    if show_file_3:
        st.subheader("New directives")
        try:
            df3 = pd.read_csv(file_3_path)
            st.dataframe(
                df3.style.set_properties(**{
                    'background-color': '#f9f9f9',
                    'color': '#222',
                    'border-color': '#ccc',
                    'font-size': '16px'
                }).set_table_styles([
                    {'selector': 'th', 'props': [('background-color', '#e3e3e3'), ('color', '#222'), ('font-size', '17px')]}
                ]),
                width=900,
                height=500
            )
        except Exception as e:
            st.error(f"Erreur lors du chargement de filtered_celex_dir_data.csv : {e}")

# Affichage du quatrième fichier
with col4:
    if show_file_4:
        st.subheader("New sector changes")
        try:
            # df4 = pd.read_csv(file_4_path)
            # st.dataframe(
            #     df4.style.set_properties(**{
            #         'background-color': '#f9f9f9',
            #         'color': '#222',
            #         'border-color': '#ccc',
            #         'font-size': '16px'
            #     }).set_table_styles([
            #         {'selector': 'th', 'props': [('background-color', '#e3e3e3'), ('color', '#222'), ('font-size', '17px')]}
            #     ]),
            #     width=900,
            #     height=500
            # )
            st.write("This file is not available yet.")
        except Exception as e:
            st.error(f"Erreur lors du chargement de newsect_changes.csv : {e}")
