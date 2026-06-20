# Cricket Projectile Motion Simulator

A Python simulator that models the trajectory of a cricket ball as projectile motion, and determines whether a shot clears the boundary for a six.

## What it does

Given the ball's launch speed, angle, and height, the simulator uses standard kinematics equations to compute:

- Maximum height reached
- Time to reach maximum height
- Total flight time
- Horizontal range
- Final velocity on landing
- Whether the shot clears the boundary ("It's a six!")

It then renders two plots:

1. **Side view** — the curved trajectory of the ball, with the peak height marked and the boundary line shown
2. **Top view** — the cricket field, the boundary circle, and the ball's path overlaid

## How it works

The physics is based on standard projectile motion equations:

- Horizontal velocity: `vx = v * cos(θ)`
- Vertical velocity: `vy = v * sin(θ)`
- Trajectory: `y(t) = h + vy*t - 0.5*g*t²`
- Total flight time (accounting for launch height) is found by solving the above for `y(t) = 0`

## Requirements

- Python 3.8+
- matplotlib
- numpy

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the simulator:

```bash
python projectile_motion.py
```

You'll be prompted to enter:

- Ground length and width (m)
- Boundary distance (m)
- Initial velocity (m/s)
- Launch angle (degrees)
- Launch height (m)
- Gravity (m/s², defaults to 9.8 on Earth)

The simulator will print the calculated results and display the trajectory plots. You can run multiple simulations in a row.

## Example

```
Enter ground length (m): 150
Enter ground width (m): 140
Enter boundary distance (m): 70
Enter initial velocity (m/s): 35
Enter launch angle (degrees): 35
Enter launch height (m): 1
Enter gravity (m/s^2): 9.8
```

Output:

```
Maximum Height:        21.56 m
Time to Max Height:    2.05 s
Total Flight Time:     4.15 s
Horizontal Range:      118.87 m
Final Velocity:        35.28 m/s
Boundary Distance:     70.00 m
IT'S A SIX! Ball cleared the boundary!
```
<img width="1092" height="563" alt="image" src="https://github.com/user-attachments/assets/1bd321fa-4006-4940-9c53-0a3bbf062e57" />

<img width="539" height="627" alt="image" src="https://github.com/user-attachments/assets/7c4cbfde-257b-4d36-a4d2-10a1348a44bf" />


## Possible improvements

- Add air resistance / drag for more realistic flight paths
- Animate the trajectory instead of static plots
- Support different field shapes (some grounds aren't perfectly circular boundaries)


