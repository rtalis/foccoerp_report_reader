from flask import Flask, flash, redirect, request, render_template, session
from werkzeug.utils import secure_filename
import xml.etree.ElementTree as ET
import os
from datetime import datetime


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'uploads')
app.secret_key= 'my_secret'
def search_cod_item(file, search_value, search_by):
    # Carregar o arquivo XML
    tree = ET.parse(file)
    root = tree.getroot()
    data = []
    # Percorrer o XML
    if search_value == '':
        flash('Digite um valor para a busca')   
        return None 
    else:
        if search_by == 'DESC_ITEM':
            if len(search_value) < 3:
                flash('Digite um valor de buscar maior que 3 caracteres')
                return None
        
        
    for g_1 in root.iter('G_1'):
        cod_cot = g_1.find('COD_COT').text
        dt_emissao = datetime.strptime(g_1.find('DT_EMISSAO').text, '%d/%m/%y')

        for g_2 in g_1.iter('G_2'):
            fornecedor = g_2.find('FORNECEDOR').text
            for g_3 in g_2.iter('G_3'):
                if g_3.find(search_by) is not None and search_value.upper() in g_3.find(search_by).text:
                    unid_med = g_3.find('UNID_MED').text
                    qtde = g_3.find('QTDE').text
                    preco = g_3.find('PRECO_UNITARIO').text
                    desc = g_3.find('DESC_ITEM').text
                    data.append((cod_cot, dt_emissao, fornecedor,desc ,unid_med, qtde, preco))
                    data.sort(key=lambda x: x[1], reverse=True)


    return data

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    data = None
    search_value = None
    uploads_folder = app.config['UPLOAD_FOLDER']
    files = os.listdir(uploads_folder)
    xml_files = [file for file in files if file.endswith('.xml')]
    if xml_files:
        filename = os.path.join(uploads_folder, xml_files[0])
    else:
        filename = None
    if request.method == 'POST':
        search_value = request.form['search_value']
        search_by = request.form['search_by']
        data = search_cod_item(os.path.join(app.config['UPLOAD_FOLDER'], filename), search_value, search_by)
    elif 'last_file' in session:  # if there is a last used file in the session
        search_value = request.form.get('search_value')
        search_by = request.form.get('search_by')
        data = search_cod_item(os.path.join(app.config['UPLOAD_FOLDER'], filename), search_value, search_by) if search_value and search_by else None
    
    return render_template('main.html', data=data, search_term=search_value.upper() if search_value else None)

if __name__ == '__main__':
    app.run(debug=True)
