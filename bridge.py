import subprocess
import sys
import json

OPENCODE_BIN = "/root/.opencode/bin/opencode"

def ask_opencode(prompt):
    try:
        # Use 'opencode run' to get reasoning
        res = subprocess.run([OPENCODE_BIN, "run", prompt], capture_output=True, text=True, timeout=60)
        return res.stdout
    except Exception as e:
        return f"OpenCode Bridge Error: {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(ask_opencode(sys.argv[1]))
    else:
        print("Usage: python3 bridge.py 'prompt'")
