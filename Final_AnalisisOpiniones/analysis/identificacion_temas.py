def identificar_temas(df):
    # Aquí puedes añadir lógica para identificar temas específicos
    temas = {'servicio': [], 'precio': [], 'calidad': [], 'funcionalidad': [], 'otros': []}
    
    for index, row in df.iterrows():
        texto = row['comment_limpio']
        if 'servicio' in texto:
            temas['servicio'].append(texto)
            df.at[index, 'aspecto'] = 'servicio'
        elif 'precio' in texto:
            temas['precio'].append(texto)
            df.at[index, 'aspecto'] = 'precio'
        elif 'calidad' in texto:
            temas['calidad'].append(texto)
            df.at[index, 'aspecto'] = 'calidad'
        elif 'funcionalidad' in texto:
            temas['funcionalidad'].append(texto)
            df.at[index, 'aspecto'] = 'funcionalidad'
        else:
            temas['otros'].append(texto)
            df.at[index, 'aspecto'] = 'otros'
    
    return df, temas
