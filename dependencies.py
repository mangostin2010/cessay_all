import streamlit as st
from deta import Deta
import io
import docx
from streamlit_js_eval import streamlit_js_eval

def get_essay_list():
    # Logging into Deta.Space database
    DETA_KEY = 'c0ki5D3avML_gSssDuj33rfuzLDrjwL1gc42oQkbgsHj'
    deta = Deta(DETA_KEY)
    db = deta.Drive("Write_Your_Essay")

    # Getting the essay lists
    response = db.list()["names"]
    response.reverse()
    return response

def get_essay_from_name(essay_name):
    # Logging into Deta.Space database
    DETA_KEY = 'c0ki5D3avML_gSssDuj33rfuzLDrjwL1gc42oQkbgsHj'
    deta = Deta(DETA_KEY)
    db = deta.Drive("Write_Your_Essay")

    # Get the file from Deta.Space database
    file = db.get(essay_name)
    file_stream = io.BytesIO(file.read())
    return file_stream

def get_text_from_file(file_stream):
    doc = docx.Document(file_stream)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

def remove_essay_from_name(essay_name):
    # Logging into Deta.Space database
    DETA_KEY = 'c0ki5D3avML_gSssDuj33rfuzLDrjwL1gc42oQkbgsHj'
    deta = Deta(DETA_KEY)
    db = deta.Drive("Write_Your_Essay")

    db.delete(essay_name)
    streamlit_js_eval(js_expressions="parent.window.location.reload()")

def check_user_url():
    return_value = streamlit_js_eval(js_expressions="""document.URL""")
    if return_value == None: st.stop()
    # Only for debugging
    return_test_value = f"{return_value} nice"
    streamlit_js_eval(js_expressions=f"""console.log({return_test_value})""")
    
    if 'check-cessay.kro.kr' in return_value: st.switch_page('pages/check_cessay.py')
    elif 'cessay.kro.kr' in return_value: st.switch_page('pages/cessay_page.py')
    
def get_user_url():
    if 'Justin is handsome' in st.query_params:
        return_value = streamlit_js_eval(js_expressions="""document.URL""")
        st.write(return_value.replace('http://','').split(sep='/')[0])
        st.stop()

def return_user_url():
    return_value = streamlit_js_eval(js_expressions="""document.URL""")
    return return_value.replace('http://','').split(sep='/')[0]

def get_announcements():
    DETA_KEY = 'c0ki5D3avML_gSssDuj33rfuzLDrjwL1gc42oQkbgsHj'
    deta = Deta(DETA_KEY)
    db = deta.Base("announcement")

    res = db.fetch()
    all_items = res.items

    while res.last:
        res = db.fetch(last=res.last)
        all_items += res.items

    if not all_items:
        # Empty list
        return None
        
    else:
        ann = db.get('announce')
        return ann
