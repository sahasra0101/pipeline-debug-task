import subprocess
import sys

def test_app_runs_successfully():
    # Run the app.py script
    result = subprocess.run([sys.executable, 'app.py'], capture_output=True, text=True)
    # Check that it ran without error
    assert result.returncode == 0
    # Check the output
    assert "DevOps Pipeline Debug Success" in result.stdout