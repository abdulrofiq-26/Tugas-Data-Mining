import numpy as np
import pandas as pd
import warnings
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

# Menyembunyikan warning bawaan library agar tampilan CMD bersih
warnings.filterwarnings('ignore')

# =====================================================================
# TAHAPAN 1: DATA PREPARATION (Dengan Korelasi Pola Logis)
# =====================================================================
print("=== TAHAPAN 1: DATA PREPARATION ===")

np.random.seed(42)
n_samples = 1000

# Generate fitur dasar
Gender = np.random.choice(['Male', 'Female'], n_samples)
Tenure = np.random.randint(1, 72, n_samples)
InternetService = np.random.choice(['DSL', 'Fiber Optic', 'No'], n_samples)
MonthlyCharges = np.random.uniform(20.0, 120.0, n_samples)

# MEMBUAT POLA LOGIS: Biaya tinggi & Baru berlangganan = Lebih rentan Churn
churn_score = (MonthlyCharges * 0.5) - (Tenure * 1.2)
churn_score += np.where(InternetService == 'Fiber Optic', 15, 0)

# Menentukan label Churn berdasarkan nilai ambang batas (threshold) median
threshold = np.median(churn_score)
Churn = np.where(churn_score > threshold, 'Yes', 'No')

data = {
    'CustomerID': [f'USR-{i}' for i in range(1000, 1000 + n_samples)],
    'Gender': Gender,
    'Tenure': Tenure,
    'InternetService': InternetService,
    'MonthlyCharges': MonthlyCharges,
    'Churn': Churn
}
df = pd.DataFrame(data)

# Menambahkan sedikit missing values buatan untuk demonstrasi cleansing

# Simpan data sintetis ke CSV untuk visualisasi interaktif
df.to_csv('customer_data.csv', index=False)
df.loc[df.sample(frac=0.02).index, 'MonthlyCharges'] = np.nan
print(f"Jumlah missing values sebelum cleansing:\n{df.isnull().sum()}\n")

# Penanganan missing values
mean_charges = df['MonthlyCharges'].mean()
df['MonthlyCharges'] = df['MonthlyCharges'].fillna(mean_charges)
print("Missing values berhasil ditangani.")

# Transformasi Data
le_gender = LabelEncoder()
le_internet = LabelEncoder()
le_churn = LabelEncoder()

df['Gender'] = le_gender.fit_transform(df['Gender'])
df['InternetService'] = le_internet.fit_transform(df['InternetService'])
df['Churn'] = le_churn.fit_transform(df['Churn'])

X = df[['Gender', 'Tenure', 'InternetService', 'MonthlyCharges']]
y = df['Churn']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
print("Transformasi data dan scaling selesai dilakukan.\n")

# =====================================================================
# TAHAPAN 2 & 3: MODELLING & EVALUATION
# =====================================================================
print("=== TAHAPAN 2 & 3: MODELLING & EVALUATION ===")

# Menggunakan Decision Tree dengan pola yang sudah terbentuk
model = DecisionTreeClassifier(max_depth=4, random_state=42)
model.fit(X_train_scaled, y_train)
print("Model Decision Tree berhasil dilatih.")

y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
print(f"Akurasi Model: {accuracy * 100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=['No Churn', 'Churn']))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# =====================================================================
# TAHAPAN 4: DEPLOYMENT (CMD INTERACTIVE TEST)
# =====================================================================
joblib.dump(model, 'churn_model.pkl')
joblib.dump(scaler, 'scaler.pkl')

print("\n=== TAHAPAN 4: DEPLOYMENT (CMD INTERACTIVE TEST) ===")
print("Model siap digunakan secara real-time via CMD.")

def run_cmd_deployment():
    loaded_model = joblib.load('churn_model.pkl')
    loaded_scaler = joblib.load('scaler.pkl')
    
    print("\n" + "="*55)
    print("     S I S T E M   P R E D I K S I   C H U R N     ")
    print("                 P E L A N G G A N                 ")
    print("="*55)
    
    while True:
        try:
            print("\nSilahkan masukkan data pelanggan baru")
            print("(atau ketik 'exit' untuk keluar)\n")
            
            # Tambahan .strip() untuk membersihkan spasi berlebih otomatis
            gender_input = input("Gender (Male/Female)                  : ").strip()
            if gender_input.lower() == 'exit': break
                
            tenure_input = input("Tenure / Lama Berlangganan (Bulan)    : ").strip()
            internet_input = input("Internet Service (DSL/Fiber Optic/No) : ").strip()
            charges_input = input("Biaya Bulanan ($)                     : ").strip()
            
            # Transformasi data
            g_encoded = le_gender.transform([gender_input])[0]
            i_encoded = le_internet.transform([internet_input])[0]
            t_val = int(tenure_input)
            c_val = float(charges_input)
            
            input_df = pd.DataFrame(
                [[g_encoded, t_val, i_encoded, c_val]], 
                columns=['Gender', 'Tenure', 'InternetService', 'MonthlyCharges']
            )
            input_scaled = loaded_scaler.transform(input_df)
            
            prediction = loaded_model.predict(input_scaled)
            prediction_label = le_churn.inverse_transform(prediction)[0]
            
            print("\n" + "-"*55)
            if prediction_label == 'Yes':
                print(" >>> HASIL PREDIKSI: CHURN (BERPOTENSI BERHENTI) <<< ")
            else:
                print(" >>> HASIL PREDIKSI: LOYAL (TETAP BERLANGGANAN)  <<< ")
            print("-"  * 55)
            
        except Exception as e:
            print(f"\n[Error] Input tidak valid. Pastikan opsi diketik persis sesuai pilihan dan gunakan titik (.) untuk desimal.")

# Jalankan fungsinya
run_cmd_deployment()