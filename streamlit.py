import streamlit as st
import pandas as pd
from lxml import etree

tree = etree.parse("./xml_example.xml")

lstKey = []
lstValue = []
for p in tree.iter() :
    lstKey.append(tree.getpath(p).replace("/",".")[1:])
    lstValue.append(p.text)

df = pd.DataFrame({'key' : lstKey, 'value' : lstValue})
df.sort_values('key')
st.write(df)
