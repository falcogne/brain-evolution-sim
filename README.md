# brain-evolution-sim
Creating a simple environment (pseudo-realistic) and trying to evolve neural networks within it.


## Scientific background
*I'm no neuroscientist, but I've researched a substiantial amount about the brain to feel like I know some pertinent stuff*

Human brains evolved into a dual-hemispheric structure. People have hypothesized why we did so: whether one was verbal and one was non-verbal, whether the left was for the right side of the body and the right was for the left side of the body, but I don't think it's mainly because of either of those. Each hemisphere has been proven to have its own standalone consciousness; if you cut the two sides off from each other they both show signs of consciousness. And yes, the left is verbal and the right is non verbal (or vice-versa I may be wrong on sides). The idea I have found most compelling is that the two sides of the brain were made to be able to deal with order and chaos. 

The left side has a structured, algorithmic process that can deal with things it already knows. It is where you can react to a situation that you have seen before and make a rational decision about it. It is what deals with order. The right side, being able to deal with chaos, is much more dynamic and able to change. It deals with the situations that you don't know about.

The dual-hemmispheric structure of human brains is not unique to us. Most animals we have studied have two sides, no matter how small they are in total. Let's assume their hemispheres deal with order and chaos as well (we have no better guess as far as I know).

Evolution is meant for its creatures to be able to deal with the structrue of reality. So if brains evolve to deal with order and chaos, that means that reality is structured in order and chaos. 

## Connection from the science to the project 

Once I learned that brains evolve to fit the structure of reality, I wanted to test that theory. It'd be hard to change the structure of reality, or rapid-evolve animals. However, I have a master's in CS, enough experience with ML/AI, and just enough arrogance to try and do so artificially. That would require both creating reality and *players* that have NN *brains* for which the structure can change due to an evolutionary algorithm. 

Assuming I'll be successful in doing this, I would have a mini-reality where organisms roam freely according to their *brain* and then over time their brains evolve in order to maximize their *reward* within the environment. I would be able to see which structures of brains become the most successful and which ones propegate throughout society. 

At some point, humans evolved to not just know food, but also meta-food like where the food is. We realized that knowing the location of the food is more important than the food itself. I'll have to implement the concept of meta-food at some point if I want to replicate human-like organisms.

## Hypothesis

The closer I get to being able to replicate the structure of our true reality, the closer the strucutre of my player's brains will look to ours.

Obviously I won't be able to replicate reality very well (especially if I continue to only use my personal machine), but I think there will be enough randomness in my design to require something to deal with what you know, and something to deal with what you don't.

Things I think will help make the environment closer to reality: food, pair reproduction, social interactions (trade food?), random predators in environment, environment changes based on how it's used, day/night cycles.

## Design

### Classes:

Environment, Board, Player, House (not yet), Brain, Wolf, Food (maybe)

### Description

**Environment:** Enclosing class that keeps track of everything. Has all elements of the environment within it.

**Board:** Is the structure of reality. It is the ground that everything walks on.
Each location will have:
- Maneuverability: how much energy a step here takes
- Food: how much food can be extracted
- Fertility: how fast food grows

**Player:** is one of the organisms in the environment. Qualities:
- Age: maybe will die automatically if it
- Breedable: ability to repoduce at the current moment
    - Gender: I think I'll make male and female organisms, but maybe not initially because it just complicates how reproduction would go. 
- Energy: replenished by food, depleted by action

**Brain:** The NN that makes action decisions for the players. Will start it simply, and let evolution design it. Not quite sure how the evolution will go yet, but will be an important decision. I'll research more about how current neural networks are designed to play games like this, and will design evolution to at least be able to reach there if it's optimal.

**Wolf:** moves semi-randomly and can kill player if it encounters a player.

**Food:** Right now it would only have a "sustinence" level, so it doesn't need to be its own class, but if I also include a "taste" factor somehow then maybe I'd want to make a seperate class.