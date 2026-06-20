import math

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle, Circle


class ProjectileSimulator:

    
    def __init__(self):
        self.velocity = 0
        self.angle = 0
        self.gravity = 9.8
        self.launch_height = 0

        self.ground_length = 0
        self.ground_width = 0
        self.boundary_distance = 0

        self.trajectory_x = []
        self.trajectory_y = []

    # --------------------------------------------------------------
    def calculate_trajectory(self):
        """Compute full trajectory curve"""
        angle_rad = math.radians(self.angle)
        vx = self.velocity * math.cos(angle_rad)
        vy = self.velocity * math.sin(angle_rad)

        discriminant = vy ** 2 + 2 * self.gravity * self.launch_height
        total_time = (vy + math.sqrt(discriminant)) / self.gravity

        t = np.linspace(0, total_time, 200)
        self.trajectory_x = vx * t
        self.trajectory_y = self.launch_height + vy * t - 0.5 * self.gravity * t ** 2

        valid = self.trajectory_y >= 0
        self.trajectory_x = self.trajectory_x[valid]
        self.trajectory_y = self.trajectory_y[valid]

        return total_time

    # --------------------------------------------------------------
    def calculate_outputs(self):
        """Calculate max height, range, flight time, final velocity"""
        angle_rad = math.radians(self.angle)
        vx = self.velocity * math.cos(angle_rad)
        vy = self.velocity * math.sin(angle_rad)

        max_height = self.launch_height + (vy ** 2) / (2 * self.gravity)
        time_to_max_height = vy / self.gravity

        discriminant = vy ** 2 + 2 * self.gravity * self.launch_height
        total_time = (vy + math.sqrt(discriminant)) / self.gravity

        range_distance = vx * total_time
        vy_final = vy - self.gravity * total_time
        # FIXED: Pythagorean theorem needs vx**2 + vy_final**2, not 2*vx + 2*vy_final
        final_velocity = math.sqrt(vx ** 2 + vy_final ** 2)

        is_six = range_distance >= self.boundary_distance

        print("\n" + "=" * 60)
        print(" OUTPUT RESULTS:")
        print("=" * 60)
        print(f"Maximum Height:        {max_height:.2f} m")
        print(f"Time to Max Height:    {time_to_max_height:.2f} s")
        print(f"Total Flight Time:     {total_time:.2f} s")
        print(f"Horizontal Range:      {range_distance:.2f} m")
        print(f"Final Velocity:        {final_velocity:.2f} m/s")
        print(f"Boundary Distance:     {self.boundary_distance:.2f} m")
        print("-" * 60)

        if is_six:
            print(" IT'S A SIX! Ball cleared the boundary!")
        else:
            print(f"NOT A SIX! Short by {self.boundary_distance - range_distance:.2f} m")

        print("=" * 60)

        return {
            'max_height': max_height,
            'time_to_max_height': time_to_max_height,
            'total_time': total_time,
            'range': range_distance,
            'final_velocity': final_velocity,
            'is_six': is_six,
        }

    # --------------------------------------------------------------
    def plot_side_view(self, outputs):
        """Draw side-view of curved trajectory"""
        fig, ax = plt.subplots(figsize=(12, 6))

        ax.fill_between([0, outputs['range'] + 20], 0, -5, color='brown', alpha=0.5)

        ax.plot(self.trajectory_x, self.trajectory_y, 'b-', linewidth=3)
        ax.fill_between(self.trajectory_x, 0, self.trajectory_y, alpha=0.2, color='blue')

        h_idx = np.argmax(self.trajectory_y)
        ax.plot(self.trajectory_x[h_idx], self.trajectory_y[h_idx], 'r*', markersize=20)

        ax.axvline(self.boundary_distance, color='red', linestyle='--', linewidth=2)

        ax.set_xlabel("Distance (m)")
        ax.set_ylabel("Height (m)")
        ax.set_title("Side View - Projectile Trajectory")

        plt.show()

    # --------------------------------------------------------------
    def plot_trajectory(self, outputs):
        """Draw top view of cricket field + trajectory"""
        fig, ax = plt.subplots(figsize=(12, 8))

        field = Rectangle((0, 0), self.ground_length, self.ground_width,
                           edgecolor='green', facecolor='lightgreen', alpha=0.3)
        ax.add_patch(field)

        boundary = Circle((0, self.ground_width / 2), self.boundary_distance,
                           edgecolor='red', linestyle='--', fill=False)
        ax.add_patch(boundary)

        ax.plot(self.trajectory_x, [self.ground_width / 2] * len(self.trajectory_x),
                'b-', linewidth=3)

        ax.set_aspect('equal')
        ax.set_title("Top View - Cricket Field Trajectory")
        ax.set_xlim(-10, outputs['range'] + 20)
        ax.set_ylim(-10, self.ground_width + 10)

        plt.show()

    # --------------------------------------------------------------
    def get_inputs(self):
        """Get user inputs"""

        print("\n" + "=" * 60)
        print(" CRICKET PROJECTILE MOTION SIMULATOR")
        print("=" * 60)

        print("\n GROUND DIMENSIONS:")
        self.ground_length = float(input("Enter ground length (m): "))
        self.ground_width = float(input("Enter ground width (m): "))
        self.boundary_distance = float(input("Enter boundary distance (m): "))

        print("\n PROJECTILE PARAMETERS:")
        self.velocity = float(input("Enter initial velocity (m/s): "))
        self.angle = float(input("Enter launch angle (degrees): "))
        self.launch_height = float(input("Enter launch height (m): "))
        self.gravity = float(input("Enter gravity (m/s^2): "))

    # --------------------------------------------------------------
    def run(self):
        self.get_inputs()
        self.calculate_trajectory()
        outputs = self.calculate_outputs()

        print("\n Generating plots...")
        self.plot_side_view(outputs)
        self.plot_trajectory(outputs)


# --------------------------------------------------------------
if __name__ == "__main__":
    while True:
        sim = ProjectileSimulator()
        sim.run()

        again = input("\n Run another simulation? (yes/no): ").lower()
        if again not in ("yes", "y"):
            print("\n Thanks for using the Cricket Projectile Simulator!")
            break