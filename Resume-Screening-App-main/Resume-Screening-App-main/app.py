# import streamlit as st
# import pickle
# import re
# import nltk
#
# nltk.download('punkt')
# nltk.download('stopwords')
#
# #loading modelss
# clf = pickle.load(open('clf.pkl','rb'))
# tfidf = pickle.load(open('tfidf.pkl','rb'))
#
# def clean_resume(resume_text):
#     clean_text = re.sub('http\S+\s*', ' ', resume_text)
#     clean_text = re.sub('RT|cc', ' ', clean_text)
#     clean_text = re.sub('#\S+', '', clean_text)
#     clean_text = re.sub('@\S+', '  ', clean_text)
#     clean_text = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', clean_text)
#     clean_text = re.sub(r'[^\x00-\x7f]', r' ', clean_text)
#     clean_text = re.sub('\s+', ' ', clean_text)
#     return clean_text
# # web app
# def main():
#     st.title("Resume Screening App")
#     uploaded_file = st.file_uploader('Upload Resume', type=['txt','pdf'])
#
#     if uploaded_file is not None:
#         try:
#             resume_bytes = uploaded_file.read()
#             resume_text = resume_bytes.decode('utf-8')
#         except UnicodeDecodeError:
#             # If UTF-8 decoding fails, try decoding with 'latin-1'
#             resume_text = resume_bytes.decode('latin-1')
#
#         cleaned_resume = clean_resume(resume_text)
#         input_features = tfidf.transform([cleaned_resume])
#         prediction_id = clf.predict(input_features)[0]
#         st.write(prediction_id)
#
#         # Map category ID to category name
#         category_mapping = {
#             15: "Java Developer",
#             23: "Testing",
#             8: "DevOps Engineer",
#             20: "Python Developer",
#             24: "Web Designing",
#             12: "HR",
#             13: "Hadoop",
#             3: "Blockchain",
#             10: "ETL Developer",
#             18: "Operations Manager",
#             6: "Data Science",
#             22: "Sales",
#             16: "Mechanical Engineer",
#             1: "Arts",
#             7: "Database",
#             11: "Electrical Engineering",
#             14: "Health and fitness",
#             19: "PMO",
#             4: "Business Analyst",
#             9: "DotNet Developer",
#             2: "Automation Testing",
#             17: "Network Security Engineer",
#             21: "SAP Developer",
#             5: "Civil Engineer",
#             0: "Advocate",
#         }
#
#         category_name = category_mapping.get(prediction_id, "Unknown")
#
#         st.write("Predicted Category:", category_name)
#
#
#
# # python main
# if __name__ == "__main__":
#     main()

# import streamlit as st
# import pickle
# import re
# import nltk
# import pandas as pd
# import matplotlib.pyplot as plt
# from wordcloud import WordCloud
# 
# nltk.download('punkt')
# nltk.download('stopwords')
# 
# # Load models
# clf = pickle.load(open('clf.pkl', 'rb'))
# tfidf = pickle.load(open('tfidf.pkl', 'rb'))
# 
# 
# # Clean resume function
# def clean_resume(resume_text):
#     clean_text = re.sub('http\S+\s*', ' ', resume_text)
#     clean_text = re.sub('RT|cc', ' ', clean_text)
#     clean_text = re.sub('#\S+', '', clean_text)
#     clean_text = re.sub('@\S+', '  ', clean_text)
#     clean_text = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', clean_text)
#     clean_text = re.sub(r'[^\x00-\x7f]', r' ', clean_text)
#     clean_text = re.sub('\s+', ' ', clean_text)
#     clean_text = clean_text.lower()
#     return clean_text
# 
# 
# # Display word cloud
# def generate_wordcloud(text):
#     wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
#     plt.figure(figsize=(10, 5))
#     plt.imshow(wordcloud, interpolation='bilinear')
#     plt.axis('off')
#     st.pyplot(plt)
# 
# 
# # Web app
# def main():
#     # Page layout
#     st.set_page_config(page_title="Resume Screening App", page_icon="📝", layout="wide")
# 
#     # Custom CSS styling
#     st.markdown("""
#         <style>
#         .main {
#             background-color: #f9f9f9;
#             color: #333333;
#             padding: 20px;
#         }
#         h1 {
#             color: #007BFF;
#             font-family: 'Arial Black', Gadget, sans-serif;
#         }
#         .stButton>button {
#             background-color: #28a745;
#             border-radius: 10px;
#             color: white;
#         }
#         .stFileUploader label {
#             font-size: 18px;
#         }
#         .stSidebar {
#             background-color: #343a40;
#             color: white;
#         }
#         .success-message {
#             color: green;
#             font-weight: bold;
#         }
#         </style>
#     """, unsafe_allow_html=True)
# 
#     # Sidebar with navigation options
#     st.sidebar.title("📄 Resume Screening App")
#     st.sidebar.markdown("An intelligent app to categorize and analyze resumes based on job roles.")
# 
#     # Add sidebar options for additional features (with unique keys)
#     st.sidebar.subheader("Features")
#     show_wordcloud = st.sidebar.checkbox("Show Resume Word Cloud", key='wordcloud_checkbox')
#     compare_template = st.sidebar.checkbox("Compare Resume to Ideal Job Template", key='compare_checkbox')
#     analyze_skills = st.sidebar.checkbox("Analyze Skills in Resume", key='analyze_checkbox')
# 
#     # Main app section with tabs
#     tab1, tab2 = st.tabs(["🔍 Resume Screening", "📊 Resume Analysis"])
# 
#     with tab1:
#         st.title("Resume Screening 📝")
#         uploaded_file = st.file_uploader('Upload your resume here (txt or pdf)', type=['txt', 'pdf'])
# 
#         if uploaded_file is not None:
#             # Custom success message with styling
#             st.markdown('<p class="success-message">Resume uploaded successfully!</p>', unsafe_allow_html=True)
# 
#             # Try reading the uploaded file
#             try:
#                 resume_bytes = uploaded_file.read()
#                 resume_text = resume_bytes.decode('utf-8')
#             except UnicodeDecodeError:
#                 resume_text = resume_bytes.decode('latin-1')
# 
#             # Process the uploaded resume
#             with st.spinner("Analyzing Resume..."):
#                 cleaned_resume = clean_resume(resume_text)
#                 input_features = tfidf.transform([cleaned_resume])
#                 prediction_id = clf.predict(input_features)[0]
# 
#             # Mapping predicted category ID to category name
#             category_mapping = {
#                 15: "Java Developer",
#                 23: "Testing",
#                 8: "DevOps Engineer",
#                 20: "Python Developer",
#                 24: "Web Designing",
#                 12: "HR",
#                 13: "Hadoop",
#                 3: "Blockchain",
#                 10: "ETL Developer",
#                 18: "Operations Manager",
#                 6: "Data Science",
#                 22: "Sales",
#                 16: "Mechanical Engineer",
#                 1: "Arts",
#                 7: "Database",
#                 11: "Electrical Engineering",
#                 14: "Health and Fitness",
#                 19: "PMO",
#                 4: "Business Analyst",
#                 9: "DotNet Developer",
#                 2: "Automation Testing",
#                 17: "Network Security Engineer",
#                 21: "SAP Developer",
#                 5: "Civil Engineer",
#                 0: "Advocate",
#             }
# 
#             category_name = category_mapping.get(prediction_id, "Unknown")
#             st.subheader(f"🎯 Predicted Job Category: **{category_name}**")
# 
#             # Display Word Cloud if selected
#             if show_wordcloud:
#                 st.subheader("Word Cloud of Resume")
#                 generate_wordcloud(resume_text)
# 
#             # Download option for the cleaned resume
#             st.download_button("Download Cleaned Resume", data=cleaned_resume, file_name="cleaned_resume.txt")
# 
#     with tab2:
#         st.title("Resume Skills Analysis 📊")
#         st.markdown("Analyze the skills in your resume and compare them to the ideal job role.")
# 
#         if uploaded_file is not None:
#             st.subheader("Skills Analysis")
#             st.write("Key Skills found in your resume:")
#             # Display some mock skills for demo
#             st.write("- Python")
#             st.write("- Machine Learning")
#             st.write("- Data Science")
#             st.write("- Web Development")
# 
#             # Visualizing skills match with a pie chart
#             skills_match = pd.DataFrame({
#                 'Skills': ['Python', 'Machine Learning', 'Data Science', 'Web Development'],
#                 'Proficiency': [80, 70, 90, 60]
#             })
# 
#             fig, ax = plt.subplots()
#             ax.pie(skills_match['Proficiency'], labels=skills_match['Skills'], autopct='%1.1f%%', startangle=90)
#             st.pyplot(fig)
# 
# 
# # Run the app
# if __name__ == "__main__":
#     main()
# 

