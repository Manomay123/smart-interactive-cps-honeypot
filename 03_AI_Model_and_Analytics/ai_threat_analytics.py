import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt

data = [
    {"service": "Modbus/TCP", "payload_len": 45, "attack_type": "Modbus Protocol Manipulation", "label": 1, "mitre_id": "T0855 (Unauthorized Command Message)"},
    {"service": "MQTT", "payload_len": 12, "attack_type": "Unauthorized Connect", "label": 1, "mitre_id": "T0886 (Remote Services)"},
    {"service": "SSH", "payload_len": 128, "attack_type": "Brute Force", "label": 1, "mitre_id": "T0812 (Default Credentials)"},
    {"service": "HTTP", "payload_len": 210, "attack_type": "Command Injection", "label": 1, "mitre_id": "T0847 (Replication Through Removable Media / Exploit)"},
    {"service": "HTTP", "payload_len": 35, "attack_type": "Benign Scan", "label": 0, "mitre_id": "N/A"}
] * 40

df = pd.DataFrame(data)
df_encoded = pd.get_dummies(df[['service', 'payload_len']], drop_first=True)

X_train, X_test, y_train, y_test = train_test_split(df_encoded, df['label'], test_size=0.3, random_state=42)
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print("=== AI Model Evaluation Report ===")
print(classification_report(y_test, y_pred))

print("\n=== MITRE ATT&CK for ICS Mapping Report ===")
print(df[['service', 'attack_type', 'mitre_id']].drop_duplicates().to_string(index=False))

plt.figure(figsize=(8,4))
df['attack_type'].value_counts().plot(kind='bar', color='darkred')
plt.title('CPS Honeypot Threat Distribution')
plt.tight_layout()
plt.savefig("attack_distribution.png")
print("\n[+] Chart saved as attack_distribution.png")