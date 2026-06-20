🏏 Cricket Projectile Motion Simulator

A Python simulator that models a cricket shot as projectile motion. Enter the
ball's launch speed, angle, and field dimensions, and it calculates the full
trajectory, checks whether the shot clears the boundary, and plots both a
side view and a top-down view of the field.

✨ Features


📐 Computes maximum height, time to max height, total flight time, horizontal
range, and final velocity
🎯 Determines whether the shot is a six (clears the boundary) or falls short
📈 Renders a side view of the parabolic trajectory
🗺️ Renders a top view of the trajectory on the cricket field, with the
boundary shown as a dashed circle
🔁 Lets you run multiple simulations in a row without restarting the script


🧰 Requirements


🐍 Python 3.x
matplotlib 📊
numpy 🔢


Install the dependencies with:

bashpython -m pip install matplotlib numpy

🚀 Usage

Run the script:

bashpython cricket_projectile_simulator.py

You'll be prompted for the following inputs:

InputDescriptionExample🏟️ Ground length (m)Length of the field150📏 Ground width (m)Width of the field150⭕ Boundary distance (m)Distance from the center to the boundary70💨 Initial velocity (m/s)Launch speed of the ball30📐 Launch angle (degrees)Angle of the shot above the horizontal35🏌️ Launch height (m)Height of the ball at the moment of the hit1🌍 Gravity (m/s²)Gravitational acceleration9.8

After entering the values, the simulator prints the calculated results to the
terminal and opens two plots.

🖼️ Example Output

With the example inputs above, the ball travels roughly 88 m — clearing the
70 m boundary — so the simulator reports "IT'S A SIX! 🎉"

📈 Side View

Shows the ball's parabolic path, its peak height (marked with a ⭐), and the
boundary line (dashed red).

Show Image

🗺️ Top View

Shows the trajectory traced across the field, with the boundary marked as a
dashed circle. The trajectory line crossing outside the circle confirms the
shot is a six. 🏆

Show Image

🧮 How It Works

The simulator uses standard projectile motion equations, accounting for a
non-zero launch height:


Velocity components: vx = v·cos(θ), vy = v·sin(θ)
Flight time: solved from 0 = h + vy·t - ½g·t² using the quadratic formula
Max height: h + vy² / (2g)
Range: vx × total flight time
Final velocity: √(vx² + vy_final²)


💡 Notes


🔺 Increase the velocity or adjust the angle to see the shot clear the
boundary; lower the velocity to see a shot fall short.
🎯 A launch angle around 35–45° typically maximizes range for a given velocity.
