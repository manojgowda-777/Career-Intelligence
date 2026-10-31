
# Run the Career Intelligence job collection and analysis pipeline.

import subprocess
import sys


def run_step(script_name, inputs):
    """Run an existing script and supply its input choices."""
    print(f"\n{'=' * 55}")
    print(f"Running: {script_name}")
    print("=" * 55)

    input_text = "\n".join(inputs) + "\n"

    result = subprocess.run(
        [sys.executable, script_name],
        input=input_text,
        text=True
    )

    if result.returncode != 0:
        print(f"\nPipeline stopped: {script_name} failed.")
        sys.exit(result.returncode)


def main():
    role = input("Enter the job role: ").strip()

    if not role:
        print("Please enter a job role.")
        return

    print("\nChoose search region:")
    print("1. India")
    print("2. International / Remote")
    print("3. Both")

    choice = input("Enter your choice (1-3): ").strip()

    if choice not in {"1", "2", "3"}:
        print("Invalid choice.")
        return

    # Run collection, cleaning, and skill analysis in order.
    run_step("job_collector.py", [role, choice])
    run_step("job_preprocessor.py", [choice, role])
    run_step("skill_extractor.py", [choice, role])

    print("\n" + "=" * 55)
    print("CAREER INTELLIGENCE PIPELINE COMPLETED")
    print("=" * 55)


if __name__ == "__main__":
    main()
