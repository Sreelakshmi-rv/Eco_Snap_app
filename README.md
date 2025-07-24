# Eco_Snap_app

## Project Context
This application was developed as a core project for our **Digital Access for Community Empowerment (DACE) program**. The aim was to leverage modern data science and machine learning techniques to address real-world environmental challenges and promote sustainable practices.

## Overview
Eco_Snap is an innovative AI-powered mobile/web application designed to promote environmental sustainability and encourage eco-friendly habits among users. It leverages image recognition, data analytics, and gamification to help individuals and organizations track, analyze, and improve their environmental impact.

The application serves as a comprehensive platform for raising awareness, providing actionable insights, and fostering a community committed to a greener future.

## Objectives
The primary objectives of the Eco_Snap app are:
* To **raise awareness** about individual and collective environmental footprints.
* To **simplify the tracking** of eco-friendly actions and resource consumption (e.g., waste management, CO2 emissions).
* To **motivate behavioral change** towards more sustainable practices through gamification and personalized feedback.
* To **provide actionable insights** for both individuals and corporate entities (CSR) to reduce their environmental impact.
* To **demonstrate the practical application** of AI and data analytics in environmental conservation efforts.

## Application Flow (User Journey)
The typical user journey through the Eco_Snap app involves:

1.  **Image Capture:** Users take a photo using the "EcoSnap Camera" (`Ecosnap_camera.py`).
2.  **AI Analysis:** The captured image is analyzed by the "AI Analyzer" (`AI_analyzer.py`) to identify [**e.g., "types of waste," "recycled items," "carbon-intensive objects"**].
3.  **Impact Estimation:** Based on the AI analysis, the "CO2 Estimator" (`Co2_estimator.py`) calculates the environmental impact (e.g., estimated CO2 emissions/savings).
4.  **Personal Tracking:** The user's actions and their associated impact are recorded and reflected in their "Personal Dashboard" (`Personal_dashboard.py`) and contribute to the "Streak Tracker" (`Streak_tracker.py`).
5.  **Motivation & Engagement:** Users can view their progress, compete on "Leaderboards" (`Leaderboards.py`), and earn rewards through the "Reward Center" (`Reward_center.py`).
6.  **Corporate Insights (for CSR):** For organizations, the "CSR Dashboard" (`CSR_dashboard.py`) aggregates data to provide a holistic view of their collective environmental efforts.

## Impact
Eco_Snap aims to create a significant impact by:
* **Empowering Individuals:** Giving users a clear understanding of their daily environmental choices and their cumulative effect.
* **Fostering Sustainable Habits:** Through consistent tracking and gamified incentives, the app encourages the adoption of long-term eco-friendly behaviors.
* **Supporting Corporate Responsibility:** Providing companies with tools to monitor and report on their environmental initiatives, promoting transparency and accountability.
* **Data-Driven Insights:** Generating valuable data on consumption patterns and environmental trends, which can inform policy or further research.
* **Community Building:** Connecting like-minded individuals and organizations in their shared goal of environmental protection.

## Key Features
* **EcoSnap Camera & AI Analyzer (`Ecosnap_camera.py`, `AI_analyzer.py`, `model_training.py`):**
    * Utilizes a camera interface to capture images.
    * Integrates an AI model (trained via `model_training.py` using `class_labels.txt`) to analyze images for [**specify what the AI identifies, e.g., "waste types (recyclable, non-recyclable)," "sustainable products," "carbon-intensive items"**].
    * Provides instant feedback on the environmental implications of the photographed items/actions.
* **CO2 Estimator (`Co2_estimator.py`):**
    * Calculates estimated CO2 emissions or savings based on user actions or identified items.
    * Helps users visualize their carbon footprint in a tangible way.
* **Personal Dashboard (`Personal_dashboard.py`):**
    * Offers a personalized view of a user's eco-activities.
    * Displays individual progress, statistics, and impact over time.
    * [**Mention specific metrics shown, e.g., "total CO2 saved," "number of items recycled," "streak of sustainable actions"**].
* **CSR Dashboard (`CSR_dashboard.py`):**
    * Provides an overview for corporate social responsibility (CSR) initiatives.
    * Aggregates data from multiple users/teams to show collective environmental impact.
    * [**Specify what corporate users might see, e.g., "company-wide carbon reduction," "team leaderboard"**].
* **Leaderboards (`Leaderboards.py`):**
    * Fosters healthy competition among users or teams based on their eco-contributions.
    * Showcases top performers and encourages greater participation.
* **Reward Center (`Reward_center.py`):**
    * Motivates users through a system of rewards or badges for achieving eco-milestones.
    * [**Describe types of rewards, e.g., "virtual badges," "points," "discounts from eco-partners"**].
* **Streak Tracker (`Streak_tracker.py`):**
    * Helps users maintain consistent eco-friendly behavior by tracking consecutive days of positive actions.
    * Encourages habit formation.

## Technologies Used
* **Python:** The core programming language for the entire application.
* **Streamlit:** For building the interactive web user interface and dashboards.
* **TensorFlow / Keras:** (Likely for `model_training.py` and `AI_analyzer.py`) For developing and deploying the AI/image classification model.
* **OpenCV (Likely):** For camera integration and image processing.
* **Pandas / NumPy:** For data manipulation and analysis across dashboards and estimators.
* **Other Libraries:** (e.g., Matplotlib/Seaborn for visualization, requests for API calls, specific database connectors if applicable).

## How to Run Locally
To set up and run this application on your local machine:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Sreelakshmi-rv/Eco_Snap_app.git](https://github.com/Sreelakshmi-rv/Eco_Snap_app.git)
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd Eco_Snap_app
    ```
3.  **Install necessary libraries:**
    * It's highly recommended to use a virtual environment.
    * ```bash
        python -m venv venv
        # On Windows:
        .\venv\Scripts\activate
        # On macOS/Linux:
        source venv/bin/activate
        ```
    * Install dependencies (adjust `tensorflow` version if needed based on your local Python):
        ```bash
        pip install -r requirements.txt
        ```
4.  **Ensure Model and Data are Present:**
    * If your AI model and any necessary datasets (e.g., for `model_training.py`) are not committed to the repo, place them in the correct subdirectories as expected by `app.py`.
5.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```
    This will open the application in your web browser, typically at `http://localhost:8501`.

## Deployment
This application is designed for deployment using Streamlit Cloud.
* **Live Demo:** [https://ecosnapapp-3uippp2u6pxdcmappck545.streamlit.app/](https://ecosnapapp-3uippp2u6pxdcmappck545.streamlit.app/)
* **Important:** When deploying to Streamlit Cloud, ensure you select a compatible Python version (e.g., **Python 3.9, 3.10, or 3.11**) as TensorFlow might not have wheels for very new Python versions like 3.13.

## Future Enhancements
* **Expand AI Capabilities:** Incorporate more sophisticated image recognition models for wider range of item identification and more nuanced analysis.
* **Database Integration:** Implement a robust database (e.g., SQL, NoSQL) for scalable user management, data storage, and performance tracking.
* **Mobile Responsiveness:** Optimize the Streamlit application for seamless use on mobile devices.
* **Notifications & Reminders:** Add features for push notifications or in-app reminders to encourage consistent eco-friendly actions.
* **Advanced Analytics:** Introduce more complex data analytics features for deeper insights into environmental impact trends.
