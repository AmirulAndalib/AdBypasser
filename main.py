
import random
import js2py
import streamlit as st
from PyBypass.main import BypasserNotFoundError, UnableToBypassError, UrlConnectionError
import PyBypass as bypasser
js = """
	atOptions = {
		'key' : 'f274454d04b18b3c2e76a5be61a28a33',
		'format' : 'iframe',
		'height' : 90,
		'width' : 728,
		'params' : {}
	};
	document.write('<scr' + 'ipt type="text/javascript" src="http' + (location.protocol === 'https:' ? 's' : '') + '://www.profitabledisplaynetwork.com/f274454d04b18b3c2e76a5be61a28a33/invoke.js"></scr' + 'ipt>');
"""
ad = js2py.eval_js(js)

print(js)

st.set_page_config(page_title="URL Bypasser", page_icon='🧊',
                   layout="centered", initial_sidebar_state="auto",    menu_items={
                       'Get Help': 'askfriends1@protonmail.com',
                       'Report a bug': "askfriends1@protonmail.com",
                       'About': "This is URL Bypasser website."
                   })


def random_celeb():
    return random.choice([st.balloons()])

st.title("URL Bypasser")
tab1, tab2 = st.tabs(["Bypass", "Available Websites", ])

__avl_website__ = ['try2link.com', ' adf.ly', ' bit.ly', ' ouo.io', ' ouo.press', ' shareus.in', ' shortly.xyz', ' tinyurl.com', ' thinfi.com', ' hypershort.com ', 'safeurl.sirigan.my.id', ' gtlinks.me', ' loan.kinemaster.cc', ' theforyou.in', ' linkvertise.com', ' shorte.st', ' earn4link.in', ' tekcrypt.in', ' link.short2url.in', ' go.rocklinks.net', ' rocklinks.net', ' earn.moneykamalo.com', ' m.easysky.in', ' indianshortner.in', ' open.crazyblog.in', ' link.tnvalue.in',' shortingly.me', ' open2get.in', ' dulink.in', ' bindaaslinks.com', ' za.uy', ' pdiskshortener.com', ' mdiskshortner.link', ' go.earnl.xyz', ' g.rewayatcafe.com', ' ser2.crazyblog.in', ' bitshorten.com', ' rocklink.in', ' droplink.co', ' tnlink.in', ' ez4short.com', ' xpshort.com', ' vearnl.in', ' adrinolinks.in', ' techymozo.com', ' linkbnao.com', ' linksxyz.in', ' short-jambo.com', ' ads.droplink.co.in', ' linkpays.in', ' pi-l.ink', ' link.tnlink.in ', ' pkin.me']

with tab1:
    show_alert = False
    url = st.text_input(label="Paste your URL")
    if st.button("Submit"):
        if url:
            try:

                with st.spinner("Loading..."):
                    bypassed_link = bypasser.bypass(url)
                    st.success(bypassed_link)

                random_celeb()

                with st.expander("Copy"):
                    st.code(bypassed_link)

            except (UnableToBypassError, BypasserNotFoundError, UrlConnectionError) as e:
                if show_alert := True:
                    st.error(e)

            if st.button("Dismiss"):
                show_alert = False

        elif show_alert := True:
            st.error("No URLS found")

with tab2:
    st.subheader("Available Websites")
    st.table(__avl_website__)


