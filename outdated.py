import streamlit as st

with open('style.css', encoding='UTF-8') as f:
  st.html(f'<style>{f.read()}</style>')
st.info('Cessay의 공식 페이지가 이전 되었습니다!🎉 이제부터는 불편한 하단 Streamlit버튼 없이 Cessay를 이용할 수 있으니 다음 링크를 사용해주세요')
st.page_link("https://cessay.kro.kr", label="cessay.kro.kr", icon="✏️")