# import streamlit as st
# import pickle
# import re
# import nltk
# import matplotlib.pyplot as plt
# from wordcloud import WordCloud
# from PIL import Image
# import io
#
# nltk.download('punkt')
# nltk.download('stopwords')
#
# # Load models
# clf = pickle.load(open('clf.pkl', 'rb'))
# tfidf = pickle.load(open('tfidf.pkl', 'rb'))
#
# # Function to clean resume text
# def clean_resume(resume_text):
#     clean_text = re.sub('http\S+\s*', ' ', resume_text)
#     clean_text = re.sub('RT|cc', ' ', clean_text)
#     clean_text = re.sub('#\S+', '', clean_text)
#     clean_text = re.sub('@\S+', '  ', clean_text)
#     clean_text = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', clean_text)
#     clean_text = re.sub(r'[^\x00-\x7f]', r' ', clean_text)
#     clean_text = re.sub('\s+', ' ', clean_text)
#     return clean_text
#
# # Function to generate a word cloud
# def generate_wordcloud(text):
#     wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
#     return wordcloud
#
# # Web app
# def main():
#     # Apply CSS styling for the app
#     st.markdown("""
#         <style>
#         .reportview-container {
#             background: #f5f5f5;
#         }
#         .sidebar .sidebar-content {
#             background: #f0f0f0;
#         }
#         .stFileUploader {
#             font-size: 18px;
#         }
#         .stButton>button {
#             background-color: #4CAF50;
#             color: white;
#             font-size: 18px;
#         }
#         </style>
#         """, unsafe_allow_html=True)
#
#     st.title("💼 Resume Screening App")
#     st.write("Upload your resume and let the AI predict the job category!")
#
#     uploaded_file = st.file_uploader('Upload Resume (TXT or PDF format)', type=['txt', 'pdf'])
#
#     if uploaded_file is not None:
#         try:
#             resume_bytes = uploaded_file.read()
#             resume_text = resume_bytes.decode('utf-8')
#         except UnicodeDecodeError:
#             resume_text = resume_bytes.decode('latin-1')
#
#         cleaned_resume = clean_resume(resume_text)
#
#         st.success('Resume uploaded successfully!')
#
#         # Generate Word Cloud
#         if st.sidebar.checkbox("Show Resume Word Cloud", key="wordcloud"):
#             st.subheader("Resume Word Cloud")
#             wordcloud = generate_wordcloud(cleaned_resume)
#             plt.imshow(wordcloud, interpolation='bilinear')
#             plt.axis('off')
#             st.pyplot()
#
#         # Make predictions
#         input_features = tfidf.transform([cleaned_resume])
#         prediction_id = clf.predict(input_features)[0]
#
#         # Map prediction to job category
#         category_mapping = {
#             15: "Java Developer",
#             23: "Testing",
#             8: "DevOps Engineer",
#             20: "Python Developer",
#             24: "Web Designing",
#             12: "HR",
#             13: "Hadoop",
#             3: "Blockchain",
#             10: "ETL Developer",
#             18: "Operations Manager",
#             6: "Data Science",
#             22: "Sales",
#             16: "Mechanical Engineer",
#             1: "Arts",
#             7: "Database",
#             11: "Electrical Engineering",
#             14: "Health and Fitness",
#             19: "PMO",
#             4: "Business Analyst",
#             9: "DotNet Developer",
#             2: "Automation Testing",
#             17: "Network Security Engineer",
#             21: "SAP Developer",
#             5: "Civil Engineer",
#             0: "Advocate",
#         }
#
#         category_name = category_mapping.get(prediction_id, "Unknown")
#
#         # Display prediction result with custom styling
#         st.markdown(f'<h3 style="color:black;"><strong>🎯 Predicted Job Category: {category_name}</strong></h3>', unsafe_allow_html=True)
#
#         # Option to download the cleaned resume
#         if st.sidebar.checkbox("Download Cleaned Resume", key="download_resume"):
#             cleaned_resume_bytes = io.BytesIO()
#             cleaned_resume_bytes.write(cleaned_resume.encode())
#             cleaned_resume_bytes.seek(0)
#             st.sidebar.download_button(label="Download Cleaned Resume", data=cleaned_resume_bytes, file_name="cleaned_resume.txt")
#
# # Run the app
# if __name__ == "__main__":
#     main()
#

