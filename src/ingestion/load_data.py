import pandas as pd

def load_raw_data(path="data/raw/traffic_data.csv"):
    try:
        df = pd.read_csv(path)
        print(f"Datos cargados: {df.shape}")
        return df
    except Exception as e:
        print(f"Error al cargar datos: {e}")
        return None


def validate_data(df):
    required_columns = ["time", "car_id", "position", "velocity"]

    # Verificar columnas
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Falta columna: {col}")

    # Verificar nulos
    if df.isnull().sum().any():
        print("Advertencia: hay valores nulos")

    # Tipos básicos
    df["time"] = df["time"].astype(int)
    df["car_id"] = df["car_id"].astype(int)

    return df


if __name__ == "__main__":
    df = load_raw_data()
    df = validate_data(df)
    print(df.head())
