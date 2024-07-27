import pandas as pd
import matplotlib.pyplot as plt

# Läs in CSV-filen
file_path = 'data-och-statistik-klimat-vaxthusgaser-utslapp-fran-inrikes-transporter-.csv'
df = pd.read_csv(file_path)

# Visa de första raderna för att kontrollera att allt lästs in korrekt
print(df.head())

# Välj den senaste året för analys (2023 i detta fall)
latest_year_data = df.iloc[-1]

# Skapa en ny DataFrame med transportmedel och deras CO2-utsläpp
transport_data = {
    'transportmedel': ['A-traktorer', 'Järnväg', 'Mopeder och motorcyklar', 'Bussar', 'Flyg', 'Sjöfart', 'Lätta lastbilar', 'Tunga lastbilar', 'Personbilar'],
    'co2_per_km': [latest_year_data['A-traktorer'], latest_year_data['Järnväg'], latest_year_data['Mopeder och motorcyklar'], latest_year_data['Bussar'], latest_year_data['Flyg'], latest_year_data['Sjöfart'], latest_year_data['Lätta lastbilar'], latest_year_data['Tunga lastbilar'], latest_year_data['Personbilar']]
}

transport_df = pd.DataFrame(transport_data)

# Funktion för att beräkna totala CO2-utsläpp för en given sträcka
def calculate_total_emissions(df, distance_km):
    df['total_emissions'] = df['co2_per_km'] * distance_km
    return df

# Användaren anger sträckan i kilometer
distance_km = float(input("Ange sträckan i kilometer: "))

# Beräkna totala utsläpp
transport_df = calculate_total_emissions(transport_df, distance_km)

# Visa resultaten
print(f"Totala CO2-utsläpp för {distance_km} km:")
print(transport_df[['transportmedel', 'total_emissions']])

# Visualisera resultaten
plt.figure(figsize=(10, 6))
plt.barh(transport_df['transportmedel'], transport_df['total_emissions'], color='skyblue')
plt.xlabel('Totala CO2-utsläpp (gram)')
plt.ylabel('Transportmedel')
plt.title(f'Totala CO2-utsläpp för {distance_km} km')
plt.show()