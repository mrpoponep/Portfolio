import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from helper import load_lottieurl
st.set_page_config(page_title="Hotu portfolio", page_icon=":tada:", layout="wide",initial_sidebar_state="collapsed")

selected3 = option_menu(None, ["Home", "Project",  "Contact"], 
    icons=['house', 'cloud-upload', "envelope"], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"display": "none"}, 
        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee","text-align": "center"},
        "nav-link-selected": {"color": "#EEEEEE","background-color": "#053B50",},
    }
)

SOCIAL_MEDIA = {
    "Gmail": "mailto:hotu0403@gmail.com",
    "Facebook": "https://www.facebook.com/profile.php?id=100016522207049&locale=vi_VN",
    "GitHub": "https://github.com/mrpoponep",}


AI_animation = load_lottieurl("https://lottie.host/f9678317-48a0-489f-9e25-a7ae3c4f6831/5TYIeF46Jg.json")
IDE_animation= load_lottieurl("https://lottie.host/b7a30c03-e7d0-433c-a4e4-8ddd22889977/oapyxzBSOl.json")
UI_UX=load_lottieurl("https://lottie.host/c34b9988-6f8c-4f08-8e80-82aefad977f5/seYbUJU2Sk.json")
PROJECT=load_lottieurl("https://lottie.host/97122321-dfea-4c17-ac73-a9b123b04cea/PDn3xmrocK.json")

html_data='<meta property="og:image" content="https://i.ibb.co/2c445wV/Picture1-dax-Dp-Tgqg-transformed-1.png">'
st.components.v1.html(html_data,height=0)

def home():
    with open("assets/styles/style.css") as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
    with st.container():
        st.markdown("""
    <style>
    .big-font {
        font-size:25px ;
    }
    </style>
    <style>
    .bigger-font {
        font-size:40px ;
    }
    </style>
    
    """, unsafe_allow_html=True)
        
    st.write('\n')
 
    left_column, right_column = st.columns(2)
    with left_column:  
        st.title("DUC TU HO")
        st.markdown('<p class="big-font">(AI Engineer)</p>', unsafe_allow_html=True)
        st.markdown('<p class="big-font">"An imaginative and enthusiastic individual who has always been captivated by the magic of technology."</p>', unsafe_allow_html=True)
    with right_column:
        st_lottie(IDE_animation, height=300, key="IDE")

    # Skills Section
    st.write("---")
    st.markdown("<h1 style='text-align: center; color: #222831;'>WHAT I DO</h1>", unsafe_allow_html=True)
    with open("template/hi.html" ,'r') as f: 
            html_data = f.read()
    st.components.v1.html(html_data,height=70)
    with st.container():
        
        left_column, right_column = st.columns(2)
        with left_column:
            st.title("ARTFICIAL INTELLIGENCE")
            st.markdown("""
                <style>
                .big-font {
                    font-size:20px ;
                    padding-left: 20px
                }
                </style>
                
                """, unsafe_allow_html=True)
             
            st.markdown('<p class="big-font">Develop simple models to solve various machine learning use case</p>', unsafe_allow_html=True)
            st.markdown('<p class="big-font">Experience of working with computer vision project</p>', unsafe_allow_html=True)
            st.markdown('<p class="big-font">Machine Learning and Reinforcement Learning Experience</p>', unsafe_allow_html=True)
            st.markdown('<p class="big-font">Familiar with fundamental supervised learning algorithm</p>', unsafe_allow_html=True)
        with right_column:
            st_lottie(AI_animation, height=300, key="AI")

    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    with st.container():
        
        left_column, right_column = st.columns(2)
        with left_column:
            st.title("WEB AND DESKTOP APPLICATION")
            st.markdown("""
                <style>
                .big-font {
                    font-size:20px ;
                    padding-left: 30px
                }
                </style>
                
                """, unsafe_allow_html=True)
             
            st.markdown('<p class="big-font">Build and deploy simple website</p>', unsafe_allow_html=True)
            st.markdown('<p class="big-font">Design UI/UX for destop app and website</p>', unsafe_allow_html=True)
            
        with right_column:
            st_lottie(UI_UX, height=250, key="UI_UX")

def project():
    with open("assets/styles/style.css") as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
    with st.container():
        st.markdown("""
    <style>
    .big-font {
        font-size:25px ;
    }
    </style>
    <style>
    .bigger-font {
        font-size:40px ;
        text-align: center;
        align-items: top;
        justify-content: top;
        padding: 0 0 0 60px
    }
    </style>
    """, unsafe_allow_html=True)
        

    left_column, right_column = st.columns(2)
    with right_column:  
        st.markdown("<h1 style='text-align: center; color:#053B50 ;'>PROJECT</h1>", unsafe_allow_html=True)
        st.markdown('<center class="big-font">Leveraging cutting-edge technologies, I have developed and fine-tuned models which excel in reinforcement learning and computer vision. My expertise also extends to deploying these models into web and desktop applications.</center>', unsafe_allow_html=True)
    with left_column:
        st_lottie(PROJECT, height=300, key="project")

    st.write("---")

    with open("template/project.html" ,'r') as f: 
            html_data = f.read()

    st.components.v1.html(html_data,height=800,)
    

def contact():
    with open("assets/styles/style.css") as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
    with open("template/contact.html" ,'r') as f: 
        html_data = f.read()
    st.components.v1.html(html_data,height=1000)

    
if selected3=="Home":
    home()
if selected3=="Project":
    project()
if selected3=="Contact":
    contact()
