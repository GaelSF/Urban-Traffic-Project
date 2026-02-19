import numpy as np
import pandas as pd

class TrafficSimulation:
    def __init__(self, num_cars=20, road_length=100, max_speed=5):
        self.num_cars = num_cars
        self.road_length = road_length
        self.max_speed = max_speed

        # Inicialización
        self.positions = np.sort(np.random.rand(num_cars) * road_length)
        self.velocities = np.random.randint(1, max_speed, size=num_cars)

    def step(self):
        for i in range(self.num_cars):
            # Distancia al siguiente coche
            next_i = (i + 1) % self.num_cars
            distance = self.positions[next_i] - self.positions[i]

            if distance <= 0:
                distance += self.road_length

            # Regla simple: evitar colisión
            if distance < self.velocities[i]:
                self.velocities[i] = max(0, distance - 1)

            # Acelerar si puede
            elif self.velocities[i] < self.max_speed:
                self.velocities[i] += 1

        # Actualizar posiciones
        self.positions = (self.positions + self.velocities) % self.road_length

    def run(self, steps=50):
        data = []

        for t in range(steps):
            self.step()
            for car_id in range(self.num_cars):
                data.append({
                    "time": t,
                    "car_id": car_id,
                    "position": self.positions[car_id],
                    "velocity": self.velocities[car_id]
                })

        return pd.DataFrame(data)


if __name__ == "__main__":
    sim = TrafficSimulation()
    df = sim.run(steps=100)

    df.to_csv("data/raw/traffic_data.csv", index=False)
    print("Datos generados en data/raw/traffic_data.csv")
