from data_cleaning import cargar_csv, limpiar_datos, vectorizar_texto, mostrar_resultados

if __name__ == "__main__":
    file_name = 'comentarios_reddit.csv'
    df = cargar_csv(file_name)
    df_limpio = limpiar_datos(df)
    tfidf_matrix, feature_names = vectorizar_texto(df_limpio)
    mostrar_resultados(df_limpio, tfidf_matrix, feature_names)
