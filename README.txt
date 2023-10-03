Principles of  Programming Assignment 1: Brainstorm 

https://images.app.goo.gl/g6qEq4jHae3FMEov9

Submission checklist 
A ZIP file containing: 
1. An assignment report submitted as a Word Document that has 
A title page with the student’s name, 
Date and assignment title and 
Clear Structure to identify the answer of each of the assignment parts. 
Work Assignments for each member of the team. ( for group) 
Short video that demo the app (2 – 5 min)
The program folder including all source files and GIT repository.

Part 1 (20%): Program inception
Invent a simple text-based adventure game that allows the user to choose their actions in a story to determine their success in the game.
The user shall be presented with a story that would allow the user to pick one out of two roles. The user would play the chosen role in the story. ( Murderer or detective).
Story: 
In the quiet town of Stars Hallow, the Edencrest Manor, a magnificent mansion, held dark secrets. One fateful night, a chilling scream shattered the peace as Lord Christian Dior was found murdered in his study.
The Stars Hollow Constabulary, led by Inspector Montgomery, was summoned to investigate the crime. Suspicion hung heavy as they interrogated staff and scoured the mansion for clues.
Meanwhile, in the shadows of the mansion, a figure lurked—the Murderer. A master of disguise and deceit, the Murderer had been living in the shadows of the manor, observing the unfolding events with bated breath. Their aim was to eliminate any trace that could lead to their apprehension and make a daring escape from the mansion unnoticed.
You stand at the mansion's threshold, facing a choice: Will you embrace the darkness as the Murderer, seeking to outwit the Inspector and escape the clutches of justice, or will you step into the shoes of the Detective, determined to unravel the secrets of Eboncrest Manor and bring the murderer to justice? The choice is yours, and the fate of stars hallow hangs in the balance.


 Each role shall have three attributes. Identify the attribute names and assign the two roles hard-coded values of your choice in the following range: -2, -1, 0, +1, +2. 
Murderer:
Strength (ST): +2
Dexterity (DX): +1
Intelligence (IQ): -1

Detective: 
Strength (ST): -1
Dexterity (DX): +1
Intelligence (IQ): +2

Based on the story, define the quest that the user, in their role, will have to go on (e.g., finding a treasure, destroying a monster, win MasterChef, solve a mystery). The quest shall be made of a minimum of three challenges. Each challenge shall be based on a different attribute of the role, such that all their attributes are used. 
Quest for the murderer: 
Eliminating Evidence: Your first challenge is to erase any trace of your presence at the crime scene. This challenge relies heavily on your Dexterity (DX) attribute. You must skillfully clean up the murder scene without leaving a shred of evidence behind. Roll the dice to determine your success:
Critical Loss: You make a mess, and the Inspector is hot on your trail.  
Loss: You leave behind some incriminating evidence.
Win: You clean up the scene without a hitch.
Critical Win: You eliminate all evidence and gain confidence.
 Dodging Suspicion: In this challenge, your Intelligence (IQ) will be tested. You need to blend in with the mansion's staff and avoid drawing attention. Roll the dice to see how well you can maintain your cover:
Critical Loss: You draw suspicion to yourself. 
Loss: You struggle to maintain your cover.
Win: You go unnoticed.
Critical Win: You successfully divert suspicion away from yourself. 
The Great Escape: Your final challenge is to make a daring escape from Eboncrest Manor. This challenge relies on your Strength (ST) to overcome obstacles in your path and slip away undetected. Roll the dice to determine your fate:
Critical Loss: You're caught during your escape attempt. 
Loss: You encounter obstacles but manage to flee.
Win: You escape without major issues.
Critical Win: You execute a flawless getaway, leaving no trace.  
Quest for the detective: 
Gathering Clues: Your first challenge is to search the mansion for vital clues that may lead you to the murderer. This challenge relies on your Intelligence (IQ). Roll the dice to uncover clues:
Critical Loss: You miss crucial evidence.
Loss: You find some clues but not enough to make progress.
Win: You gather significant clues.
Critical Win: You uncover all key evidence.
 Interrogating Suspects: In this challenge, your Dexterity (DX) will be essential for your success in questioning the mansion's staff and suspects. Roll the dice to gauge your interrogation skills:
Critical Loss: You offend the suspects and get misleading information.
Loss: You struggle to extract useful information.
Win: You obtain valuable insights.
Critical Win: You skillfully extract confessions.  
Identifying the Culprit: Your final challenge is to piece together the evidence and make an accurate deduction. This challenge combines your Intelligence (IQ), Strength (ST), and Dexterity (DX). Roll the dice to identify the murderer:
Critical Loss: You accuse the wrong person, letting the real killer go free.  
Loss: You're close but not entirely correct.
Win: You correctly identify the murderer.
Critical Win: You not only identify the killer but also capture them, ensuring justice is served.

Define the gameplay rules which are dice-based. You can pick the number of dice and the range of each dice (e.g., two six-sided dice with a range of 2-12). As the game proceeds the outcome of each challenge would depend upon the roll value (given by the sum of the number rolled on dice) and the attribute value related to the challenge. Associate the total roll value with different results e.g., critical loss, loss, win, critical win. These results could have the following meaning: 
a. Critical Loss (e.g., 2 - 3): challenge is lost and the attribute that is based on is decreased
b. Loss (e.g., 4-7): challenge is lost, no change in the character’s attributes 
c. Win (e.g., 8-10): challenge is won, no change in the character’s attributes 
d. Critical Win (e.g., 11-12): challenge is won and the attribute that is based on increases
Gameplay Rules:
Dice Rolling: You will use two six-sided dice with a range of 2-12.
Attribute Interaction: Your success in each challenge depends on the sum of the dice roll and your related attribute. Each challenge corresponds to one of your attributes: Strength (ST), Dexterity (DX), or Intelligence (IQ).
Challenge Outcomes:
Critical Loss (2-3): Challenge is failed, and the related attribute decreases by 1. This signifies a significant failure.
Loss (4-7): Challenge is failed, but there is no change in your character's attributes. This represents a minor setback.
Win (8-10): Challenge is passed, and there is no change in your character's attributes. You succeed without any complications.
Critical Win (11-12): Challenge is passed, and the related attribute increases by 1. This indicates a remarkable success.

Define the game win/loss criteria. For example, the user might win if they succeed in all challenges. 
Win/lose criteria: 
The Murderer wins by successfully completing their quest, which means eliminating all evidence and escaping the mansion without being caught.
The Detective wins by solving the murder mystery, correctly identifying the murderer among the suspects.
The game ends if the Murderer is caught or the Detective fails to solve the mystery, resulting in a loss.

Part 2 (20%): Program Structure (???)
Create a program using Visual Studio Code and Python that will implement the game and have the following structure that ensures a basic separation of concerns:
1. The program shall use GIT for version control. Ensure the GIT repository is initialized as soon as the program folder is created. 
2. The program shall at least have the following modules: 
a. App.py: implements the interactivity with the user. 
b. Game.py: implements the game data and logic. 
c. .py: implements the data and logic associated with the first role (e.g., wizard.py) 
d. .py: implements the data and logic associated with the second role (e.g., barbarian.py)

3. Each module shall be described using a doc string at the top of the source file
4. Each module function shall be described using a doc string to explain its purpose 
5. Each module variable shall be described using a to explain its purpose

 Report Requirements 
In your assignment report, identify and describe the program structure, clearly stating the purpose of each module and function.

Part 3 (40%): Program logic/ Flow (???)
Implement the game logic to allow the following functionality: 

