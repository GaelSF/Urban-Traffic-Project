import pandas as pd

def compute_metrics(df):
    # Velocidad promedio por tiempo
    avg_velocity = df.groupby("time")["velocity"].mean().reset_index()
    avg_velocity.rename(columns={"velocity": "avg_velocity"}, inplace=True)

    # Número de autos (densidad proxy)
    density = df.groupby("time")["car_id"].count().reset_index()
    density.rename(columns={"car_id": "num_cars"}, inplace=True)

    # Unir métricas
    metrics = pd.merge(avg_velocity, density, on="time")

    # Índice simple de congestión
    metrics["congestion_index"] = metrics["num_cars"] / (metrics["avg_velocity"] + 1e-5)

    # Clasificación de tráfico
    def classify(congestion):
            if congestion < 5:
                return "Low"
            elif congestion < 10:
                return "Medium"
            else:
                return "High"

    metrics["traffic_level"] = metrics["congestion_index"].apply(classify)


    return metrics


def save_processed_data(df, path="data/processed/traffic_metrics.csv"):
    df.to_csv(path, index=False)
    print(f"Datos transformados guardados en {path}")


if __name__ == "__main__":
    from src.ingestion.load_data import load_raw_data, validate_data

    df = load_raw_data()
    df = validate_data(df)

    metrics = compute_metrics(df)
    save_processed_data(metrics)

    print(metrics.head())
