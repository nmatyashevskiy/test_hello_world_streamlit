import streamlit as st
import sys
from streamlit import cli as stcli

if __name__ == '__main__':
    if st._is_running_with_streamlit:
        st.header("Hello world")
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())