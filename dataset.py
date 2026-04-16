import streamlit as st
import pandas as pd

st.set_page_config(page_title='Company Dataset', layout='wide')

st.title('📊 Company Dataset Directory')

companies = [
    ['Big Drop Inc','https://bigdropinc.com','Digital Agency','hello@bigdropinc.com','+1 212-430-3830'],
    ['Lounge Lizard','https://loungelizard.com','Web Design','info@loungelizard.com','+1 646-661-7828'],
    ['HUEMOR','https://huemor.rocks','Web Development','hello@huemor.rocks','+1 631-319-1555'],
    ['Hudson Integrated','https://hudsonintegrated.com','Digital Marketing','info@hudsonintegrated.com','+1 212-381-0556'],
    ['DotcomWeavers','https://dotcomweavers.com','E-commerce','info@dotcomweavers.com','+1 888-315-6518'],
    ['Socialfix Media','https://socialfix.com','Digital Marketing','info@socialfix.com','+1 212-684-2454'],
    ['Mainstay','https://mainstay.com','Software Dev','hello@mainstay.com','+1 212-255-0000'],
    ['Major Tom','https://majortom.com','Digital Strategy','info@majortom.com','+1 646-381-1934'],
    ['Crafted','https://craftedny.com','Creative Agency','hello@craftedny.com','+1 212-213-9005'],
    ['Avenue Code','https://avenuecode.com','Software Dev','info@avenuecode.com','+1 888-512-2633'],
    ['Ruckus Marketing','https://ruckusmarketing.com','Branding','info@ruckusmarketing.com','+1 212-913-9828'],
    ['Social Driver','https://socialdriver.com','Digital Strategy','info@socialdriver.com','+1 202-747-3456'],
    ['The Bureau','https://thebureau.io','Web Design','hello@thebureau.io','+1 917-746-8888'],
    ['Thrive Design','https://thriveny.com','Web Design','hello@thriveny.com','+1 212-671-1100'],
    ['Small Planet','https://smallplanet.com','App Development','hello@smallplanet.com','+1 718-243-2070'],
    ['Ready Set Rocket','https://readysetrocket.com','Digital Marketing','hello@readysetrocket.com','+1 212-673-4554'],
    ['Simple Science','https://simplescience.com','Tech/Creative','info@simplescience.com','+1 800-410-0000'],
    ['Ironpaper','https://ironpaper.com','B2B Marketing','info@ironpaper.com','+1 212-993-5811'],
    ['Dom & Tom','https://domandtom.com','Mobile Apps','hello@domandtom.com','+1 646-602-0000'],
]

df = pd.DataFrame(companies, columns=['Company Name','Website','Category','Email','Phone'])

search = st.text_input('🔍 Search Company')
if search:
    df = df[df['Company Name'].str.contains(search, case=False, na=False)]

st.dataframe(df, use_container_width=True)

st.subheader('🌐 Open Links')
for _, row in df.iterrows():
    st.markdown(f"**{row['Company Name']}** - [Open Website]({row['Website']})")
