# Brazilian Nut Effect Simulation for Alien Object Dimension Estimation

## Overview

This project simulates the Brazilian Nut Effect, a phenomenon where larger particles are propelled upwards against the force of gravity, while smaller particles settle down in the presence of a constant random force. By leveraging this effect, we aim to determine the dimensions of an alien object introduced into a system of robot micro swarms.

![image](https://github.com/Kelvin4915/Brazil_nut_effect_simulation/assets/145865695/29792d67-a40c-4e4f-810d-5cef571e6e44)

## Simulation Details

In our simulation, we utilized the Brazilian Nut Effect with a swarm of 200 micro robots. The main premise is that particles of varying sizes will settle at different levels, causing particles of similar sizes to aggregate. By analyzing the positions and radii of robots in the vicinity of the alien object, we can infer its dimensions.

### Key Assumptions
1. **Brazilian Nut Effect:** Larger particles rise to the top, while smaller particles settle at the bottom when subjected to a random force.
2. **Consistent Behavior:** Particles of similar sizes will settle at the same level within the system.
3. **Reference Points:** The radii of robots around the unknown object can be used to estimate its dimensions.

## Methodology

1. **Simulation Setup:** 
   - A swarm of 200 robot micro particles was introduced into the system.
   - A constant random force was applied to the system to simulate the Brazilian Nut Effect.

2. **Data Collection:**
   - The positions and sizes of the robots were recorded.
   - The location and dimensions of the alien object were inferred based on the aggregation pattern of surrounding robots.

3. **Dimension Estimation:**
   - By referencing the radius of the robots near the alien object, we calculated its approximate dimensions.
![swarm_crop](https://github.com/Kelvin4915/Brazil_nut_effect_simulation/assets/145865695/ba0aa310-b7ff-4418-8e26-04ca24d569fc)

## Usage

To run the simulation and estimate the dimensions of an alien object, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/Kelvin4915/Brazil_nut_effect_simulation
