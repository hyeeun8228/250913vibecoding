import streamlit as st
import pandas as pd
import altair as alt

st.title("🌍 MBTI 비율 상위 10개 국가")

uploaded_file = st.file_uploader("📂 MBTI CSV 파일 업로드", type="csv")

@st.cache_data
def load_data(file):
    return pd.read_csv(file)

if uploaded_file is not None:
    df = load_data(uploaded_file)
    st.success("✅ 업로드한 파일을 사용합니다")
else:
    df = load_data("countriesMBTI_16types.csv")
    st.info("ℹ️ 기본 CSV 파일을 사용합니다")

df_long = df.melt(id_vars=["Country"], var_name="MBTI", value_name="Ratio")
df_max = df_long.loc[df_long.groupby("Country")["Ratio"].idxmax()]
top10 = df_max.sort_values("Ratio", ascending=False).head(10)

st.subheader("🏆 MBTI 비율이 가장 높은 국가 Top 10")

chart = (
    alt.Chart(top10)
    .mark_bar()
    .encode(
        x=alt.X("Ratio:Q", title="비율"),
        y=alt.Y("Country:N", sort="-x", title="국가"),
        color="MBTI:N",
        tooltip=["Country", "MBTI", "Ratio"]
    )
    .interactive()
)

st.altair_chart(chart, use_container_width=True)