# import streamlit as st
# import pickle
# import re
# import nltk
# from wordcloud import WordCloud
# import matplotlib.pyplot as plt
# from PIL import Image
# import io
#
# nltk.download('punkt')
# nltk.download('stopwords')
#
# # Load models
# clf = pickle.load(open('clf.pkl', 'rb'))
# tfidf = pickle.load(open('tfidf.pkl', 'rb'))
#
# # Function to clean resume text
# def clean_resume(resume_text):
#     clean_text = re.sub('http\S+\s*', ' ', resume_text)
#     clean_text = re.sub('RT|cc', ' ', clean_text)
#     clean_text = re.sub('#\S+', '', clean_text)
#     clean_text = re.sub('@\S+', '  ', clean_text)
#     clean_text = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', clean_text)
#     clean_text = re.sub(r'[^\x00-\x7f]', r' ', clean_text)
#     clean_text = re.sub('\s+', ' ', clean_text)
#     return clean_text
#
# # Function to generate a word cloud
# def generate_wordcloud(text):
#     wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
#     return wordcloud
#
# # Web app
# def main():
#     # Apply CSS styling for the app
#     st.markdown("""
#         <style>
#         body {
#             background-color: #f5f5f5;
#             font-family: 'Arial', sans-serif;
#         }
#         .main-header {
#             text-align: center;
#             color: #2c3e50;
#             font-size: 36px;
#             font-weight: bold;
#             margin-bottom: 20px;
#         }
#         .app-description {
#             text-align: center;
#             color: #7f8c8d;
#             font-size: 18px;
#             margin-bottom: 40px;
#         }
#         .upload-section {
#             background-color: #ffffff;
#             padding: 20px;
#             border-radius: 10px;
#             box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.1);
#             margin-bottom: 30px;
#         }
#         .stButton>button {
#             background-color: #2980b9;
#             color: white;
#             font-size: 18px;
#             border-radius: 8px;
#             padding: 10px 24px;
#         }
#         .prediction-text {
#             color: #27ae60;
#             font-size: 22px;
#             font-weight: bold;
#         }
#         .stSuccess {
#             color: green;
#             font-size: 20px;
#             font-weight: bold;
#         }
#         </style>
#         """, unsafe_allow_html=True)
#
#     # App title and description
#     st.markdown('<div class="main-header">💼 Resume Screening App</div>', unsafe_allow_html=True)
#     st.markdown('<div class="app-description">Upload your resume and know the best matching job category for you.</div>', unsafe_allow_html=True)
#
#     uploaded_file = st.file_uploader('Upload Resume (TXT or PDF format)', type=['txt', 'pdf'])
#
#     if uploaded_file is not None:
#         try:
#             resume_bytes = uploaded_file.read()
#             resume_text = resume_bytes.decode('utf-8')
#         except UnicodeDecodeError:
#             resume_text = resume_bytes.decode('latin-1')
#
#         cleaned_resume = clean_resume(resume_text)
#
#         st.markdown('<p class="stSuccess">Resume uploaded successfully!</p>', unsafe_allow_html=True)
#
#         # Generate Word Cloud
#         if st.sidebar.checkbox("Show Resume Word Cloud", key="wordcloud"):
#             st.subheader("Resume Word Cloud")
#             wordcloud = generate_wordcloud(cleaned_resume)
#             plt.imshow(wordcloud, interpolation='bilinear')
#             plt.axis('off')
#             st.pyplot()
#
#         # Make predictions
#         input_features = tfidf.transform([cleaned_resume])
#         prediction_id = clf.predict(input_features)[0]
#
#         # Map prediction to job category
#         category_mapping = {
#             15: "Java Developer",
#             23: "Testing",
#             8: "DevOps Engineer",
#             20: "Python Developer",
#             24: "Web Designing",
#             12: "HR",
#             13: "Hadoop",
#             3: "Blockchain",
#             10: "ETL Developer",
#             18: "Operations Manager",
#             6: "Data Science",
#             22: "Sales",
#             16: "Mechanical Engineer",
#             1: "Arts",
#             7: "Database",
#             11: "Electrical Engineering",
#             14: "Health and Fitness",
#             19: "PMO",
#             4: "Business Analyst",
#             9: "DotNet Developer",
#             2: "Automation Testing",
#             17: "Network Security Engineer",
#             21: "SAP Developer",
#             5: "Civil Engineer",
#             0: "Advocate",
#         }
#
#         category_name = category_mapping.get(prediction_id, "Unknown")
#
#         # Display prediction result with custom styling
#         st.markdown(f'<p class="prediction-text">🎯 Predicted Job Category: <strong>{category_name}</strong></p>', unsafe_allow_html=True)
#
#         # Option to download the cleaned resume
#         if st.sidebar.checkbox("Download Cleaned Resume", key="download_resume"):
#             cleaned_resume_bytes = io.BytesIO()
#             cleaned_resume_bytes.write(cleaned_resume.encode())
#             cleaned_resume_bytes.seek(0)
#             st.sidebar.download_button(label="Download Cleaned Resume", data=cleaned_resume_bytes, file_name="cleaned_resume.txt")
#
# # Run the app
# if __name__ == "__main__":
#     main()

