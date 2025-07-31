<h1>Snake Game with Pygame</h1>

<p>This project is a classic Snake game implemented using <strong>Python</strong> and the <strong>Pygame</strong> library. It features a graphical user interface with smooth gameplay, custom graphics, sound effects, and score tracking. The game offers two main implementations showcasing different coding styles and mechanics for the Snake game.</p>

<h2>Features</h2>
<ul>
  <li>Snake controlled by arrow keys to move around the grid.</li>
  <li>Randomly spawning fruit (apples) that the snake can eat to grow longer.</li>
  <li>Game over conditions when the snake hits the screen boundaries or itself.</li>
  <li>Custom graphics for snake head, body, tail, and fruit loaded from images.</li>
  <li>Sound effects for eating fruit and game events.</li>
  <li>Score display based on snake length.</li>
  <li>Background music and pause/play functionality in one version.</li>
  <li>Two implementations: a class-based vector position approach and a pixel-based coordinate approach.</li>
</ul>

<h2>How to Run</h2>
<ol>
  <li>Ensure you have <code>Python 3.x</code> installed.</li>
  <li>Install the <code>pygame</code> library if not installed:
    <pre><code>pip install pygame</code></pre>
  </li>
  <li>Download or clone the repository.</li>
  <li>Place all required assets (images and sounds) in the specified paths, or update the code to reflect your asset locations:
    <ul>
      <li>Snake head and body images (e.g. <code>dora.jpg</code>)</li>
      <li>Fruit image (e.g. <code>mon.jpg</code>)</li>
      <li>Sound files (e.g. <code>haha.wav</code>, <code>oh_no.mp3</code>)</li>
      <li>Background music (e.g. <code>B.mp3</code>)</li>
    </ul>
  </li>
  <li>Run the main Python file:
    <pre><code>python your_snake_game_file.py</code></pre>
  </li>
</ol>

<h2>Controls</h2>
<ul>
  <li><strong>Arrow Keys</strong>: Move the snake up, down, left, and right.</li>
  <li>In the second implementation:
    <ul>
      <li>Press <code>Enter</code> to restart after game over.</li>
      <li>Press <code>Escape</code> to exit the game.</li>
    </ul>
  </li>
</ul>

<h2>Code Structure</h2>
<p>The project includes two different game classes:</p>
<ul>
  <li><strong>SNAKE, FRUIT, MAIN</strong> classes implementing the snake game using grid vectors and images for different snake parts.</li>
  <li><strong>Dora, Eat, Game</strong> classes implementing a similar snake game with pixel-based movement, background music, and collision detection.</li>
</ul>

<h2>Dependencies</h2>
<ul>
  <li>Python 3.x</li>
  <li>Pygame library</li>
</ul>

<h2>Assets</h2>
<p>Make sure to have the following files in your working directory or adjust the paths in the code accordingly:</p>
<ul>
  <li><code>dora.jpg</code> - Snake head/body/tail image</li>
  <li><code>mon.jpg</code> - Fruit/apple image</li>
  <li><code>haha.wav</code> and <code>oh_no.mp3</code> - Sound effects</li>
  <li><code>B.mp3</code> - Background music</li>
  <li><code>bag.jpg</code> - Background image for the second game version</li>
  <li><code>PoetsenOne-Regular.ttf</code> - Font file used for score display</li>
</ul>

<h2>Future Improvements</h2>
<ul>
  <li>Refactor and unify both game versions for consistency.</li>
  <li>Add more game modes or difficulty levels.</li>
  <li>Improve graphics and animations.</li>
  <li>Add pause/resume functionality in all versions.</li>
  <li>Implement better collision handling and game state management.</li>
</ul>

<h2>License</h2>
<p>This project is open-source and free to use and modify.</p>

<p>Enjoy playing and customizing your Snake game!</p>
