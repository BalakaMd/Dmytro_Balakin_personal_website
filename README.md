# Dmytro_Balakin_personal_website

---

This repository contains the source code for a simple Flask web application that serves as a portfolio website. The website includes a home page and a download page for a resume file. The application is built using the Flask web framework and utilizes Flask-Bootstrap for improved design and layout.

## Features:

1. **Home Page**: The root route of the application (`'/'`) serves a home page, which is rendered using an HTML template (`index.html`). This page can be customized to display information about you, your skills, and any other content you'd like to share with visitors.

2. **Download Button**: After the section "CURRICULUM VITAE" at the bottom right of the section there is a button to download the CV. Also the `/download` route allows users to download resume. The resume file (`Dmytro_Balakin_-_Junior_Python_Developer.pdf`) is served as an attachment, making it easy for users to download.

## Getting Started:

To run this application locally, follow these steps:

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/Dmytro_Balakin_personal_website.git
   ```

2. Install the required dependencies by running:

   ```
   pip install -r requirements.txt
   ```

3. Run the Flask application:

   ```
   python app.py
   ```

4. Open a web browser and navigate to `http://localhost:5000` to view your portfolio website.

## Dependencies:

- Flask: A lightweight and flexible Python web framework.
- Flask-Bootstrap: An extension for Flask that provides Bootstrap integration for better website styling.

## Customization:

- **Homepage Content**: To customize the content of the home page, edit the `index.html` template located in the `templates` directory.

- **Resume File**: Replace the existing resume file (`Dmytro_Balakin_-_Junior_Python_Developer.pdf`) in the `static` directory with your own resume in PDF format.

- **Styling**: You can further customize the website's styling by modifying the HTML and CSS in the `templates` and `static` directories.

## Deployment:

You can deploy this Flask application to a hosting platform of your choice to make your portfolio website accessible to a wider audience.

---