# import streamlit as st
# import pickle
# import re
# import nltk
# import pandas as pd
# import matplotlib.pyplot as plt
# from wordcloud import WordCloud
#
# nltk.download('punkt')
# nltk.download('stopwords')
#
# # Load models
# clf = pickle.load(open('clf.pkl', 'rb'))
# tfidf = pickle.load(open('tfidf.pkl', 'rb'))
#
# # Clean resume function
# def clean_resume(resume_text):
#     clean_text = re.sub('http\S+\s*', ' ', resume_text)
#     clean_text = re.sub('RT|cc', ' ', clean_text)
#     clean_text = re.sub('#\S+', '', clean_text)
#     clean_text = re.sub('@\S+', '  ', clean_text)
#     clean_text = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', clean_text)
#     clean_text = re.sub(r'[^\x00-\x7f]', r' ', clean_text)
#     clean_text = re.sub('\s+', ' ', clean_text)
#     clean_text = clean_text.lower()
#     return clean_text
#
# # Display word cloud
# def generate_wordcloud(text):
#     wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
#     plt.figure(figsize=(10, 5))
#     plt.imshow(wordcloud, interpolation='bilinear')
#     plt.axis('off')
#     st.pyplot(plt)
#
# # Web app
# def main():
#     # Page layout
#     st.set_page_config(page_title="Resume Screening App", page_icon="📝", layout="wide")
#
#     # Custom CSS styling
#     st.markdown("""
#         <style>
#         .main {
#             background-color: #f9f9f9;
#             color: #333333;
#             padding: 20px;
#         }
#         h1 {
#             color: #007BFF;
#             font-family: 'Arial Black', Gadget, sans-serif;
#         }
#         .stButton>button {
#             background-color: #28a745;
#             border-radius: 10px;
#             color: white;
#         }
#         .stFileUploader label {
#             font-size: 18px;
#         }
#         .stSidebar {
#             background-color: #343a40;
#             color: white;
#         }
#         .success-message {
#             color: green;
#             font-weight: bold;
#         }
#         .prediction {
#             color: black;
#             font-weight: bold;
#         }
#         .description {
#             font-family: 'Verdana', sans-serif;
#             font-size: 16px;
#             color: #444;
#             margin-bottom: 20px;
#         }
#         </style>
#     """, unsafe_allow_html=True)
#
#     # Description section
#     st.markdown("<div class='description'>Welcome to the Resume Screening App! This intelligent app helps you analyze and categorize resumes into various job roles based on the content of the resume. Upload your resume and let the app predict the most suitable job category for you. It also provides additional analysis tools like word cloud and skill match analysis.</div>", unsafe_allow_html=True)
#
#     # Sidebar with navigation options
#     st.sidebar.title("📄 Resume Screening App")
#     st.sidebar.markdown("An intelligent app to categorize and analyze resumes based on job roles.")
#
#     # Add sidebar options for additional features (with unique keys)
#     st.sidebar.subheader("Features")
#     show_wordcloud = st.sidebar.checkbox("Show Resume Word Cloud", key='wordcloud_checkbox')
#     compare_template = st.sidebar.checkbox("Compare Resume to Ideal Job Template", key='compare_checkbox')
#     analyze_skills = st.sidebar.checkbox("Analyze Skills in Resume", key='analyze_checkbox')
#
#     # Main app section with tabs
#     tab1, tab2 = st.tabs(["🔍 Resume Screening", "📊 Resume Analysis"])
#
#     with tab1:
#         st.title("Resume Screening 📝")
#         uploaded_file = st.file_uploader('Upload your resume here (txt or pdf)', type=['txt', 'pdf'])
#
#         if uploaded_file is not None:
#             # Custom success message with styling
#             st.markdown('<p class="success-message">Resume uploaded successfully!</p>', unsafe_allow_html=True)
#
#             # Try reading the uploaded file
#             try:
#                 resume_bytes = uploaded_file.read()
#                 resume_text = resume_bytes.decode('utf-8')
#             except UnicodeDecodeError:
#                 resume_text = resume_bytes.decode('latin-1')
#
#             # Process the uploaded resume
#             with st.spinner("Analyzing Resume..."):
#                 cleaned_resume = clean_resume(resume_text)
#                 input_features = tfidf.transform([cleaned_resume])
#                 prediction_id = clf.predict(input_features)[0]
#
#             # Mapping predicted category ID to category name
#             category_mapping = {
#                 15: "Java Developer",
#                 23: "Testing",
#                 8: "DevOps Engineer",
#                 20: "Python Developer",
#                 24: "Web Designing",
#                 12: "HR",
#                 13: "Hadoop",
#                 3: "Blockchain",
#                 10: "ETL Developer",
#                 18: "Operations Manager",
#                 6: "Data Science",
#                 22: "Sales",
#                 16: "Mechanical Engineer",
#                 1: "Arts",
#                 7: "Database",
#                 11: "Electrical Engineering",
#                 14: "Health and Fitness",
#                 19: "PMO",
#                 4: "Business Analyst",
#                 9: "DotNet Developer",
#                 2: "Automation Testing",
#                 17: "Network Security Engineer",
#                 21: "SAP Developer",
#                 5: "Civil Engineer",
#                 0: "Advocate",
#             }
#
#             category_name = category_mapping.get(prediction_id, "Unknown")
#             st.markdown(f"<h3>🎯 Predicted Job Category: <span class='prediction'>{category_name}</span></h3>", unsafe_allow_html=True)
#
#             # Display Word Cloud if selected
#             if show_wordcloud:
#                 st.subheader("Word Cloud of Resume")
#                 generate_wordcloud(resume_text)
#
#             # Download option for the cleaned resume
#             st.download_button("Download Cleaned Resume", data=cleaned_resume, file_name="cleaned_resume.txt")
#
#     with tab2:
#         st.title("Resume Skills Analysis 📊")
#         st.markdown("Analyze the skills in your resume and compare them to the ideal job role.")
#
#         if uploaded_file is not None:
#             st.subheader("Skills Analysis")
#             st.write("Key Skills found in your resume:")
#             # Display some mock skills for demo
#             st.write("- Python")
#             st.write("- Machine Learning")
#             st.write("- Data Science")
#             st.write("- Web Development")
#
#             # Visualizing skills match with a pie chart
#             skills_match = pd.DataFrame({
#                 'Skills': ['Python', 'Machine Learning', 'Data Science', 'Web Development'],
#                 'Proficiency': [80, 70, 90, 60]
#             })
#
#             fig, ax = plt.subplots()
#             ax.pie(skills_match['Proficiency'], labels=skills_match['Skills'], autopct='%1.1f%%', startangle=90)
#             st.pyplot(fig)
#
# # Run the app
# if __name__ == "__main__":
#     main()

