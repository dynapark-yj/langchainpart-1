

import streamlit as st
from stock_info import stock
from report_service import investment_report
from search import stock_search

class SearchResult:
    def _init_(self,item:
               self.item = investment_report)
    @property
    def symbol(self):
        return self.item["Symbol"]
    
    @property
    def name(self):
        return f"{self.symbol} {self.name}"


st.title("AI 추자 보고서 생성 서비스" )

search_query =st.text_input("회사명", "Apple Inc.")
hits = stck_search(search_query)['hits']
search_results = [SearchResult(hit) for hit in hits]

st.selectbox("검색 결과 리스트", search_results )

tabs = ["회사 정보", "AI 투자자 보고서" ]
tab1, tab2 = st.tabs(tabs)

with tab1:



with tab2:

