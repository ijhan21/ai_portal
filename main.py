import streamlit as st
import os
st.set_page_config(layout="wide")

path = "images"

st.markdown("# ISOS AI Solution Portal")
st.info("AI 개발 항목에 대한 종합적인 설명과 연결 기능 제공 포털")
contents = [
    ("공구 파손/마모 관리 Solution",'http://191.1.70.188:8501',"Spindle Load의 정밀 측정 데이터에서 패턴을 추출하여 높은 신뢰성을 확보한 공구관리 솔루션", "tm.png"),
    ("공정최적화 데이터 분석 Solution",'http://191.1.70.188:8503',"6 Sigma와 대표 인공지능 모델을 결합한 통합 기업 데이터 분석 솔루션", "analysis.png"),
    ("hns 공정최적화 분석 API",'http://191.1.70.188:8085',"인공지능의 시스템 이식성과 보안성을 갖춘 솔루션 구현 API", "hns_rest.webp"),
    ("hns 공정최적화 분석 API Document",'http://191.1.70.188:8085/docs',"빠르고 유연한 개발을 위한 Document", "rest_docs.png"),
    ("데이터 품질 분석 Solution",'http://191.1.70.188:8505',"ISO 8000 데이터 품질 국제표준, ISO/IEC 25024 소프트웨어 엔지니어링 및 시스템에 대한 국제표준에 의거하여 데이터의 품질을 평가하는 솔루션", "data_q.png")
]

for i in range( len(contents)//2 if len(contents)//2 == len(contents)/2 else len(contents)//2+1):
    cols = st.columns(2)
    with cols[0]:
        content = contents[2*i]
        st.markdown("##### [{}]({})".format(content[0], content[1]))
        st.image(os.path.join(path, content[3]))
        st.success(content[2])
    if 2*i+1<len(contents):
        with cols[1]:
            content = contents[2*i+1]
            st.markdown("##### [{}]({})".format(content[0], content[1]))
            st.image(os.path.join(path, content[3]))
            st.success(content[2])
        