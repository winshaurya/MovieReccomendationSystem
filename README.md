
# 🎬 Movie Recommendation System

[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-orange?logo=streamlit)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-DataFrame-green?logo=pandas)](https://pandas.pydata.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikitlearn)](https://scikit-learn.org/)
[![Deploy](https://img.shields.io/badge/Live%20App-Click%20Here-success?logo=streamlit&link=https%3A%2F%2Fmoviereccomendationsystem-9669.streamlit.app%2F)](https://moviereccomendationsystem-9669.streamlit.app/)

---

## 👋 About Me
Hi, I'm Shaurya — an aspiring data scientist and machine learning enthusiast. This is one of my favorite projects where I combined machine learning with a clean interactive UI to build a **content-based movie recommender**. It’s deployed live and ready to use!

---

## 🔍 What This Project Does

This project recommends similar movies based on the one you like.

✨ **Core Features:**
- Search for any movie from the dataset
- Get **Top 5 recommended movies** based on content similarity
- Display movie posters using TMDb API
- Streamlit web app for interactive use

Live Demo: [MovieReccomendationSystem Web App](https://moviereccomendationsystem-9669.streamlit.app/)

---

## 🧠 Tech Stack & Tools Used

| Tech | Description |
|------|-------------|
| ![Python](https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg) | Core programming language |
| ![Pandas](https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg) | Data wrangling and manipulation |
| ![Scikit-Learn]<img width="250" height="135" alt="image" src="https://github.com/user-attachments/assets/bee0de79-76cc-4816-a68c-52d0eef74a44" />
 | Used `CountVectorizer` and cosine similarity for ML logic |
| ![Streamlit](https://cdn.jsdelivr.net/gh/devicons/devicon/icons/streamlit/streamlit-original.svg) | Frontend UI for rapid web deployment |
| TMDb API | To fetch poster images for each movie |

---

## 📊 Recommendation Logic

The system is built using a **content-based filtering** approach:
1. **Text Feature Engineering**: Combine `genre`, `keywords`, `cast`, `crew`, and `overview` into a single "tag".
2. **Vectorization**: Convert text tags to numerical vectors using **CountVectorizer**.
3. **Similarity Calculation**: Use **cosine similarity** to find how similar two movies are.
4. **Ranking**: Return top 25 closest movies based on similarity.

---

## 🖼️ UI



| Home Page | 
|-----------|
|<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/873ea173-7b90-4143-be18-7262f58036a6" /> |

|Recommendations|
| <img width="1175" height="881" alt="image" src="https://github.com/user-attachments/assets/8abe2bd8-67df-412d-843b-260298be6242" /> |


---

## 📦 Installation

To run locally:

```bash
git clone https://github.com/winshaurya1/MovieReccomendationSystem.git
cd MovieReccomendationSystem
pip install -r requirements.txt
streamlit run app.py
```

---

## 🛰️ Deployed At

✅ [Streamlit - Click Here](https://moviereccomendationsystem-9669.streamlit.app/)  
No setup required. Just open the link and try the recommender!

---

## 📁 Project Structure

```
📦 MovieReccomendationSystem
 ┣ 📜 app.py                 # Streamlit frontend
 ┣ 📜 recommender.py        # ML logic (content filtering)
 ┣ 📜 movie_dict.pkl        # Preprocessed movie data
 ┣ 📜 similarity.pkl        # Precomputed cosine similarity matrix
 ┣ 📜 requirements.txt
 ┗ 📁 assets                # For screenshots
```

---

## 🧑‍💻 What I Learned

- Real-world application of **content-based filtering**
- Using **Scikit-Learn** to engineer features and calculate similarity
- Building fast **interactive UIs with Streamlit**
- Integrating APIs (TMDb) to enhance the user experience
- Deploying projects online for real use

---

## 🤝 Let's Connect

If you're interested in collaborating, giving feedback, or just talking about data science — feel free to reach out!

[![LinkedIn](https://img.shields.io/badge/LinkedIn-winShaurya-blue?logo=linkedin)](https://www.linkedin.com/in/shaurya-mishra-0b4751204/)  
[![GitHub](https://img.shields.io/badge/GitHub-winshaurya1-black?logo=github)](https://github.com/winshaurya1)

---

## 📜 License

This project is licensed under the **MIT License**. Use, modify, and share freely.
