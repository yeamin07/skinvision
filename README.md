# 🩺 SkinVision

**AI-Powered Skin Disease Detection Using CNNs with a Treatment Recommendation System**

SkinVision is a full-stack web application that lets a user upload a photo of a skin condition and receive an AI-generated prediction. The model is an **EfficientNet-B0** CNN (transfer learning) served through a **Django REST Framework** backend, with a React frontend. For each prediction the app returns the top matching diseases with confidence scores, plus treatment and prevention recommendations.

> ⚠️ **Medical disclaimer:** SkinVision is an academic capstone project built for educational purposes. It is **not** a medical device and must **not** be used as a substitute for professional diagnosis or treatment. Always consult a qualified dermatologist.

---

## ✨ Features

- Upload a skin image and get an instant prediction
- Top-3 predictions with confidence scores
- Treatment and prevention recommendations for the predicted condition
- EfficientNet-B0 transfer-learning model with a custom classification head
- REST API backend (Django REST Framework)
- Runs fully locally: no external APIs, no cloud database, no `.env` file required

---

## 🧰 Tech Stack

| Layer | Technology |
|---|---|
| Model | EfficientNet-B0, Keras |
| Hyperparameter tuning | Optuna (TPE sampler + Hyperband pruner) |
| Backend | Python, Django, Django REST Framework |
| Database | SQLite (`db.sqlite3`, bundled with Django) |
| Frontend | JavaScript, Node.js / npm |

---

## 🔄 How It Works

```
User uploads image
        │
        ▼
Preprocessing (resize to 224×224, EfficientNet preprocess_input)
        │
        ▼
EfficientNet-B0 prediction (top-3 classes + confidence)
        │
        ▼
Treatment / prevention recommendation lookup
        │
        ▼
JSON response → displayed in the frontend
```

---

## 📁 Project Structure

```
skinvision/
├── skinvision_backend/
│   ├── diagnosis/          # Diagnosis app (views, models, recommendations)
│   ├── ml_model/           # Trained model + metadata used for inference
│   ├── skinvision_api/     # Django project settings and URL config
│   ├── skin_venv/          # Python virtual environment (local only)
│   ├── db.sqlite3          # SQLite database
│   ├── manage.py
│   └── requirements.txt
├── skinvision-frontend/
│   ├── public/
│   ├── src/
│   ├── package.json
│   └── README.md
└── .gitignore
```

---

## ✅ Prerequisites

Install the following before you begin:

| Tool | Recommended version | Check with |
|---|---|---|
| Git | any recent | `git --version` |
| Python | 3.10 or 3.11 (TensorFlow supports 3.9–3.12) | `python --version` |
| Node.js + npm | Node 18 or newer | `node -v` and `npm -v` |

---

## 🚀 Running the Project Locally

You will need **two terminals**: one for the backend and one for the frontend.

### 1. Clone the repository

```bash
git clone https://github.com/yeamin07/skinvision.git
cd skinvision
```

### 2. Set up and start the backend

```bash
cd skinvision_backend
```

**Create a virtual environment**

```bash
# Windows
python -m venv skin_venv

# macOS / Linux
python3 -m venv skin_venv
```

**Activate it**

```bash
# Windows (Command Prompt)
skin_venv\Scripts\activate

# Windows (PowerShell)
skin_venv\Scripts\Activate.ps1

# macOS / Linux
source skin_venv/bin/activate
```

**Install dependencies**

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

> The first install can take several minutes because TensorFlow is a large package.


**Start the Django server**

```bash
python manage.py runserver
```

The backend is now running at **http://127.0.0.1:8000/**.


### 3. Set up and start the frontend

Open a **new terminal** from the project root:

```bash
cd skinvision-frontend
npm install
npm start
```

> If your frontend was created with Vite, use `npm run dev` instead of `npm start`.

The frontend opens at **http://localhost:3000/** (or the port shown in your terminal).

### 4. Use the app

1. Make sure both servers are running.
2. Open the frontend URL in your browser.
3. Upload a clear, well-lit photo of the affected skin area.
4. View the predicted condition, confidence score, and treatment/prevention recommendations.

---

## 🛠️ Troubleshooting

| Problem | Fix |
|---|---|
| `pip install` fails on TensorFlow | Use Python 3.10 or 3.11 and make sure `pip` is up to date. |
| `ModuleNotFoundError` when starting Django | The virtual environment is not active. Re-run the activate command. |
| PowerShell blocks `Activate.ps1` | Run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, or use Command Prompt. |
| Frontend cannot reach the backend (CORS error) | Ensure the backend is running on port 8000 and that CORS is configured for the frontend origin (e.g. `django-cors-headers`). |
| `Port 8000 is already in use` | Run `python manage.py runserver 8080` and update the API URL in the frontend. |
| Model file not found | Confirm the trained model and metadata files exist inside `skinvision_backend/ml_model/`. |
| `npm install` errors | Delete `node_modules` and `package-lock.json`, then run `npm install` again. |

---

## 🧠 Model Overview

- **Backbone:** EfficientNet-B0 pretrained on ImageNet
- **Head:** GlobalAveragePooling → BatchNorm → Dense → BatchNorm → ReLU → Dropout → Dense → BatchNorm → ReLU → Dropout → Softmax
- **Training:** two phases. Phase 1 trains with a frozen backbone; Phase 2 fine-tunes the top 30 layers
- **Regularization:** label smoothing (0.1), class-weight balancing, dropout, L2
- **Callbacks:** EarlyStopping, ReduceLROnPlateau, ModelCheckpoint
- **Tuning:** Optuna (TPESampler + HyperbandPruner)
- **Data:** Kaggle skin disease dataset filtered to ~15 classes, augmented to 1,200 images per class at 224×224
- **Output:** top-3 predictions with confidence scores

---


---

## 👤 Author

**Walid Been Shahid(yeamin)**
GitHub: [@yeamin07](https://github.com/yeamin07)
Repository: [github.com/yeamin07/skinvision](https://github.com/yeamin07/skinvision)

⭐ If you found this project helpful, consider giving it a star!
