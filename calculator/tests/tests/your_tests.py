import subprocess


def run_calculator(args):
    """Helper function to run the calculator with given arguments and return output."""
    result = subprocess.run(
        ["../calculator/calculator"] + args,
        capture_output=True,
        text=True
    )
    return result


def test_addition():
    """Test that the calculator correctly adds two numbers."""
    result = run_calculator(["-q", "3", "+", "5"])
    assert "8" in result.stdout, f"Expected 8 in output, got: {result.stdout}"


def test_subtraction():
    """Test that the calculator correctly subtracts two numbers."""
    result = run_calculator(["-q", "10", "-", "4"])
    assert "6" in result.stdout, f"Expected 6 in output, got: {result.stdout}"
