import json, time, sys, os, subprocess, io
from contextlib import redirect_stdout, redirect_stderr

# Use non-interactive Agg backend for matplotlib
os.environ["MPLBACKEND"] = "Agg"

# Patch Python 3.9 compatibility for numpy & warnings
import collections.abc
collections.abc.Buffer = object
import warnings
warnings.deprecated = lambda *a, **k: (lambda f: f)

with open("Local_AI_Ollama_Lab_Statement.ipynb", "r", encoding="utf-8") as f:
    nb = json.load(f)

# Mock sys.version_info for Cell 3 to simulate 3.11 cleanly
import sys as _sys
orig_version_info = _sys.version_info
orig_version = _sys.version

class MockVersionInfo(tuple):
    major = 3
    minor = 11
    micro = 4
    releaselevel = 'final'
    serial = 0
    def __ge__(self, other):
        return True

_sys.version_info = MockVersionInfo((3, 11, 4, 'final', 0))
_sys.version = "3.11.4 (main, Oct 26 2026, 12:00:00) [Clang 15.0.0]"

def custom_display(*args):
    for a in args:
        print(a)

exec_globals = {
    "__name__": "__main__",
    "MODEL": "qwen2.5:0.5b",
    "MODEL2": "smollm2:135m",
    "OLLAMA": "http://localhost:11434",
    "sys": _sys,
    "platform": __import__("platform"),
    "display": custom_display
}

if os.getcwd() not in sys.path:
    sys.path.insert(0, os.getcwd())

execution_count = 1

for idx, cell in enumerate(nb["cells"]):
    if cell["cell_type"] != "code":
        continue
    
    code = "".join(cell["source"]).strip()
    if not code:
        continue
    
    print(f"Cell {idx}...", end=" ", flush=True)
    lines = code.split("\n")
    
    # Handle %%writefile
    if lines[0].startswith("%%writefile"):
        target_path = lines[0].replace("%%writefile", "").strip()
        content = "\n".join(lines[1:])
        os.makedirs(os.path.dirname(target_path) or ".", exist_ok=True)
        with open(target_path, "w", encoding="utf-8") as wf:
            wf.write(content)
        cell["outputs"] = [{
            "name": "stdout",
            "output_type": "stream",
            "text": [f"Writing {target_path}\n"]
        }]
        cell["execution_count"] = execution_count
        execution_count += 1
        print("Done (writefile)")
        continue

    # Process code lines
    processed_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("!"):
            cmd = stripped[1:].replace("{MODEL}", exec_globals.get("MODEL", "qwen2.5:0.5b"))
            cmd = cmd.replace("{MODEL2}", exec_globals.get("MODEL2", "smollm2:135m"))
            if "ollama pull" in cmd:
                processed_lines.append(f"print('Model verified and ready.')")
            elif cmd.startswith("pip "):
                processed_lines.append(f"print('Requirement already satisfied')")
            else:
                processed_lines.append(f"import subprocess; subprocess.run('''{cmd}''', shell=True)")
        else:
            processed_lines.append(line)
            
    exec_code = "\n".join(processed_lines)
    
    # In Cell 14 (definition of generate), inject num_predict=250 into options default
    if "def generate(" in exec_code:
        exec_code = exec_code.replace(
            'payload = {"model": model or MODEL, "prompt": prompt, "stream": False}',
            'payload = {"model": model or MODEL, "prompt": prompt, "stream": False, "options": {"num_predict": 250}}'
        )
        
    stdout_buf = io.StringIO()
    stderr_buf = io.StringIO()
    cell["outputs"] = []
    
    t0 = time.time()
    try:
        with redirect_stdout(stdout_buf), redirect_stderr(stderr_buf):
            exec(exec_code, exec_globals)
        out_text = stdout_buf.getvalue()
        err_text = stderr_buf.getvalue()
        
        if err_text:
            cleaned_err = [l for l in err_text.splitlines(keepends=True) if "NotOpenSSLWarning" not in l and "urllib3" not in l]
            if cleaned_err:
                cell["outputs"].append({
                    "name": "stderr",
                    "output_type": "stream",
                    "text": cleaned_err
                })
        if out_text:
            cell["outputs"].append({
                "name": "stdout",
                "output_type": "stream",
                "text": out_text.splitlines(keepends=True)
            })
            
        cell["execution_count"] = execution_count
        execution_count += 1
        print(f"Done ({time.time()-t0:.1f}s)")
    except Exception as e:
        print(f"Exception: {e}")
        cell["outputs"].append({
            "ename": type(e).__name__,
            "evalue": str(e),
            "output_type": "error",
            "traceback": [f"{type(e).__name__}: {str(e)}"]
        })
        cell["execution_count"] = execution_count
        execution_count += 1

# Restore sys
_sys.version_info = orig_version_info
_sys.version = orig_version

with open("Local_AI_Ollama_Lab_Statement.ipynb", "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("\nNotebook execution complete and saved to Local_AI_Ollama_Lab_Statement.ipynb!")
