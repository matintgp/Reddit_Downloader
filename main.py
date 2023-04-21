import streamlit as st
import requests 
import json

st.title('Reddit Video Downloader 📸')

header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

reddit_url = st.text_input(label = 'Enter your Reddit URL')

# https://www.domian.com.json

if reddit_url:

    if reddit_url[len(reddit_url)-1] == '/':
        json_url = reddit_url[:len(reddit_url)-1]+'.json'
    else:
        json_url = reddit_url + 'json'
        
    json_res = requests.get(json_url, headers=header)

    # st.write(json_res)

    if json_res.status_code != 200:
        st.warning("Error Detected, check the URL!!!")
    else:
        mp4_url = json_res.json()[0]['data']['children'][0]['data']['secure_media']['reddit_video']['fallback_url']
        
    # st.write(mp4_url)
    with st.spinner("Waiting to download the video..."):
        mp4_res = requests.get(mp4_url, headers=header)
        
        if mp4_res.status_code == 200:
            st.video(mp4_res.content)

            # st.download_button("Download", mp4_res, "mp4")
        else:
            st.warning("⚠️ Video Download Failed!!!")

else:
    st.error('⚠️Enter the right URL')