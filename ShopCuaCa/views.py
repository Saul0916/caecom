from django.shortcuts import render
import pandas as pd
import csv

# Create your views here.
def home(request):
    file_path = '/Users/saul/Downloads/pj.csv'
    product_data = []
    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=';')
        for row in csvreader:
            product_data.append({
                'name': row['name'],
                'price': row['price'],
                'image_URL': row['image_URL'],
                'product_URL': row['product_URL'],
                'review': row['review'],
                'luot_mua':row['luot_mua']
            })

    print(product_data)  # Check if product_data contains all rows

    return render(request, 'home.html', {'product_data':product_data})

