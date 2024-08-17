# CO2 Transport Calculator Example

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=flat&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=flat&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=flat&logo=Matplotlib&logoColor=black)
![Seaborn](https://img.shields.io/badge/seaborn-%23e6b91e.svg?style=flat&logo=seaborn&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=flat&logo=scikit-learn&logoColor=white)
![Flask](https://img.shields.io/badge/flask-2.0%2B-orange)
![Pandas](https://img.shields.io/badge/pandas-1.3%2B-brightgreen)
![Matplotlib](https://img.shields.io/badge/matplotlib-3.4%2B-yellow)
![HTML](https://img.shields.io/badge/HTML-5-red)
![CSS](https://img.shields.io/badge/CSS-3-blueviolet)
![Jinja2](https://img.shields.io/badge/jinja2-3.0%2B-green)
![License](https://img.shields.io/badge/license-MIT-green)

## Description
This project is a simple (currently) web application that calculates carbon dioxide (CO2) emissions from various modes of transport based on a specified distance. Users can enter a distance in kilometers, and the application displays the total CO2 emissions for different transport modes, including cars, buses, trains, and more. The results are presented both in tabular form and as a graph.

## PythonAnywhere Deployment
The first version of this program is currently hosted on PythonAnywhere and can be accessed at the following address: http://wartem.pythonanywhere.com. Please note that this deployment is intended for demonstration purposes and may be deactivated or moved at a later date.
A version of this program can also be viewed here: http://wartem.xyz

## Features
- User-friendly interface for entering distance.
- Calculation of CO2 emissions for various transport modes.
- Visualization of results using charts.
- Responsive design to work on different devices.

## Technologies
- **Python**: For backend logic and calculations.
- **Flask**: For building the web application.
- **Jinja2**: For templating and rendering dynamic content in HTML.
- **Pandas**: For handling and analyzing data.
- **Matplotlib**: For creating graphs and visualizations.
- **HTML**: For structuring the frontend content.
- **CSS**: For styling the frontend design.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/Wartem/co2_transport_calculator_example.git

## How It Works

This Flask application calculates and visualizes CO2 emissions for different modes of transport based on a user-input distance. Here's an overview of its structure and functionality:

### Project Structure
```your_project/
│
├── app.py
├── routes.py
├── templates/
│ ├── index.html
│ └── result.html
├── carbon-footprint-travel-mode.csv
└── requirements.txt```

### Key Components

1. **app.py**: 
   - Initializes the Flask application
   - Loads the CSV data containing emission information
   - Serves as the entry point for running the application

2. **routes.py**:
   - Defines the URL routes and their corresponding functions
   - Handles user requests and form submissions
   - Processes data and generates visualizations

3. **templates/**:
   - Contains HTML templates for rendering pages
   - `index.html`: The form for distance input
   - `result.html`: Displays the calculation results and visualization

### How It's Connected

1. `app.py` creates the Flask application instance and loads the necessary data.
2. It then imports all routes from `routes.py`.
3. `routes.py` uses the app instance and data from `app.py` to define how the application responds to different URLs.
4. When a user accesses the root URL:
   - They see a form (rendered from `index.html`) to input distance.
   - Upon form submission, the application calculates emissions, generates a plot, and displays results using `result.html`.

### Data Flow

1. User inputs distance on the home page.
2. Flask processes the form submission in the `index()` function in `routes.py`.
3. The function calculates emissions, creates a visualization, and renders the results.
4. The user sees the rendered `result.html` page with the emissions data and plot.

This structure separates concerns, making the code modular and easier to maintain. The application logic is in `routes.py`, while `app.py` handles setup and serves as the entry point.

## Data
The data used in this project comes from OurWordData in the form of a CSV file from 2022. [[carbon-footprint-travel-mode.csv](https://github.com/user-attachments/files/16403775/carbon-footprint-travel-mode.csv)](https://ourworldindata.org/grapher/carbon-footprint-travel-mode)

## First Version
This is the first simple version of the application. There are many opportunities for future improvements, including:
More transport modes and detailed data.
Use of external APIs to fetch updated data.
Enhanced user interface and user experience.

## Acknowledgments
This project was developed with the assistance of Perplexity (and Claude), an innovative AI tool that greatly facilitated the research and development process. Perplexity helped streamline the gathering of information and provided valuable insights into the structure and functionality of the application. By leveraging its capabilities, I was able to quickly access relevant data, explore various transport modes, and efficiently calculate CO2 emissions based on user input.
Using Perplexity allowed me to focus on the creative aspects of the project while ensuring that the technical details were accurate and well-informed. The AI's ability to summarize complex information and suggest relevant topics significantly enhanced the overall development experience. This collaboration exemplifies how AI tools can be effectively integrated into the software development process, making it easier to create functional and user-friendly applications.

## License
This project is licensed under the MIT License.
