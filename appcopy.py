import streamlit as st
import pandas as pd

st.title("大腿骨回旋角度予測")

# パスワード入力（マスク付き）
password = st.text_input("パスワードを入力してください", type="password")

# パスワードが正しい場合のみ計算画面を表示
if password == "YCUMED":
    st.write("""
    術前大腿骨回旋角度とBMIを入力すると、ステム角度が0°から30°まで5°刻みの場合の
    術後大腿骨回旋角度を予測します
    """)

    # 入力フィールド
    daidai_kaiten_kakudo = st.number_input('術前大腿骨回旋角度 (°)', 
                                           min_value=-180.0, max_value=180.0, 
                                           value=0.0, step=0.1)
    bmi = st.number_input('BMI', 
                          min_value=0.0, max_value=100.0, 
                          value=22.0, step=0.1)

    # 「計算」ボタン
    if st.button("計算"):
        # ステム角度のリスト（0°から30°まで5°刻み）
        stem_angles = list(range(0, 31, 5))

        # 予測結果を計算
        predictions = []
        for stem_angle in stem_angles:
            y = (0.3895 * daidai_kaiten_kakudo) + (-0.3228 * stem_angle) + (0.5491 * bmi) - 5.0894
            fra = stem_angle + y  # FRA(術後大腿骨回旋角度 + ステム角度) の計算
            predictions.append({
                'ステム角度 (°)': stem_angle,
                '術後大腿骨回旋角度 (°)': round(y, 2),
                'FRA(°)': round(fra, 2)
            })

        # 結果をデータフレームに変換
        results_df = pd.DataFrame(predictions)
        # インデックスをリセットして非表示にする
        results_df.reset_index(drop=True, inplace=True)

        # 結果を表示
        st.write("### 予測結果")
        st.table(results_df.style.hide(axis="index"))
else:
    # パスワードが空の場合はスキップ
    if password != "":
        st.warning("パスワードが正しくありません。")
    
