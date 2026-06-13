import streamlit as st
import pandas as pd
import joblib

# Setup Halaman
st.set_page_config(page_title="Telco Churn Prediction", page_icon="🌐", layout="wide")

# Header
st.title("🌐 TELCO CHURN PREDICTION DASHBOARD")
st.markdown("---")

# Sidebar untuk Input
st.sidebar.header("⚙️ PANEL INPUT DATA")

gender = st.sidebar.selectbox("👤 Gender", ["Male", "Female"])
tenure = st.sidebar.slider("⏳ Lama Berlangganan (Bulan)", min_value=1, max_value=72, value=30)
internet = st.sidebar.radio("📶 Layanan Internet", ["DSL", "Fiber Optic", "No"])
charges = st.sidebar.number_input("💳 Biaya Bulanan ($)", min_value=0.0, value=85.50, step=0.5)

predict_btn = st.sidebar.button("🔍 PREDIKSI SEKARANG")

# Main Area
st.subheader("📊 HASIL ANALISIS & PREDIKSI")

if predict_btn:
    try:
        # Load model dan scaler
        model = joblib.load('churn_model.pkl')
        scaler = joblib.load('scaler.pkl')

        # Manual Encoding untuk mengubah teks dropdown menjadi angka yang dipahami model
        g_encoded = 1 if gender == "Male" else 0
        
        if internet == "DSL":
            i_encoded = 0
        elif internet == "Fiber Optic":
            i_encoded = 1
        else:
            i_encoded = 2
            
        # Bentuk DataFrame input
        input_df = pd.DataFrame(
            [[g_encoded, int(tenure), i_encoded, float(charges)]], 
            columns=['Gender', 'Tenure', 'InternetService', 'MonthlyCharges']
        )
        
        # Scale input
        input_scaled = scaler.transform(input_df)
        
        # Prediksi
        prediction = model.predict(input_scaled)
        
        # Tampilan Hasil SANGAT BESAR DAN JELAS
        if prediction[0] == 1: # 1 = Yes (Churn)
            st.markdown(
                """
                <div style="background-color:#ffeaea;padding:40px;border-radius:10px;text-align:center;border:3px solid #ff4b4b;">
                    <h1 style="color:#ff4b4b;font-size:70px;margin:0;font-weight:900;">🚨 CHURN</h1>
                    <h2 style="color:#ff4b4b;margin-top:10px;">(BERPOTENSI BERHENTI)</h2>
                </div>
                """, 
                unsafe_allow_html=True
            )
            pesan = "💡 **Rekomendasi:** Pelanggan ini berisiko tinggi untuk beralih. Segera tawarkan promo retensi atau diskon tagihan."
        else: # 0 = No (Loyal)
            st.markdown(
                """
                <div style="background-color:#eaffea;padding:40px;border-radius:10px;text-align:center;border:3px solid #00c04b;">
                    <h1 style="color:#00c04b;font-size:70px;margin:0;font-weight:900;">✅ LOYAL</h1>
                    <h2 style="color:#00c04b;margin-top:10px;">(TETAP BERLANGGANAN)</h2>
                </div>
                """, 
                unsafe_allow_html=True
            )
            pesan = "💡 **Rekomendasi:** Pelanggan dalam kondisi aman. Tidak perlu intervensi khusus, pertahankan kualitas layanan."

        st.markdown("<br>", unsafe_allow_html=True)
        
        # Ringkasan Profil
        st.markdown("### 📝 RINGKASAN PROFIL:")
        col1, col2, col3, col4 = st.columns(4)
        col1.info(f"**Gender:** {gender}")
        col2.info(f"**Tenure:** {tenure} Bulan")
        col3.info(f"**Internet:** {internet}")
        col4.info(f"**Tagihan:** ${charges:.2f}")
        
        st.warning(pesan)

    except FileNotFoundError:
        st.error("❌ File model tidak ditemukan. Pastikan 'churn_model.pkl' dan 'scaler.pkl' ada di folder yang sama dengan app.py!")
    except Exception as e:
        st.error(f"❌ Terjadi kesalahan: {e}")
else:
    st.info("Silakan atur data di panel sebelah kiri dan klik tombol **🔍 PREDIKSI SEKARANG** untuk melihat hasil.")