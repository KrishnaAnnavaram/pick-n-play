import streamlit as st
import random
from utils.file_parser import parse_excel

# ✅ Page setup
st.set_page_config(page_title="Pick-n-Play", layout="centered")
st.title("🎲 Pick-n-Play: A Smart Group Selector App")

# ✅ Upload Excel file
uploaded_file = st.file_uploader("📁 Upload your group Excel file", type=["xlsx"])

if uploaded_file:
    try:
        # ✅ Parse groups from Excel
        groups = parse_excel(uploaded_file)
        group_numbers = [g["group_number"] for g in groups]

        st.success(f"✅ Successfully loaded {len(groups)} groups.")

        # ✅ Exclude input
        excluded = st.multiselect("❌ Select group(s) to exclude from random selection:", group_numbers)

        # ✅ Track shown groups
        if "shown_groups" not in st.session_state:
            st.session_state.shown_groups = []

        # ✅ Filter groups: not shown and not excluded
        available_groups = [
            g for g in groups
            if g["group_number"] not in excluded
            and g["group_number"] not in st.session_state.shown_groups
        ]

        # ✅ Pick button
        if st.button("🎯 Pick a Random Group"):
            if available_groups:
                selected = random.choice(available_groups)
                st.session_state.shown_groups.append(selected["group_number"])

                st.subheader(f"🎉 {selected['group_number']}")
                st.markdown(f"**📌 Project Title:** {selected['project_title']}")
                st.markdown("**👥 Group Members:**")
                for member in selected["members"]:
                    st.markdown(f"- {member}")
            else:
                st.warning("🚫 No more groups left to pick!")

        # ✅ Reset button (safe, no rerun)
        if st.button("🔁 Reset All"):
            st.session_state.shown_groups = []
            st.warning("✅ Group memory has been cleared. Please manually refresh the page to restart.")

        # ✅ Status view
        with st.expander("📋 View Group Selection Status", expanded=True):
            st.markdown("### ✅ Completed Groups")
            if st.session_state.shown_groups:
                for g in st.session_state.shown_groups:
                    st.markdown(f"- {g}")
            else:
                st.info("No groups have been selected yet.")

            st.markdown("### ❌ Excluded Groups")
            if excluded:
                for g in excluded:
                    st.markdown(f"- {g}")
            else:
                st.info("No groups have been excluded.")

    except Exception as e:
        st.error(f"❌ Error processing file: {e}")
