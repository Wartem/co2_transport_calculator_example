import matplotlib.pyplot as plt
from io import BytesIO
import base64
from flask import render_template, request
from app import app, df

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        distance = float(request.form['distance'])
        
        emissions_column = 'Transport emissions per kilometer travelled'
        df['Total emissions'] = df[emissions_column] * distance
        
        # Sort the dataframe by Total emissions
        df_sorted = df.sort_values('Total emissions', ascending=False)
        
        # Create a bar plot
        plt.figure(figsize=(15, 8))  # Increased figure size
        plt.bar(df_sorted['Entity'], df_sorted['Total emissions'])
        plt.title(f'CO2 Emissions for {distance} km by transport type', fontsize=18)
        plt.xlabel('Transport Mode', fontsize=16)
        plt.ylabel('CO2 Emissions (g)', fontsize=16)
        plt.xticks(rotation=45, ha='right', fontsize=14)
        plt.yticks(fontsize=12)
        plt.tight_layout()
        
        # Save plot to a buffer
        buffer = BytesIO()
        plt.savefig(buffer, format='png', dpi=300)  # Increased DPI for better quality
        buffer.seek(0)
        plot_data = base64.b64encode(buffer.getvalue()).decode()
        
        # Pass the sorted DataFrame to the template
        return render_template('result.html', table_data=df_sorted, plot_url=plot_data, distance=distance)
    
    return render_template('index.html')