from src.model import BacteriaCellularAutomaton

# Crear simulación en gravedad normal
sim = BacteriaCellularAutomaton(L=50, microgravity=False)
print(f"Células iniciales: {sim.get_cell_count()}")
print(f"Sustrato: {sim.get_substrate_amount()}")

sim.step()
print(f"Células después de 1 paso: {sim.get_cell_count()}")