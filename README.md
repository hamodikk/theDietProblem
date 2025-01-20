# MSDS 460 Assignment 1

This repository includes the work done for the first assignment of the MSDS 460 class. It tackles The Diet Problem using linear programming approach and PuLP library.

## Table of Contents
- [Introduction](#introduction)
- [Problem Approach](#problem-approach)
- [Initial Code Result](#usage)
- [Revised Code Result](#revised-code-result)
- [Generative AI Approach](#generative-ai-approach)

## Introduction

Further information on The Diet Problem can be found [here](https://neos-guide.org/case-studies/om/the-diet-problem/).

For this assignment, I will be using 5 packaged items to implement The Diet Problem. The documentation for the five packaged food items has been included in the github repository. In addition to the labeling of the files, here are the items and their prices per serving:

- Devanco Beef Bacon - $0.85/serving ($8.49 / 10 servings) 
- Chicken Breasts – $0.46/serving ($6.97 / ~15 servings) 
- Kerrygold Unsalted Butter – $0.37/serving ($5.99 / 16 servings) 
- O Organics Quinoa – $0.70/serving ($6.99 / 10 servings) 
- Cocoa Puffs Cereal – $0.85/serving ($6.79 / 8 servings)

The prices per serving have been calculated using the price of the packaged item divided by the number of servings per package the nutritional facts mention. It is worth noting that the beef bacon and chicken breasts labels only mention serving sizes in weight, which I used to divide the package weight to find the number of servings per package.

## Problem Approach

Here is the linear programming problem in standard form: 
**Decision Variables:**
- X<sub>1</sub> – Beef Bacon 
- X<sub>2</sub> – Chicken Breasts 
- X<sub>3</sub> – Butter 
- X<sub>4</sub> – Quinoa 
- X<sub>5</sub> – Cereal

**Objective Function:**

Minimize Z = 0.85x<sub>1</sub> + 0.46x<sub>2</sub> + 0.37x<sub>3</sub> + 0.7x<sub>4</sub> + 0.85x<sub>5</sub> 

**Constraints:**

These inequalities are for sodium, energy, protein, vitamin D, calcium, iron, potassium and lastly non-zero requirements, in that order:

270x<sub>1</sub> + 74x<sub>2</sub> + 0x<sub>3</sub> + 0x<sub>4</sub> + 130x<sub>5</sub> ≤ 35000

45x<sub>1</sub> + 165x<sub>2</sub> + 100x<sub>3</sub> + 170x<sub>4</sub> + 140x<sub>5</sub> ≥ 14000

5x<sub>1</sub> + 31x<sub>2</sub> + 0x<sub>3</sub> + 6x<sub>4</sub> + 2x<sub>5</sub> ≥ 350

0x<sub>1</sub> + 0x<sub>2</sub> + 0x<sub>3</sub> + 0x<sub>4</sub> + 4x<sub>5</sub> ≥ 140

2x<sub>1</sub> + 11x<sub>2</sub> + 0x<sub>3</sub> + 20x<sub>4</sub> + 130x<sub>5</sub> ≥ 9100

0x<sub>1</sub> + 1x<sub>2</sub> + 0x<sub>3</sub> + 2.1x<sub>4</sub> + 3.6x<sub>5</sub> ≥ 126

58x<sub>1</sub> + 0x<sub>2</sub> + 0x<sub>3</sub> + 250x<sub>4</sub> + 10x<sub>5</sub> ≥ 32900

x<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub>, x<sub>4</sub>, x<sub>5</sub> ≥ 1

This linear programming problem is designed to calculate a weekly diet using at least one of each of the 5 designated packaged food items with the goal finding the cheapest diet that will satisfy the nutritional needs within a week. The Python PuLP code and the output of the code have been included in the github repository under [PuLP code](Assignment_1_PuLP.py) and [output](PuLP_Output.txt) respectively. 

## Initial Code Result

Running the PuLP code, we get the following results for the weekly number of servings per each food item and the weekly cost of all the food items:

```bash
Optimal servings for each food item for minimum cost: 
Devanco_Beef_Bacon: 0.0 servings 
Chicken_Breats: 0.0 servings 
Kerrygold_Butter: 0.0 servings 
O_Organics_Quinoa: 129.59752 servings 
Cocoa_Puffs_Cereal: 50.06192 servings 
Total weekly cost: $133.27
```

The results show that to get the nutritional needs with minimum cost, I could consume 0 servings of beef bacon, chicken breast and butter and 129.6 servings of quinoa and finally 50.1 servings of cereal. The total cost of all these servings would come to $133.27 per week.

## Revised Code Result

In this part, I have included an additional constraint (mentioned also as the last constraint in part 2) that requires each packaged item to be used at least once each week. Following is the additional code mentioned:

```py
# Add the constraint that requires at least one serving for each packaged item
for food in foods:
    problem += x[food] >= 1, f"Min_Serving_{food}"
```

The PuLP code in the github repository is of this revised version and the output of the code can be found in [here](PuLP_Output_Revised.txt) with the following output:

```bash
Optimal servings for each food item for minimum cost: 
Devanco_Beef_Bacon: 1.0 servings 
Chicken_Breats: 1.0 servings 
Kerrygold_Butter: 1.0 servings 
O_Organics_Quinoa: 129.36811 servings 
Cocoa_Puffs_Cereal: 49.997214 servings 
Total weekly cost: $134.74 
```

The additional constraint does not seem to have a big impact on the results. The only differences are the 1 additional serving for each of the 3 items that had 0 serving in the original result as well as the small changes in the other two items and the total weekly cost of the items. In comparison to the original results, these additional constraints did not change the results while introducing minimal variety in the diet. To further introduce variety to the diet, we can add additional food items, increase the minimum serving for each item further, or implement more constraints such as fibers or fats.

## Generative AI Approach

I have selected [ChatGPT](https://chatgpt.com/) as the LLM model. For this part, I initially started the conversation with the agent by narrowing its focus by telling it to pretend to be a data scientist, and describe the problem to tackle. Once provided with an approach and code, I specified some of the requirements for our assignment approach, such as using PuLP or specifying the nutritional constraints. Once I refined the requirements, the agent was able to provide a code similar to what I wrote for the assignment. There is a chance that as the problem is a popular one, the training of the agent probably includes solution code, which is why it was able to provide answers that are ideal. I think the agent was able to successfully provide an adequate solution to The Diet Problem. When tackling problems such as this, it is important to define a focus for the agent, followed by a general direction with goals and tasks. I seem to find success when I allow the agent to provide an initial response, followed by prompting for modifications over the initial response as well as any additional specifications. This allows the agent to work on its own response to better tailor the answer to the needs of the task at hand. I should point out that I grouped up several prompts and ended up with 2 prompts to get a relatively desired answer. More prompts could result in a further performance increase with the agent. The conversation with the agent can be found [here](ChatGPT_conv.txt). It is important to note that there are no easy ways to save a conversation with the agent, and some copy pasting looks different in plain text file.