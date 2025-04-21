import os
import numpy as np
import faiss
import streamlit as st
from utils.embedding import embed_text, create_faiss_index, search_similar
from utils.jd_parser import parse_jd
from utils.resume_parser import parse_resume

# --- Streamlit Layout ---
st.title("AI-Powered Resume Parser and JD Matcher")

# Upload files
uploaded_resumes = st.file_uploader("Upload Resumes", type=["pdf", "docx"], accept_multiple_files=True)
jd_file = st.file_uploader("Upload Job Description", type=["pdf", "txt"])

# --- Handle Job Description Embedding ---
jd_embedding = None
if jd_file:
    # Parse and embed JD
    jd_text = parse_jd(jd_file, jd_file.name)
    jd_embedding = embed_text(jd_text)
    st.text_area("📝 Parsed JD Preview", jd_text[:1000], height=200)

# --- Handle Resume Parsing & Embedding ---
resume_embeddings = []
resume_names = []
if uploaded_resumes:
    for resume in uploaded_resumes:
        resume_text = parse_resume(resume, resume.name)
        resume_embedding = embed_text(resume_text)
        resume_embeddings.append(resume_embedding)
        resume_names.append(resume.name)

    # Convert to numpy arrays for FAISS
    resume_embeddings = np.array(resume_embeddings)

    # Create a FAISS index for resumes
    resume_index = create_faiss_index(resume_embeddings)

    # --- Perform Similarity Search ---
    if jd_embedding is not None:
        # Convert JD embedding to numpy array
        jd_embedding_np = np.array([jd_embedding.numpy()])

        # Search for most similar resumes in the FAISS index
        indices, distances = search_similar(jd_embedding_np, resume_index, top_k=5)

        # --- Display Ranking Results ---
        st.subheader("Ranking of Resumes based on JD")
        for i, idx in enumerate(indices[0]):
            st.write(f"Rank {i+1}: {resume_names[idx]} with similarity score {distances[0][i]:.4f}")