import streamlit as st
import pickle
import re
import nltk
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

nltk.download('punkt')
nltk.download('stopwords')

# Load models
clf = pickle.load(open('clf.pkl', 'rb'))
tfidf = pickle.load(open('tfidf.pkl', 'rb'))

# Clean resume function
def clean_resume(resume_text):
    clean_text = re.sub('http\S+\s*', ' ', resume_text)
    clean_text = re.sub('RT|cc', ' ', clean_text)
    clean_text = re.sub('#\S+', '', clean_text)
    clean_text = re.sub('@\S+', '  ', clean_text)
    clean_text = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', clean_text)
    clean_text = re.sub(r'[^\x00-\x7f]', r' ', clean_text)
    clean_text = re.sub('\s+', ' ', clean_text)
    clean_text = clean_text.lower()
    return clean_text

# Display word cloud
def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)

# Web app
def main():
    # Page layout
    st.set_page_config(page_title="Resume Screening App", page_icon="📝", layout="wide")

    # Custom CSS styling
    st.markdown("""
        <style>
        .main {
            background-color: #f9f9f9;
            color: #333333;
            padding: 20px;
        }
        h1 {
            color: #007BFF;
            font-family: 'Arial Black', Gadget, sans-serif;
        }
        .stButton>button {
            background-color: #28a745;
            border-radius: 10px;
            color: white;
        }
        .stFileUploader label {
            font-size: 18px;
        }
        .stSidebar {
            background-color: #343a40;
            color: white;
        }
        .success-message {
            color: green;
            font-weight: bold;
        }c
        .prediction {
            color: black;
            font-weight: bold;
        }
        .description {
            font-family: 'Verdana', sans-serif;
            font-size: 16px;
            color: #444;
            margin-bottom: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Description section
    st.markdown("<div class='description'>Welcome to the Resume Screening App! This intelligent app helps you analyze and categorize resumes into various job roles based on the content of the resume. Upload your resume and let the app predict the most suitable job category for you. It also provides additional analysis tools like word cloud and skill match analysis.</div>", unsafe_allow_html=True)

    # Sidebar with navigation options
    st.sidebar.title("📄 Resume Screening App")
    st.sidebar.markdown("An intelligent app to categorize and analyze resumes based on job roles.")

    # Add sidebar options for additional features (with unique keys)
    st.sidebar.subheader("Features")
    show_wordcloud = st.sidebar.checkbox("Show Resume Word Cloud", key='wordcloud_checkbox')
    compare_template = st.sidebar.checkbox("Compare Resume to Ideal Job Template", key='compare_checkbox')
    analyze_skills = st.sidebar.checkbox("Analyze Skills in Resume", key='analyze_checkbox')

    # Main app section with tabs
    tab1, tab2 = st.tabs(["🔍 Resume Screening", "📊 Resume Analysis"])

    with tab1:
        st.title("Resume Screening 📝")
        uploaded_file = st.file_uploader('Upload your resume here (txt or pdf)', type=['txt', 'pdf'])

        if uploaded_file is not None:
            # Custom success message with styling
            st.markdown('<p class="success-message">Resume uploaded successfully!</p>', unsafe_allow_html=True)

            # Try reading the uploaded file
            try:
                resume_bytes = uploaded_file.read()
                resume_text = resume_bytes.decode('utf-8')
            except UnicodeDecodeError:
                resume_text = resume_bytes.decode('latin-1')

            # Process the uploaded resume
            with st.spinner("Analyzing Resume..."):
                cleaned_resume = clean_resume(resume_text)
                input_features = tfidf.transform([cleaned_resume])
                prediction_id = clf.predict(input_features)[0]

            # Mapping predicted category ID to category name
            category_mapping = {
                15: "Java Developer",
                23: "Testing",
                8: "DevOps Engineer",
                20: "Python Developer",
                24: "Web Designing",
                12: "HR",
                13: "Hadoop",
                3: "Blockchain",
                10: "ETL Developer",
                18: "Operations Manager",
                6: "Data Science",
                22: "Sales",
                16: "Mechanical Engineer",
                1: "Arts",
                7: "Database",
                11: "Electrical Engineering",
                14: "Health and Fitness",
                19: "PMO",
                4: "Business Analyst",
                9: "DotNet Developer",
                2: "Automation Testing",
                17: "Network Security Engineer",
                21: "SAP Developer",
                5: "Civil Engineer",
                0: "Advocate",
            }

            category_name = category_mapping.get(prediction_id, "Unknown")
            st.markdown(f"<h3 style='color: black;'>🎯 Predicted Job Category: <span class='prediction'>{category_name}</span></h3>", unsafe_allow_html=True)

            # Display Word Cloud if selected
            if show_wordcloud:
                st.subheader("Word Cloud of Resume")
                generate_wordcloud(resume_text)

            # Download option for the cleaned resume
            st.download_button("Download Cleaned Resume", data=cleaned_resume, file_name="cleaned_resume.txt")

    with tab2:
        st.title("Resume Skills Analysis 📊")
        st.markdown("Analyze the skills in your resume and compare them to the ideal job role.")

        if uploaded_file is not None:
            st.subheader("Skills Analysis")
            st.write("Key Skills found in your resume:")
            # Display some mock skills for demo
            st.write("- Python")
            st.write("- Machine Learning")
            st.write("- Data Science")
            st.write("- Web Development")

            # Visualizing skills match with a pie chart
            skills_match = pd.DataFrame({
                'Skills': ['Python', 'Machine Learning', 'Data Science', 'Web Development'],
                'Proficiency': [80, 70, 90, 60]
            })

            fig, ax = plt.subplots()
            ax.pie(skills_match['Proficiency'], labels=skills_match['Skills'], autopct='%1.1f%%', startangle=90)
            st.pyplot(fig)

# Run the app
if __name__ == "__main__":
    main()

