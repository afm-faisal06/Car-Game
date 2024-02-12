# Car Game

---

This Python program uses the OpenGL library to create a simple car game with the following features:

1. **Game Environment**: The game takes place on a 700x600 window where the car moves horizontally and vertically to avoid rocks.

2. **Game Elements**:
   - **Car**: Represented by a rectangular shape that the player controls using the arrow keys.
   - **Rocks**: Represented by rectangular shapes that fall from the top of the screen. The player must avoid colliding with them.
   - **Power-up**: Activated by a right-click, it temporarily grants the car invincibility against collisions with rocks.
   
3. **Gameplay**:
   - The player controls the car using the arrow keys, navigating it to avoid collision with falling rocks.
   - Rocks fall from the top of the screen, and if the car collides with any of them, the game ends.
   - The player's score is represented by the distance covered by the car without collision.
   - A power-up can be activated using a right-click, granting temporary invincibility to the car against collisions.
   
4. **Graphics and Animation**:
   - Rocks and the car are represented by lines and rectangles drawn using OpenGL's drawing functions.
   - Animation is achieved by updating the positions of rocks and the car in the `animation()` function.
   - The game screen is updated continuously using OpenGL's display functions.

5. **User Interaction**:
   - Mouse clicks are used to activate the power-up and control the game state.
   - Arrow keys are used to control the car's movement.

---
