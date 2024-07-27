import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, send_file
from io import BytesIO
import base64

app = Flask(__name__)

# Läs in CSV-filen
file_path = 'data-och-statistik-klimat-vaxthusgaser-utslapp-fran-inrikes-transporter-.csv'
df = pd.read_csv(file_path)

# Välj den senaste året för analys (2023 i detta fall)
latest_year_data = df.iloc[-1]

# Skapa en ny DataFrame med transportmedel och deras CO2-utsläpp
transport_data = {
    'transportmedel': ['A-traktorer', 'Järnväg', 'Mopeder och motorcyklar', 'Bussar', 'Flyg', 'Sjöfart', 'Lätta lastbilar', 'Tunga lastbilar', 'Personbilar'],
    'co2_per_km': [latest_year_data['A-traktorer'], latest_year_data['Järnväg'], latest_year_data['Mopeder och motorcyklar'], latest_year_data['Bussar'], latest_year_data['Flyg'], latest_year_data['Sjöfart'], latest_year_data['Lätta lastbilar'], latest_year_data['Tunga lastbilar'], latest_year_data['Personbilar']]
}

transport_df = pd.DataFrame(transport_data)

def calculate_total_emissions(df, distance_km):
    df = df.copy()
    df['total_emissions'] = df['co2_per_km'] * distance_km
    return df

def create_plot(df, distance_km):
    plt.figure(figsize=(10, 6))
    plt.barh(df['transportmedel'], df['total_emissions'], color='skyblue')
    plt.xlabel('Totala CO2-utsläpp (gram)')
    plt.ylabel('Transportmedel')
    plt.title(f'Totala CO2-utsläpp för {distance_km} km')
    
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return plot_url

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        distance_km = float(request.form['distance'])
        result_df = calculate_total_emissions(transport_df, distance_km)
        plot_url = create_plot(result_df, distance_km) 
        return render_template('result.html', tables=[result_df.to_html(classes='data')], titles=result_df.columns.values, plot_url=plot_url)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)