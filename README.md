# 🎬 Movie Recommender System

A content-based movie recommendation web application built using Streamlit.
The app recommends similar movies based on a selected title and displays movie posters using the The Movie Database API.

---

## 🚀 Features

* 🎥 Recommend movies similar to a selected movie
* 🖼️ Display movie posters alongside recommendations
* ⚡ Fast recommendations using pre-trained similarity matrices
* 🌐 Interactive and user-friendly web interface with Streamlit
* 📦 Lightweight and easy to run locally

---

## 🛠️ Tech Stack

* **Python**
* Streamlit
* Pandas
* NumPy
* Requests
* Pickle
* The Movie Database API

---

# 📂 Project Structure

```bash
Movie-Recommender-System/
│
├── app.py                  # Main Streamlit application
├── moviesdict.pkl          # Movie dataset
├── similarity1.pkl         # Similarity matrix file
├── similarity2.pkl         # Additional similarity matrix
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone <your-repository-url>
cd Movie-Recommender-System
```

---

## 2️⃣ Install Dependencies

```bash
pip install streamlit pandas requests numpy
```

Or install using:

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Add Required Files

Ensure the following files are present in the project directory:

* `moviesdict.pkl`
* `similarity1.pkl`
* `similarity2.pkl`

These files contain the movie dataset and pre-trained similarity matrices used for generating recommendations.

---

# ▶️ Usage

Run the Streamlit application:

```bash
streamlit run app.py
```

After running the command, open the local URL provided in the terminal (usually `http://localhost:8501`) in your browser.

---

# 🎯 How It Works

1. The user selects a movie from the dropdown menu.
2. The recommendation engine finds similar movies using pre-trained similarity matrices.
3. Movie posters are fetched dynamically from the TMDb API.
4. Recommended movies are displayed with their posters in the web interface.

---

# 🔑 TMDb API Integration

This project uses the The Movie Database API to fetch movie posters.

You can get your API key from:

[TMDb Official Website](https://www.themoviedb.org/?utm_source=chatgpt.com)

Replace the API key in `app.py` with your own key if required.

---

# 📸 Application Preview

## Movie Selection Interface

![Image](https://images.openai.com/static-rsc-4/c8EClW7rDbB_9nhCcN6eRjs744JONtVZONXRSTz0MucsaqTm9322IbACr-IlrDjyhOCgDHXE3mxjIiNy5vkGTB0EC5XUuEnGhTpqtVmMBsf0qgv68yiXYICsVtJSntXbwlo3ndhNP8ki8t3sgixNeBqoEczChqYAofg7HlQD34iAKjq8kuDyD9UeYNrq7o9d?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/82liD42ASnkZj3d1PyptAV1goVQNezkXj8f3buNyeRpImhVt0graESMRV56zi_0R8Nn1WTtk0ugr_nZM13qsOw-rDrY_vhIVYhd992eRLP1XNg7IUch6nUSLh47oaVhiQaMUU8Z_Ee7lP60_ecywhmJxbVea7bIJLOfRaBNy_kJF6vbfdZvtFNSubOfSf4cg?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/VHbGeqsW6-3g34Ooer1vQI7qRFylJEjJHJz2TcHy5_6MPthMBh0JVpcIe_clMU1sxIRYfIq3UE4iDYHSZBoejdBOloRHc9xPYHMOAu3UkD8LK2edx8r4j6lKLgTABg87AsNEW3y9Q8hghQHzQOeiXCvPMB5xpbf1AbYtMuzVi_-MotPWxtY05WVY5QjTac9L?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/dlvMre2R1BqUZ5JnVOUup-Z7bkJuVMp_x2tk5zFTBkCU-0ToYpVjjWMgCaE8V79aHouzEYdRZ9fRHahSHcP3tXSRoyc7baHkoJyK76OtsFRwC92mfk9yEFUeJNbPGcgqF5P0ONAmqrwg9KS4YPLx7fvtazCooiFUXdV6ymt7jw_8gAckpIsykLn2ONs1TcVA?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/ySyFeAcf8KPaFaUJPxyLZNVr7jBpZEgZnvmrIofnXT_9nZTwkHx9g6p00IvC0B9J6Oh78bsOdtpf9lee-aYoXdTCHK04wYGL6s18N0zs94yHBw9nHZCX5xn4STP_JYpJhdneJerN8wnoDdekaVCgLQCISd8tE-d7bWUR-V_D01CmwE7_l35Hh4CkhghSnh19?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/OjFd9AO36szWK0gjBlsmkXB08Bw1T2n4AaQcnthb4d6EOl6s6II1t9xCvfKmCy5hG3nSxSg5oItuJx3aqUp5F3YbCH4j9E5ZW1vvsLs3e21lybHOrKwztcVIQ1el4tz8eamGALFEwOpGJBVbplJVrtEbBwsIKBVu8RncJD-Z50EHnPPDG4DM93gbON6fL8Qy?purpose=fullsize)

---

# 📦 Requirements

* Python 3.6+
* Streamlit
* Pandas
* NumPy
* Requests

---

# 🙌 Acknowledgements

* Streamlit
* Pandas
* NumPy
* The Movie Database API

---


# 👨‍💻 Author

Developed by **Dishant Singh** 🚀
