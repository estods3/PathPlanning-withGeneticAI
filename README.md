# PathPlanning-withGeneticAI

After watching a Youtube video (link below) on Genetic AI algorithms, I thought about creating my own program that could simulate a genetic AI in a random environment. This way, you could see just how the AI can learn the path (provided one exists) from the start point to the end point.

This simulation is a useful demonstration for genetic AI's applications in autonomous vehicles or robotics. If you have enough computing power, you could use this to create a coordinate trajectory for your vehicle to navigate around an obstacle.

## System Requirements

You will need Python to run this program. I tested it with Python 2.7.15+ 64 bit.
You will also need a few Python modules. You can install these by typing 

`pip install -r requirements.txt` 

in your cloned directory of this repository.

## Example:

Clone or download the code and navigate to its directory in a terminal.
Run the program by typing the following in a terminal: 

`python src/runSimulation.py`

A window will appear with a random collection of obstacles and start and end points on either side of the screen. "Samples" from the population will begin to travel in random directions based on their randomized genetics that are hard-coded into them at the start of the simulation.
![Alt text](/pics/gen3.PNG?raw=true "After 3 Generations")

Some samples may make it closer to the end point than others, which will give them a higher fitness score, which is a reproductive advantage when the next generation is produced. The samples with the highest fitness scores are more likely to be naturally selected as parents. Their children samples will be cloned with the same genetics as their parents, but with random mutations which allow them to potentially outperform their parents and reach the end point.
![Alt text](/pics/gen9.PNG?raw=true "After 9 Generations")

If all goes well, the samples will not only find the end point, but optimize the path. After many many generations, the resulting path should resemble the shortest path between the start and end point without hitting any obstacles.
![Alt text](/pics/gen280.PNG?raw=true "After 280 Generations")



## Resources:
https://www.youtube.com/watch?v=BOZfhUcNiqk  
https://github.com/Code-Bullet/Smart-Dots-Genetic-Algorithm-Tutorial
