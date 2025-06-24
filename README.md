# 🧠 Brain Map API Server

A custom-built Flask API server that exposes RESTful endpoints to interact with a database of brain regions — built with clean architecture, frontend integration, automated testing, and readiness for DevOps adoption.

---

## 🚀 Phase 1 Summary

This marks the completion of **Phase 1** under an Agile, iterative workflow:

* ✅ API Design & Implementation
* ✅ SQLite Database Integration
* ✅ Unit Testing with Pytest
* ✅ Frontend UI for API interaction
* 🚧 Manual Testing via Postman
* 📦 DevOps-compatible structure (multi-branch Git, modular code)

---

## 📚 Project Structure

```
Brain_Map_API_Server/
│
├── app/                 # Flask app (routes, models)
├── tests/               # Pytest unit tests
├── frontend/            # HTML/JS/CSS frontend
├── .env                 # Environment config
├── requirements.txt     # Dependencies
├── run.py               # App entry point
└── README.md            # You’re here!
```

---

## 🌐 API Overview

| Endpoint        | Method | Description                 | Payload / Params    |
| --------------- | ------ | --------------------------- | ------------------- |
| `/regions/`     | GET    | Get all brain regions       | –                   |
| `/regions/<id>` | GET    | Get a specific region by ID | URL param `id`      |
| `/regions/`     | POST   | Create a new brain region   | JSON payload        |
| `/regions/<id>` | PUT    | Update an existing region   | JSON payload + `id` |
| `/regions/<id>` | DELETE | Delete a region             | URL param `id`      |

---

## 🧒 Sample API Usage

### ✅ GET All Regions

```bash
curl http://localhost:5000/regions/
```

### ✅ POST a Region

```bash
curl -X POST http://localhost:5000/regions/ \
  -H "Content-Type: application/json" \
  -d '{"name":"Amygdala","description":"Emotion center","function":"Detect fear"}'
```

### ✅ PUT (Update)

```bash
curl -X PUT http://localhost:5000/regions/1 \
  -H "Content-Type: application/json" \
  -d '{"name":"Updated Region","function":"Updated function"}'
```

---

## 🧑‍💻 How to Run the Server

### 1. 📦 Install dependencies

```bash
pip install -r requirements.txt
```

### 2. 🧪 Setup Database

```bash
python create_db.py
```

### 3. 🚀 Run the Flask app

```bash
python run.py
```

---

## 🌐 Frontend (Optional but Implemented)

### 🖥 Access UI via HTTP Server

From the `frontend/` directory:

```bash
python -m http.server 8000
```

Then visit: [http://localhost:8000](http://localhost:8000)

Interact with API via the buttons: **Get, Post, Update, Delete, Get by ID**

---

## ✅ API Testing (Phase 1)
  ✔️ Manual testing via Postman and browser
  ✔️ Automated testing using pytest

### 🧪 Pytest

Run all tests:

```bash
pytest
```

### 🔹 Tested Endpoints:

* `GET /regions/`
* `GET /regions/<id>`
* `POST /regions/`
* `PUT /regions/<id>`
* `DELETE /regions/<id>`

---

## ✅ Testing Overview (After Task 2)

📂 Tests organized into:
- `tests/unit_tests/` – Unit tests (mocking + non-mocking)
- `tests/integration_tests/` – End-to-end DB integration
- `tests/api_tests/` – Full API endpoint validation

📊 **Test Coverage: 94%**

✔️ Meets requirement of 70%+  
✔️ Pytest used with `pytest-cov`  
✔️ Mocking done via `unittest.mock`

📸 Coverage:
![coverage](<images/coverage.png>)

## 📦 DevOps Readiness

* ✅ Structured in feature-based Git branches
* ✅ Clear commit history and modular design
* ✅ Compatible with CI/CD pipeline integrations
* ✅ Tag created for Phase 1 submission
---

## 🔧 Tech Stack

* **Backend:** Flask, SQLAlchemy
* **Database:** SQLite (Phase 1)
* **Frontend:** HTML + JS + CSS
* **Testing:** Pytest + Postman
* **DevOps (Ready):** GitHub, `.env`, Keploy (phase 2)

---

## 🌟 Contribution Workflow (Agile Model)

This project followed an **Agile approach**:

1. Split into branches: `feature/get-all`, `feature/post-region`, `feature/frontend`, etc.
2. Each branch was tested, merged into `dev`
3. Final tested version merged to `main`
4. Tag created for Phase 1 completion

---

## 🔗 Repository

> 📌 [GitHub Link to Brain\_Map\_API\_Server](https://github.com/Maithili-Badhan/Brain_Map_API_Server)

---

## 🚧 Phase 2 (Planned)

* [ ] Integrate [Keploy](https://keploy.io) for record-replay API testing
* [ ] Add Docker support
* [ ] Deploy to a public cloud or localhost Docker container
* [ ] Switch to PostgreSQL

---

## 👏 Credits

Built by **Maithili Badhan** as part of the Keploy API Fellowship.
Exploring end-to-end API lifecycle with testing, frontend, and DevOps.
