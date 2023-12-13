# Simulator
WIDTH  = 900 
HEIGHT = 900
MAX_FOOD_SUPPLY = 100
CHANCE_OF_ESCAPE = 0.2
initialPreyPopulation = 300
initialPredatorPopulation = 50
INIT_VELOCITY = 10
FPS = 30

PREY_REPRODUCTION_CHANCE = 0.5
PREDATOR_REPRODUCTION_CHANCE = 0.25
MUTATION_CHANCE = 0.1

# Food
FoodCOLOR = (0, 255, 0, 100)
FoodSIZE = 5

# Predator
PredatorMAX_HEALTH   = 100
PredatorVIEW_RADIUS  = 200
PredatorMAX_VELOCITY = 15
PredatorSIZE = 15
PredatorCOLOR = (255, 0, 0, 100)
PredatorHEALTH_GAIN = PredatorMAX_HEALTH * 0.05
PredatorHEALTH_LOSS = PredatorMAX_HEALTH * 0.005
MAX_DETECTION_OF_PREY  = 10
MAX_ATTRACTION_TO_PREY = 10
PredatorsMUTATION_AMOUNT = 0.05

# Prey
PreyMAX_HEALTH   = 100
PreyVIEW_RADIUS  = 200
PreyMAX_VELOCITY = 15
PreySIZE = 15
PreyCOLOR = (0, 255, 255, 100)
PreyHEALTH_GAIN = PreyMAX_HEALTH * 0.05
PreyHEALTH_LOSS = PreyMAX_HEALTH * 0.005
MAX_DETECTION_OF_FOOD       = 10
MAX_ATTRACTION_TO_FOOD      = 10
MAX_DETECTION_OF_PREDATOR   = 10
MAX_REPULSION_FROM_PREDATOR = 10
PreyMUTATION_AMOUNT = 0.05

#Detection
maxForce = 1.5