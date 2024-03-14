import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from django.db.models import Avg
from ..models import VariationPrice
import os

def report_price_variation():
    price_variations = VariationPrice.objects.all()

    df = pd.DataFrame(list(price_variations.values()))
    print(df)

    df['data'] = pd.to_datetime(df['data'])

    df_daily_mean = df.groupby('data').agg({'price': 'mean'}).reset_index()

    plt.figure(figsize=(10, 6))
    plt.bar(df_daily_mean['data'], df_daily_mean['price'], color='blue')
    plt.title('Variação de Preço ao Longo do Tempo')
    plt.xlabel('Data')
    plt.ylabel('Preço Médio')
    plt.xticks(rotation=45)
    plt.tight_layout()

    filename = 'price_variation_report.png'
    plt.savefig(filename)

    # Exibir o nome do arquivo onde o gráfico foi salvo
    print(f'O gráfico foi salvo em: {os.path.abspath(filename)}')
    
    print(df_daily_mean)