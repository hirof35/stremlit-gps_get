import streamlit as st
from streamlit_js_eval import get_geolocation
import folium
from streamlit_folium import st_folium
from geopy.distance import geodesic  # 距離計算用

st.title("📍 ジオフェンス・アラートアプリ")

# --- 設定: ターゲット地点 (例: 東京駅) ---
TARGET_LAT = 35.6812
TARGET_LON = 139.7671
RADIUS_METERS = 100  # 通知を出す半径(m)

st.sidebar.header("ジオフェンス設定")
st.sidebar.write(f"ターゲット緯度: {TARGET_LAT}")
st.sidebar.write(f"ターゲット経度: {TARGET_LON}")
st.sidebar.write(f"通知半径: {RADIUS_METERS}m")

# 1. 現在地の取得
location = get_geolocation()

if location:
    curr_lat = location['coords']['latitude']
    curr_lon = location['coords']['longitude']
    current_pos = (curr_lat, curr_lon)
    target_pos = (TARGET_LAT, TARGET_LON)

    # 2. ターゲットとの距離を計算 (単位: メートル)
    distance = geodesic(current_pos, target_pos).meters

    # 3. 判定と通知
    if distance <= RADIUS_METERS:
        st.error(f"⚠️ 【通知】エリア内に侵入しました！ (距離: {distance:.1f}m)")
        # ここで外部API（LINE Notifyやメール等）を叩く処理も追加可能
    else:
        st.success(f"エリア外です。ターゲットまであと {distance:.1f}m")

    # 4. 地図の表示
    m = folium.Map(location=current_pos, zoom_start=16)
    
    # 現在地マーカー
    folium.Marker(current_pos, popup="あなた", icon=folium.Icon(color="blue")).add_to(m)
    
    # ジオフェンス範囲を円で描画
    folium.Circle(
        location=target_pos,
        radius=RADIUS_METERS,
        color="red",
        fill=True,
        fill_opacity=0.2,
        popup="ターゲットエリア"
    ).add_to(m)

    st_folium(m, width=700, height=500)

    # 自動更新
    import time
    time.sleep(5)
    st.rerun()

else:
    st.info("位置情報を取得中...")
