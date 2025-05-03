import math

def calculate_trigonometry():
    print("=" * 50)
    print("📐 Welcome to the Trigonometric Calculator using Math Module")
    print("=" * 50)

    # Ask user to enter an angle in degrees
    angle_deg = float(input("Enter an angle in degrees: "))

    # Convert degrees to radians
    angle_rad = math.radians(angle_deg)

    # Calculate trigonometric values
    sine = math.sin(angle_rad)
    cosine = math.cos(angle_rad)
    tangent = math.tan(angle_rad)

    # Display the results
    print(f"\nTrigonometric values for {angle_deg}°:")
    print(f"  🔹 Sine     : {sine:.4f}")
    print(f"  🔹 Cosine   : {cosine:.4f}")
    print(f"  🔹 Tangent  : {tangent:.4f}")

    print("\n✅ Calculation completed successfully!")
    print("=" * 50)

# Run the function
calculate_trigonometry()
