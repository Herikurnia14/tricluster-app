import streamlit as st
import numpy as np
import plotly.express as px
import pandas as pd
from typing import List, Set, Tuple

# Definisi kelas THDTricluster
class THDTricluster:
    def __init__(self, dataset, d, ming, mins, r):
        self.dataset = dataset
        self.d = d
        self.ming = ming
        self.mins = mins
        self.r = r
        self.m, self.n, self.t = dataset.shape
        self.Bt = set()
        self.Tc = set()

    def generate_biclusters(self):
        # Implementasi sederhana untuk contoh
        self.Bt = {frozenset([(i, j) for i in range(self.m) for j in range(self.n)])}

    def generate_triclusters(self):
        # Implementasi sederhana untuk contoh
        self.Tc = {frozenset([(i, j, k) for i in range(self.m) for j in range(self.n) for k in range(self.t)])}

    def compute_mS(self, col1, col2):
        # Implementasi sederhana
        return np.mean(np.abs(col1 - col2))

# Fungsi untuk membuat visualisasi sederhana menggunakan Plotly
def visualize_tricluster(dataset, tricluster):
    fig = px.imshow(dataset[:, :, 0], 
                    title="Tricluster Visualization (First Time Point)",
                    labels=dict(x="Samples", y="Genes", color="Expression"))
    return fig

# Fungsi untuk membuat boxplot untuk tiap sampel
def create_sample_boxplot(dataset):
    df_melted = pd.melt(pd.DataFrame(dataset.reshape(-1, dataset.shape[1])), 
                        var_name='Sample', value_name='Expression')
    fig = px.box(df_melted, x='Sample', y='Expression', 
                 title="Distribution of Gene Expression Across Samples")
    return fig

# Fungsi untuk membuat distribusi ekspresi gen
def create_gene_expression_distribution(dataset):
    df_melted = pd.melt(pd.DataFrame(dataset.reshape(-1, dataset.shape[0])).T, 
                        var_name='Gene', value_name='Expression')
    fig = px.histogram(df_melted, x='Expression', 
                       title="Distribution of Gene Expression",
                       marginal="box")
    return fig

# Aplikasi Streamlit
st.title("Triclustering Application")
st.subheader("Magister of Mathematics - Universitas Indonesia")

# Input parameters
st.sidebar.header("Dataset Parameters")
m = st.sidebar.slider("Number of genes", min_value=10, max_value=1000, value=100)
n = st.sidebar.slider("Number of samples", min_value=10, max_value=100, value=50)
t = st.sidebar.slider("Number of time points", min_value=2, max_value=20, value=3)

st.sidebar.header("Triclustering Parameters")
d = st.sidebar.slider("d parameter", min_value=0.0, max_value=1.0, value=0.8)
ming = st.sidebar.number_input("Minimum number of genes", min_value=2, max_value=20, value=5)
mins = st.sidebar.number_input("Minimum number of samples", min_value=2, max_value=20, value=3)
r = st.sidebar.slider("r parameter", min_value=0.0, max_value=1.0, value=0.7)

if st.sidebar.button("Generate Data and Run Triclustering"):
    # Generate random dataset
    dataset = np.random.randint(1, 201, size=(m, n, t))
    st.write("Dataset shape:", dataset.shape)
    
    # Run triclustering
    thd_tricluster = THDTricluster(dataset, d=d, ming=ming, mins=mins, r=r)
    thd_tricluster.generate_biclusters()
    thd_tricluster.generate_triclusters()
    
    # Display results
    st.write(f"Number of biclusters found: {len(thd_tricluster.Bt)}")
    st.write(f"Number of triclusters found: {len(thd_tricluster.Tc)}")
    
    # Display first tricluster (if any)
    if thd_tricluster.Tc:
        first_tricluster = list(thd_tricluster.Tc)[0]
        st.write("First Tricluster:")
        st.write(f"Number of elements: {len(first_tricluster)}")
        
        # Visualize the first tricluster
        fig = visualize_tricluster(dataset, first_tricluster)
        st.plotly_chart(fig)
        
        # EDA: Boxplot for each Sample
        st.subheader("Boxplot for Each Sample")
        fig_boxplot = create_sample_boxplot(dataset)
        st.plotly_chart(fig_boxplot)
        
        # EDA: Distribution of Gene Expression
        st.subheader("Distribution of Gene Expression")
        fig_dist = create_gene_expression_distribution(dataset)
        st.plotly_chart(fig_dist)
    else:
        st.write("No triclusters found.")

st.sidebar.info("Adjust the parameters and click 'Generate Data and Run Triclustering' to execute the algorithm.")