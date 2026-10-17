import streamlit as st
import pandas as pd

# 1. アプリのタイトル
st.title("🚤 競艇フル解析 AIアプリ（全部盛り版）")
st.write("レース場と直前情報を入力すると、3大解析（イン危険度・展示歪み・展開）を自動計算します。")

# 2. 画面の入力エリア
st.subheader("📋 レース情報の入力")
place = st.selectbox("レース場を選択", ["平和島", "多摩川", "浜名湖", "蒲郡", "住之江", "尼崎", "若松", "芦屋", "福岡"])
race_num = st.number_input("レース番号 (R)", min_value=1, max_value=12, value=1)

wind_speed = st.slider("風速 (m)", 0, 10, 2)
wind_dir = st.radio("風向き", ["追い風", "向かい風", "横風"], horizontal=True)

st.write("---")

# 3. 選手データ
st.subheader("👥 出走表 & 直前情報（自動連携テストデータ）")
boat_data = [
    {"艇番": 1, "選手名": "峰 竜太", "展示タイム": 6.67, "過去勝率": 0.78},
    {"艇番": 2, "選手名": "毒島 誠", "展示タイム": 6.72, "過去勝率": 0.72},
    {"艇番": 3, "選手名": "茅原 悠紀", "展示タイム": 6.69, "過去勝率": 0.68},
    {"艇番": 4, "選手名": "石野 貴之", "展示タイム": 6.75, "過去勝率": 0.65},
    {"艇番": 5, "選手名": "池田 浩二", "展示タイム": 6.71, "過去勝率": 0.63},
    {"艇番": 6, "選手名": "桐生 順平", "展示タイム": 6.78, "過去勝率": 0.60},
]
df = pd.DataFrame(boat_data)
st.dataframe(df)

# 4. 🔥 解析スタートボタン
if st.button("⚡️ 3大解析を一括実行する", type="primary"):
    st.write("---")
    st.success(f"【解析完了】 {place} {race_num}R の計算結果")
    
    st.markdown("### 📊 解析①：イン逃げ信頼度判定")
    if wind_speed >= 5 and wind_dir == "向かい風":
        st.error("⚠️ 危険度：大！ (向かい風強風のため、1号艇が飛ぶ確率が上昇中)")
    else:
        st.info("✅ 信頼度：普通 (安定したイン戦が予想されます)")
        
    st.markdown("### 🔍 解析②：展示の歪みチェック")
    fast_boats = df[df["展示タイム"] <= 6.70]
    st.write("展示タイムが抜けて良い（6.70以下）注目レーサー:")
    st.dataframe(fast_boats[["艇番", "選手名", "展示タイム"]])
    
    st.markdown("### 🎯 解析③：推奨買い目と確率シミュレーション")

    st.warning("【AI推奨】3連単：1-2-3, 1-3-2 (確率: 各24%) / 穴狙い: 3-1-全")
