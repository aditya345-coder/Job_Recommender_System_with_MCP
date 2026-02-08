from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import fitz
from core.graph import ResumeGraph, ResumeState

st.set_page_config(page_title="AI Job Intelligence", layout="wide")
st.title("🤖 AI Job Intelligence & Resume Matching System")
st.markdown("Upload your resume to get intelligent job matches with explainable AI.")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

if uploaded_file:
    # The pipeline handles ingestion internally

    with st.spinner("Running intelligence pipeline..."):
        graph = ResumeGraph()
        initial_state = ResumeState(
            uploaded_file=uploaded_file,
            resume_text="",
            skills=[],
            roles=[],
            jobs=[],
            matches=[],
            explanations=[],
            error=None,
        )
        result = graph.invoke(initial_state)

    if result.get("error"):
        st.error(f"Error: {result['error']}")
    else:
        st.markdown("---")
        st.header("🔍 Extracted Skills")
        st.write(", ".join(result.get("skills", [])))

        st.markdown("---")
        st.header("🎯 Inferred Target Roles")
        st.write(", ".join(result.get("roles", [])))

        st.markdown("---")
        st.header("💼 Top Job Matches")

        matches = result.get("matches", [])
        explanations = result.get("explanations", [])

        if matches:
            for i, match in enumerate(matches):
                st.markdown(f"### {match['title']} at {match['company']}")
                st.markdown(f"**Location:** {match['location']}")
                st.markdown(f"**Match Score:** {match['match_score']:.2%}")

                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("**✅ Matched Skills:**")
                    st.write(
                        ", ".join(match["matched_skills"])
                        if match["matched_skills"]
                        else "None"
                    )

                with col2:
                    st.markdown("**❌ Missing Skills:**")
                    st.write(
                        ", ".join(match["missing_skills"])
                        if match["missing_skills"]
                        else "None"
                    )

                if i < len(explanations):
                    st.markdown("**📝 Explanation:**")
                    st.markdown(explanations[i].get("explanation", ""))

                st.markdown("---")
        else:
            st.warning("No matching jobs found.")
