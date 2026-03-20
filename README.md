# Random Forest Prediction Deployment

This project contains everything needed to serve your Random Forest Regressor online with a gorgeous, dynamic Glassmorphism UI.

## File Breakdown
- `train.py`: Script to train the random forest regressor and save it as `model.pkl`.
- `app.py`: The FastAPI application server.
- `requirements.txt`: Python package dependencies.
- `Procfile`: Command used by cloud providers to start your server.
- `static/`: Contains the dynamic frontend UI (`index.html`, `style.css`, `script.js`).

---

## 🚀 How to Deploy to the Web (Free & Easy)

Since Python is not installed on your local machine, the best way to deploy this and see it live is to use a free cloud provider like **Render** or **Heroku**.

### Option A: Deploying on Render (Recommended, Free)

1. **Upload Code to GitHub**: 
   - Create a new free repository on [GitHub](https://github.com/).
   - Upload all the files in this folder (or use Git to push them to your repository).
   
2. **Deploy on Render**:
   - Go to [Render.com](https://render.com/) and sign in with your GitHub account.
   - Click **New +** and select **Web Service**.
   - Connect the repository you just created.
   - Set the following configuration:
     - **Environment**: `Python`
     - **Build Command**: `pip install -r requirements.txt && python train.py`
     - **Start Command**: `uvicorn app:app --host 0.0.0.0 --port $PORT`
   - Click **Create Web Service**. 
   - Render will automatically build the model using `train.py` and assign you a live, public URL containing your new premium app!

### Option B: Deploying on Heroku

1. Create a free account on [Heroku](https://heroku.com/).
2. Push your code to GitHub.
3. In Heroku, create a "New App", connect your GitHub repo, and click "Deploy". Heroku will run the Procfile and dependencies automatically.

----

## 💻 How to Run Locally (If you install Python later)

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Train the model:**
   ```bash
   python train.py
   ```
   *(This ensures `model.pkl` is saved correctly).*

3. **Start the API Server:**
   ```bash
   uvicorn app:app --reload
   ```

4. **View the live app:**
   Open your browser to `http://localhost:8000/` and you will be greeted by the new UI.
