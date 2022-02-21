import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Ibsen Villarroel
##### *Resume* 
''')

image = Image.open('foto perfil.jpg')
st.image(image, width=175)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Actuary / Data scientist with strong background in mathematics and statistics, with more than 7 years of experience in insurance, data analysis and data science. 
- Skilled in Machine Learning and AI strategies, SQL, PL / SQL, Python, R, JavaScript, HTML5, Solidity, BlockChain
- With Native Spanish, Full Professional English and Limited working French
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" target="_blank">Ibsen Villarroel</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')
st.markdown('**_Bachelors of Science_** (Actuary Science), **Universidad Central de Venezuela**, Caracas, Venezuela, 2010-2017')
#txt('**Bachelors of Science** (Actuary Science), *Universidad Central de Venezuela*, Caracas, Venezuela','2010-2017')
st.markdown('''
- Financial accounting, Financial maths. 
- Microeconomics, Macroeconomics, Econometrics.
- Probability and Stochastic Processes, Multivariate statistics.
- Mathematics, Calculus.
- insurance law and regulation.
- Risk models.
''')
st.markdown('**_Master Degree_** (Data Science), **Universidad Central de Venezuela**, Caracas, Venezuela, 2020-Present')
#txt('**Bachelors of Science** (Actuary Science), *Universidad Central de Venezuela*, Caracas, Venezuela','2010-2017')
st.markdown('''
- Data mining, Text Mining, Web Mining.
- Clustering, K Means.
- Decision Trees, Linear regression and Logistics, Regression Models. 
- Machine Learning, Supervised and Unsupervised Learning, Recommendation Engine. 
- Data Visualization.
- Pentaho, Power BI, Tableau
- MongoDB, Hadoop, Spark.
''')
st.markdown('**SOA Exam P** (Actuary Science), **Society of Actuaries**, Global, Present')
#txt('**Bachelors of Science** (Actuary Science), *Universidad Central de Venezuela*, Caracas, Venezuela','2010-2017')
st.markdown('''
- Currently preparing for the SOA **P-Exam**.
''')
#####################
st.markdown('''
## Work Experience
''')

txt('**Actuary – Oracle Developer**, GIOSEG, Caracas, Venezuela','2019-Present')
st.markdown('''
- Advice and configuration of insurance products, in the SIRweb system, for different companies in Latin America such as Mercantil Seguros (Panama, Venezuela), Banesco Seguros (Panama), Humanos Seguros(Dominican Republic), among others. 
- Using, writing, debugging and testing complex SQL statements and PL/SQL algorithms in stored procedures, packages, functions, triggers.
- Calculate and Automate processes such as the calculation of mathematical and balance reserves for life products.
- knowledge on DBLinks, Hints, Performance Tuning, ETL.
''')

txt('**Trading Data Analyst**, Andes Investments, USA (Remote from Caracas, Venezuela)','2018-2019')
st.markdown('''
- Preparing and interpreting financial document summaries, investment performance reports and income projections for clients. 
- Assess investor risk adversity, creating multiples tests.
- Generating in depth analytics reports to identify meaningful business trends.
- Helps prepare Key Performance Indicator (KPI) reports on trading activity. Monitors effectiveness of trading performance measures on ongoing basis
- Use Python and R statistical software in order to obtain statistical information and graphical analysis of the stock market and Analyze large data sets of historical market data and trading statistics.
- Scarping data and apply text mining and sentiment analysis for particulars stocks market.
''')

txt('**Junior Actuary – Junior Oracle Developer**, Vivir Seguros, Caracas Venezuela', '2014-2017')
st.markdown('''
- Experience in the configuration of general and specific information for insurance products, dynamic processes, and declarations of claims
- Using, writing, debugging and testing complex SQL statements and PL/SQL algorithms in stored procedures, packages, functions, triggers. Import and export xls / xlm files to an oracle data base. Reviews, analyzes, and evaluate business systems and user needs.
''')

txt('**Data Entry**, Instituto Delphos, Caracas Venezuela','2012')
st.markdown('''
- Responsible for the codification, transcription and analysis of results obtained from surveys conducted during the 2012 Venezuelan regional elections. Verify the integrity and accuracy of the data received Application of population sampling techniques
''')

#####################
#st.markdown('''
## Data Science Tools
#''')
#txt3('**Excel-Google Sheets**', 'used for data processing, complicated and visualization calculations.')
#txt4('AutoWeka', 'An automated data mining software based on Weka', 'http://www.mt.mahidol.ac.th/autoweka/')
#txt4('ACPred', 'A computational tool for the prediction and analysis of anticancer peptides','http://codes.bio/acpred/')
#txt4('BioCurator', 'A web server for curating ChEMBL bioactivity data', 'http://codes.bio/biocurator/')
#txt4('CryoProtect', 'A web server for classifying antifreeze proteins from non-antifreeze proteins','http://codes.bio/cryoprotect/')
#txt4('ERpred', 'A web server for the prediction of subtype-specific estrogen receptor antagonists', 'http://codes.bio/erpred')
#txt4('HCVpred', 'A web server for predicting the bioactivity of Hepatitis C virus NS5B inhibitors', 'http://codes.bio/hemopred/')
#txt4('HemoPred', 'A web server for predicting the hemolytic activity of peptides', 'http://codes.bio/hemopred/')
#txt4('iQSP', 'A sequence-based tool for the prediction and analysis of quorum sensing peptides', 'http://codes.bio/iqsp/')
#txt4('Meta-iAVP', 'A sequence-based meta-predictor for improving the prediction of antiviral peptides', 'http://codes.bio/meta-iavp/')
#txt4('osFP', 'A web server for predicting the oligomeric state of fluorescent proteins', 'http://codes.bio/osfp/')
#txt4('PAAP', 'A web server for predicting antihypertensive activity of peptides', 'http://codes.bio/paap/')
#txt4('PepBio', 'A web server for predicting the bioactivity of host defense peptide', 'http://codes.bio/pepbio')
#txt4('PyBact', 'Open source software written in Python for bacterial identification', 'https://sourceforge.net/projects/pybact/')
#txt4('TargetAntiAngio', 'A sequence-based tool for the prediction and analysis of anti-angiogenic peptides','http://codes.bio/targetantiangio/')
#txt4('ThalPred', 'Development of decision model for discriminating Thalassemia trait and Iron deficiency anemia','http://codes.bio/thalpred/')
#txt4('THPep', 'A web server for predicting tumor homing peptides','http://codes.bio/thpep/')


#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`, `Linux`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `altair`, `ggplot2`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Web development', '`Flask`, `HTML`, `CSS`')
txt3('Model deployment', '`streamlit`, `gradio`, `R Shiny`, `Heroku`, `AWS`, `Digital Ocean`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/ibsen-villarroel-garcia-26236777/?locale=en_US')
txt2('Twitter', 'https://twitter.com/ibsenv')
txt2('GitHub', 'https://github.com/ibsenvillarroel')
txt2('Medium', 'https://medium.com/@ibsenvillarroel')
txt2('Portfolio', 'https://ibsenvillarroel.github.io/ibsen/')

