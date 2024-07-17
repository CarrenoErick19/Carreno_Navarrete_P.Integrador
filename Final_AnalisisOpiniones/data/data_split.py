from sklearn.model_selection import train_test_split

def dividir_datos(df, test_size=0.2, validation_size=0.1):
    train_df, test_df = train_test_split(df, test_size=test_size, random_state=42)
    train_df, val_df = train_test_split(train_df, test_size=validation_size/(1-test_size), random_state=42)
    return train_df, val_df, test_df

