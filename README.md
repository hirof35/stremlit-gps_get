
📍 ジオフェンス・アラートアプリ (Streamlit Geofence Alert)
Streamlit Geofence Alert は、ブラウザのGPS位置情報を利用して、特定のターゲット地点への接近をリアルタイムで監視・通知するWebアプリケーションです。

🌟 概要
「指定したエリアに近づいたら通知する」というジオフェンス機能を、複雑なネイティブアプリ開発なしで実現します。物流の拠点接近検知、位置情報ゲームのプロトタイプ、または特定エリアへの侵入アラートなど、幅広い用途に応用可能です。

✨ 特徴機能
リアルタイム位置情報取得:

streamlit_js_eval を利用し、ユーザーのデバイスから最新の緯度・経度を取得。

高精度な距離計算:

geopy の測地系計算アルゴリズムを採用。地球の曲率を考慮した、正確なメートル単位の距離判定を実現。

インタラクティブな地図表示:

folium を使用し、現在地とターゲットエリア（赤い円）を地図上に視覚化。

自動モニタリング:

5秒ごとの自動再実行（Rerun）ロジックを搭載。常に最新の状態を監視し続けます。

ステータス通知:

エリア内（st.error）とエリア外（st.success）をカラーテーマで分かりやすく通知。

🛠 技術スタック
Framework: Streamlit

Map Engine: folium / streamlit-folium

Geospatial: geopy (Distance calculation)

JS Bridge: streamlit_js_eval (Browser API integration)

🚀 クイックスタート
1. 依存ライブラリのインストール
Bash
pip install streamlit streamlit-folium streamlit-js-eval geopy folium
2. アプリの起動
Bash
streamlit run app.py
3. 位置情報の許可
ブラウザでアプリを開くと位置情報の共有を求められます。「許可」を選択してください。

⚙️ 設定のカスタマイズ
ソースコード内の以下の定数を変更することで、任意の場所をターゲットに設定できます。

Python
TARGET_LAT = 35.6812    # ターゲットの緯度
TARGET_LON = 139.7671   # ターゲットの経度
RADIUS_METERS = 100     # 通知を出す半径(m)
📜 ライセンス
MIT License

「ブラウザ一つで、地理空間をスマートに管理する。」
