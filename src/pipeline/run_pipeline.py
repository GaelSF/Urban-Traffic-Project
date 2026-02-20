from src.simulation.traffic_simulation import TrafficSimulation
from src.ingestion.load_data import load_raw_data, validate_data
from src.transformation.transform_data import compute_metrics, save_processed_data
from src.ingestion.load_to_db import create_connection, create_table, load_data


def run_simulation():
    print("Ejecutando simulación...")
    sim = TrafficSimulation()
    df = sim.run(steps=100)
    df.to_csv("data/raw/traffic_data.csv", index=False)
    print("Datos crudos generados")


def run_ingestion():
    print("Cargando datos...")
    df = load_raw_data()
    df = validate_data(df)
    print("Datos validados")
    return df


def run_transformation(df):
    print("Transformando datos...")
    metrics = compute_metrics(df)
    save_processed_data(metrics)
    print("Datos transformados")
    return metrics


def run_load_to_db():
    print("Cargando a base de datos...")
    conn = create_connection()
    create_table(conn)
    load_data(conn)
    conn.close()
    print("Datos en DB")


def main():
    print("INICIANDO PIPELINE\n")

    run_simulation()
    df = run_ingestion()
    run_transformation(df)
    run_load_to_db()

    print("\nPIPELINE COMPLETADO")


if __name__ == "__main__":
    main()
