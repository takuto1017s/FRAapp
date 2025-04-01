import streamlit as st
import pandas as pd

st.title("大腿骨回旋角度予測")

st.write("""
術前大腿骨回旋角度とBMIを入力すると、ステム角度が0°から30°まで5°刻みの場合の術後大腿骨回旋角度を予測します
""")

# 入力フィールド
daidai_kaiten_kakudo = st.number_input('術前大腿骨回旋角度 (°)', min_value=-180.0, max_value=180.0, value=0.0, step=0.1)
bmi = st.number_input('BMI', min_value=0.0, max_value=100.0, value=22.0, step=0.1)

# ステム角度のリスト（0°から30°まで5°刻み）
stem_angles = list(range(0, 31, 5))

# 予測結果を計算
predictions = []
for stem_angle in stem_angles:
    y = (0.0108 * daidai_kaiten_kakudo) + (-0.3143 * stem_angle) + (0.4814 * bmi) + (0.0161 * bmi * daidai_kaiten_kakudo)-3.9725
    fra = stem_angle + y  # FRAの計算
    predictions.append({
        'ステム角度 (°)': stem_angle,
        '術後大腿骨回旋角度 (°)': round(y, 2),
        'FRA(°)': round(fra, 2)  # FRAの値を追加
    })


# 結果をデータフレームに変換
results_df = pd.DataFrame(predictions)


# インデックスをリセットして非表示にする
results_df.reset_index(drop=True, inplace=True)

# 結果を表示
st.write("### 予測結果")
#st.table(results_df)
st.table(results_df.style.hide(axis="index"))
# 必要な列のみ表示
#st.dataframe(results_df[['ステム角度 (°)', '術後大腿骨回旋角度 (°)', 'FRA(°)']])
