import streamlit as st

    # Initialize connection.
conn = st.connection('mysql', type='sql')

# Perform query.
df = conn.query('SELECT * FROM collection;', ttl=600)

# Print results.

cat=st.radio('Stash - PandeAkshat', ['All','Core','Research', 'Social', 'Resource', 'LLM', 'Courses'], horizontal=True)

# Send a ping to confirm a successful connection
if cat=='All':
    for item in df.itertuples():
        col1, col2 = st.columns([4,1])
        with col1:
            with st.expander(item.title + ' ----- [' + item.category + ']'):
                st.write(item.information)
        with col2:
            st.link_button('Link', item.url)

if cat=='Core':
    for item in df.itertuples():
        if item.category=='Core':
            col1, col2 = st.columns([4,1])
            with col1:
                with st.expander(item.title + ' ----- [' + item.category + ']'):
                    st.write(item.information)
            with col2:
                st.link_button('Link', item.url)


if cat=='Research':
    for item in df.itertuples():
        if item.category=='Research':
            col1, col2 = st.columns([4,1])
            with col1:
                with st.expander(item.title + ' ----- [' + item.category + ']'):
                    st.write(item.information)
            with col2:
                st.link_button('Link', item.url)
if cat=='Social':
    for item in df.itertuples():
        if item.category=='Social':
            col1, col2 = st.columns([4,1])
            with col1:
                with st.expander(item.title + ' ----- [' + item.category + ']'):
                    st.write(item.information)
            with col2:
                st.link_button('Link', item.url)
if cat=='Resource':
    for item in df.itertuples():
        if item.category=='Resource':
            col1, col2 = st.columns([4,1])
            with col1:
                with st.expander(item.title + ' ----- [' + item.category + ']'):
                    st.write(item.information)
            with col2:
                st.link_button('Link', item.url)

if cat=='LLM':
    for item in df.itertuples():
        if item.category=='LLM':
            col1, col2 = st.columns([4,1])
            with col1:
                with st.expander(item.title + ' ----- [' + item.category + ']'):
                    st.write(item.information)
            with col2:
                st.link_button('Link', item.url)