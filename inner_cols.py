### Imports
import streamlit as st
import pandas as pd
import numpy as np  
import re
from string import punctuation
import requests
import streamlit_nested_layout

###Import Data
#reviews_wc = pd.read_pickle("pickles/review_final-wc_p.pkl")

### Define columns:
st.set_page_config(page_title=None, page_icon=None, layout="wide", menu_items=None)

outer_cols = st.columns([2,0.5,2])

### Left side of screen
with outer_cols[0]:
    st.markdown('## Movie')
    title = st.text_input('Type the title and press Enter (try Carmencita)')
    if title:
            try: 
                url = f"https://www.omdbapi.com/?t={title}&apikey=38187759"
                re = requests.get(url)
                re = re.json()

                inner_cols = st.columns([1,2])
                with inner_cols[0]:
                    st.image(re['Poster'])

                with inner_cols[1]:
                    st.header(re['Title'])
                    st.caption(f"Gender:{re['Genre']} Year: {re['Year']} ")
                    st.write (re['Plot'])
                    st.text(f"Rating: {re['imdbRating']}")
                    st.progress(float(re['imdbRating'])/10)

                    ### Right side of screen    
                    with outer_cols[0]:
                        st.markdown('')
                        
                    with outer_cols[2]:
                        st.markdown('## Recommendations')
                        st.text('')
                        inner_cols = st.columns([1,2])
                        
                        with inner_cols[0]:
                            st.markdown('Recommendation 1')
                        
                        with inner_cols[1]:
                            st.write (re['Plot'])
                        
                        inner_cols = st.columns([1,2])
                        with inner_cols[0]:
                            st.markdown('Recommendation 2')
                        with inner_cols[1]:
                            st.write (re['Plot'])
                        
                        inner_cols = st.columns([1,2])
                        with inner_cols[0]:
                            st.markdown('Recommendation 3')
                        with inner_cols[1]:
                            st.write (re['Plot'])


            except:
                title = False
                st.markdown('''We currently don't have detailed information on this movie
                drop us an email and our scouting team will look into it and will send you our review''')
                contact_form = """
                <form action="https://formsubmit.co/inovmovie@gmail.com" method="POST">
                <input type="text" name="Suggestion" placeholder="Movie suggestion" required>
                <input type="text name="Name" placeholder="Your name" required>
                <button type="submit">Send</button>
                </form>
                """
                st.markdown (contact_form, unsafe_allow_html=True)

# outer_cols = st.columns([1])
# with outer_cols[1]:
#     st.markdown('## Recommendations')
#     inner_cols = st.columns([1,2])
                        
#     with inner_cols[0]:
#         st.markdown('Recommendation 1')
                        
#     with inner_cols[1]:
#          st.write ('hello world')
                        
#     inner_cols = st.columns([1,2])
#     with inner_cols[0]:
#         st.markdown('Recommendation 2')
#     with inner_cols[1]:
#         st.write ('hello world')
                        
#     inner_cols = st.columns([1,2])
#     with inner_cols[0]:
#         st.markdown('Recommendation 3')
#     with inner_cols[1]:
#         st.write ('hello world')