import streamlit as st
import numpy as np
import plotly.express as px
import pandas as pd
from navigation import make_sidebar

# Fungsi untuk menjalankan algoritma THD-Tricluster (simulasi)
def run_thd_tricluster(dataset, d, ming, mins, r):
    # Simulasi hasil tricluster
    # Dalam implementasi sebenarnya, Anda akan menjalankan algoritma THD-Tricluster di sini
    genes = np.random.choice(dataset.shape[0], size=ming, replace=False)
    samples = np.random.choice(dataset.shape[1], size=mins, replace=False)
    times = np.arange(dataset.shape[2])  # Menggunakan semua time points
    
    tricluster = dataset[np.ix_(genes, samples, times)]
    return tricluster, genes, samples, times

# Fungsi untuk memvisualisasikan hasil tricluster
def visualize_tricluster(tricluster):
    fig = px.imshow(tricluster.mean(axis=2),  # Rata-rata sepanjang sumbu waktu
                    title="Tricluster Visualization (Mean Across Time)",
                    labels=dict(x="Samples", y="Genes", color="Expression"))
    return fig

# Fungsi untuk membuat boxplot dari tricluster
def create_tricluster_boxplot(tricluster):
    df_melted = pd.DataFrame(tricluster.reshape(-1, tricluster.shape[2]))
    df_melted['Gene'] = [f'Gene_{i}' for i in range(tricluster.shape[0]) for _ in range(tricluster.shape[1])]
    df_melted['Sample'] = [f'Sample_{i}' for _ in range(tricluster.shape[0]) for i in range(tricluster.shape[1])]
    df_melted = pd.melt(df_melted, id_vars=['Gene', 'Sample'], var_name='Time', value_name='Expression')
    
    fig = px.box(df_melted, x='Gene', y='Expression', color='Sample', 
                 title="Tricluster Boxplot", height=600)
    fig.update_layout(showlegend=False, xaxis_tickangle=-45)
    return fig

# Fungsi utama untuk halaman Triclustering
def main():
    st.set_page_config(page_title="THD-Tricluster Algorithm", page_icon="🧬", layout="wide")
    
    make_sidebar()

    st.title("THD-Tricluster Algorithm")
    st.info("By: Heri Kurnia A.")
    st.write("Welcome to the THD-Tricluster analysis tool.")

    # Input parameters
    st.header("Dataset Parameters")
    col1, col2, col3 = st.columns(3)
    with col1:
        m = st.slider("Number of genes", min_value=10, max_value=1000, value=100)
    with col2:
        n = st.slider("Number of samples", min_value=10, max_value=100, value=50)
    with col3:
        t = st.slider("Number of time points", min_value=2, max_value=20, value=3)

    st.header("Triclustering Parameters")
    col1, col2 = st.columns(2)
    with col1:
        d = st.slider("d parameter", min_value=0.0, max_value=1.0, value=0.8)
        ming = st.number_input("Minimum number of genes", min_value=2, max_value=20, value=5)
    with col2:
        mins = st.number_input("Minimum number of samples", min_value=2, max_value=20, value=3)
        r = st.slider("r parameter", min_value=0.0, max_value=1.0, value=0.7)

    if st.button("Generate Data and Run Triclustering"):
        # Generate random dataset
        dataset = np.random.randint(1, 201, size=(m, n, t))
        st.write("Dataset shape:", dataset.shape)
        
        # Run THD-Tricluster algorithm
        tricluster, genes, samples, times = run_thd_tricluster(dataset, d, ming, mins, r)
        st.write("Tricluster shape:", tricluster.shape)
        
        # Visualize the tricluster
        st.subheader("Tricluster Visualization")
        fig = visualize_tricluster(tricluster)
        st.plotly_chart(fig)
        
        # Create and display tricluster boxplot
        st.subheader("Tricluster Boxplot")
        fig_boxplot = create_tricluster_boxplot(tricluster)
        st.plotly_chart(fig_boxplot)
        
        # Display tricluster information
        st.subheader("Tricluster Information")
        st.write(f"Selected Genes: {genes}")
        st.write(f"Selected Samples: {samples}")
        st.write(f"Time Points: {times}")

    st.info("Adjust the parameters and click 'Generate Data and Run Triclustering' to execute the algorithm.")

if __name__ == "__main__":
    main()
