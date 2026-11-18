from pathlib import Path
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title='StayScope | Airbnb Analytics',page_icon='🏙️',layout='wide',initial_sidebar_state='expanded')
ROOT=Path(__file__).resolve().parent
if not (ROOT/'data').exists() and (ROOT.parent/'data').exists(): ROOT=ROOT.parent
DATA=ROOT/'data'/'cleaned_airbnb.csv'
OUT=ROOT/'outputs'
st.markdown('''<style>.block-container{padding-top:1.5rem}.hero{padding:24px;border-radius:18px;background:linear-gradient(120deg,#123654,#176b83);color:white;margin-bottom:16px}.hero h1{color:white;margin:0;font-size:2.3rem}.hero p{color:#d7eef4;margin:6px 0 0}.stMetric{border:1px solid #e4e9ee;border-radius:12px;padding:12px}</style>''',unsafe_allow_html=True)
st.markdown('<div class="hero"><h1>🏙️ StayScope</h1><p>New York City Airbnb • 2019 Historical Listing Analytics & Web Content Mining</p></div>',unsafe_allow_html=True)
if not DATA.exists():
 st.error(f'Cleaned dataset not found: {DATA}')
 st.info('Keep dashboard.py inside your StayScope project folder (next to data and outputs), then run it again.')
 st.stop()
@st.cache_data
def load_data(path):
 d=pd.read_csv(path,low_memory=False)
 return d
raw=load_data(DATA)
st.sidebar.title('🔎 Explore listings')
st.sidebar.caption('Filters update the interactive charts. Saved notebook graphs below remain the original full-dataset results.')
groups=sorted(raw['neighbourhood_group'].dropna().unique().tolist())
selected_groups=st.sidebar.multiselect('Neighbourhood groups',groups,default=groups)
rooms=sorted(raw['room_type'].dropna().unique().tolist())
selected_rooms=st.sidebar.multiselect('Room types',rooms,default=rooms)
maxprice=int(raw['price'].quantile(.99))
price_range=st.sidebar.slider('Price range (USD)',10,maxprice,(10,maxprice))
df=raw[raw['neighbourhood_group'].isin(selected_groups)&raw['room_type'].isin(selected_rooms)&raw['price'].between(*price_range)].copy()
st.sidebar.divider()
st.sidebar.info('Dataset: NYC Airbnb Open Data (2019). This is not live Airbnb pricing or availability.')
if df.empty: st.warning('No listings match the selected filters. Adjust filters in the sidebar.');st.stop()
cols=st.columns(4)
for col,label,value in zip(cols,['Listings shown','Average price','Median price','Neighbourhoods'],[f'{len(df):,}',f'${df.price.mean():,.2f}',f'${df.price.median():,.0f}',f'{df.neighbourhood.nunique():,}']): col.metric(label,value)
tabs=st.tabs(['📊 Overview','💵 Prices & Outliers','📍 Neighbourhoods','🧩 Clustering','🔤 Web Content Mining','📁 Data & Project'])
def saved_chart(name,title,caption=''):
 st.markdown(f'#### {title}')
 p=OUT/name
 if p.exists():st.image(str(p),use_container_width=True)
 else:st.warning(f'Missing graph: outputs/{name}. Run StayScope_Analysis.ipynb to generate it.')
 if caption:st.caption(caption)
with tabs[0]:
 st.subheader('Interactive overview (responds to filters)')
 a,b=st.columns(2)
 with a:st.plotly_chart(px.histogram(df,x='room_type',color='room_type',title='Room type distribution',labels={'room_type':'Room type'}),use_container_width=True)
 with b:st.plotly_chart(px.histogram(df,x='price',nbins=45,title='Listing price distribution'),use_container_width=True)
 st.divider();st.subheader('Original notebook figures')
 a,b=st.columns(2)
 with a:saved_chart('room_type_distribution.png','Room Type Distribution','Entire homes/apartments were the largest category in the cleaned dataset.')
 with b:saved_chart('average_price_by_room_type.png','Average Price by Room Type','Entire homes/apartments had the highest average price.')
with tabs[1]:
 st.subheader('Price exploration')
 a,b=st.columns(2)
 with a:st.plotly_chart(px.box(df,x='room_type',y='price',color='room_type',title='Filtered price ranges by room type'),use_container_width=True)
 with b:st.plotly_chart(px.histogram(df,x='price',nbins=55,title='Filtered price distribution'),use_container_width=True)
 a,b=st.columns(2)
 with a:saved_chart('price_distribution.png','Original Price Distribution','Original plot limits the x-axis to $1,000 for readability.')
 with b:saved_chart('price_outliers.png','IQR Price Outlier Analysis','Q1 = $69, Q3 = $175, upper threshold = $334; 2,972 price outliers in the cleaned data.')
with tabs[2]:
 st.subheader('Neighbourhood insights')
 a,b=st.columns(2)
 with a:
  top=df.neighbourhood.value_counts().head(10).reset_index();top.columns=['Neighbourhood','Listings']
  st.plotly_chart(px.bar(top,x='Listings',y='Neighbourhood',orientation='h',title='Top neighbourhoods (filtered)').update_layout(yaxis={'categoryorder':'total ascending'}),use_container_width=True)
 with b:
  g=df.groupby(['neighbourhood_group','room_type'],as_index=False)['price'].mean()
  st.plotly_chart(px.bar(g,x='neighbourhood_group',y='price',color='room_type',barmode='group',title='Average price by area and room type'),use_container_width=True)
 a,b=st.columns(2)
 with a:saved_chart('top_neighbourhoods.png','Top 10 Neighbourhoods')
 with b:saved_chart('room_type_patterns.png','Room Types by Neighbourhood Group')
 saved_chart('price_patterns_heatmap.png','Price Pattern Heatmap','Manhattan entire homes/apartments average approximately $249.3 in the original dataset.')
with tabs[3]:
 st.subheader('K-Means clustering')
 st.write('The notebook groups listings into **four clusters** using price, minimum nights, reviews, reviews per month, and availability. The reported silhouette score is approximately **0.307**.')
 saved_chart('kmeans_clusters.png','K-Means Cluster Scatter Plot','The two-dimensional plot shows minimum nights vs price; clustering used five features.')
 st.info('Clustering is unsupervised machine learning, not itself Web Content Mining.')
with tabs[4]:
 st.subheader('Web Content Mining: listing titles')
 st.write('This is the main Web Data Mining component: counting frequent individual words (unigrams) and adjacent word pairs (bigrams) in Airbnb listing titles.')
 a,b=st.columns(2)
 with a:saved_chart('frequent_words.png','Top 20 Listing-Title Words','Common terms include room, bedroom, private, apartment, and cozy.')
 with b:saved_chart('frequent_bigrams.png','Top 20 Two-Word Phrases','Common phrases include private room, central park, and east village.')
with tabs[5]:
 st.subheader('Explore the cleaned data')
 st.dataframe(df.head(200),use_container_width=True)
 st.download_button('Download filtered listings CSV',df.to_csv(index=False).encode('utf-8'),'stayscope_filtered.csv','text/csv')
 st.markdown('''**Workflow:** NYC Airbnb 2019 CSV → inspection → cleaning → EDA → IQR outlier analysis → K-Means → listing-title word and bigram mining → charts and CSV outputs.

**Limitations:** Historical data, not live pricing; missing last-review dates; outliers; moderate/weak cluster separation.

**Project:** [GitHub repository](https://github.com/sakshibhagit05/StayScope)''')
