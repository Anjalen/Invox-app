import streamlit as st
import openai

# Define the prompt directly here (skip importing from another file for now)
scam_analysis_prompt = """
You are a cybersecurity assistant designed to detect email scams, phishing, and psychological manipulation.

When a user submits an email, analyze it for:
- Scam indicators (e.g., urgency, impersonation, threats)
- Manipulative language (fear, flattery, reward)
- Requests for personal information
- Red flags like poor grammar, spoofed links, false authority

Return your analysis in this format:

Scam Risk: [Low | Medium | High]

Red Flags:
- [Bullet point list of detected tactics]

Summary:
A clear explanation of why this message may or may not be dangerous.

Recommendations:
- What should the user do next?
"""

# Set your OpenAI API key here
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

# Streamlit UI
st.set_page_config(page_title="Invox - Scam Analyzer", layout="centered")
st.title("📨 Invox — Email Scam Analyzer")
st.caption("Paste any suspicious email below and get an instant AI-powered threat analysis.")

user_input = st.text_area("Email Content", height=300)

if st.button("Analyze"):
    if not user_input.strip():
        st.warning("Please paste some content before analyzing.")
    else:
        with st.spinner("Analyzing the email for scam signals..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": scam_analysis_prompt},
                        {"role": "user", "content": user_input}
                    ],
                    temperature=0.4
                )
                result = response.choices[0].message.content
                st.success("✅ Analysis Complete!")
                st.markdown(result)
            except Exception as e:
                st.error(f"Something went wrong: {e}")
