# Basics of the `os` Module

Let’s dive into the **basics** of the `os` module—those building blocks you’ll use constantly in any non‑trivial script.

## 1. Importing


All `os` functionality lives under that single import.
```
```python
import os
```

## 2. Current Working Directory

- **Why?** So you know “where” your script is running, and can build paths relative to it.

```python
cwd = os.getcwd()
print("Current folder:", cwd)
```

- **Change it** if you want to work somewhere else:

```python
os.chdir("/path/to/project")
print("Now in:", os.getcwd())
```

---

## 3. Listing Contents

- **Quick list of names** (files + subfolders):

```python
entries = os.listdir(".")    # list of strings
print(entries)
```

- **Rich, fast scan** (gives file‑type info without separate stat calls):

```python
with os.scandir(".") as it:
    for entry in it:
        kind = "DIR" if entry.is_dir() else "FILE"
        print(f"{kind:4}  {entry.name}")
```

---

## 4. Creating & Removing

### 4.1 Directories

- **Single**:

  ```python
  os.mkdir("reports")
  ```

- **Nested** (creates parents if needed):

  ```python
  os.makedirs("archive/2025/April", exist_ok=True)
  ```

- **Remove empty**:

  ```python
  os.rmdir("reports")
  ```

- **Remove nested empty tree**:

  ```python
  os.removedirs("archive/2025/April")
  ```

### 4.2 Files

- **Create an empty file**:

  ```python
  open("data.csv", "w").close()
  ```

- **Delete a file**:

  ```python
  os.remove("data.csv")
  ```

---

## 5. Renaming & Moving

```python
# rename in place, or move across folders
os.rename("log_old.txt", "log_backup.txt")

# atomic overwrite of an existing target
os.replace("tmp_output.txt", "final_output.txt")
```

---

## 6. Putting It All Together

```python
import os

# 1. Start in project root
print("Start in:", os.getcwd())

# 2. Make a results folder
os.makedirs("results", exist_ok=True)

# 3. List all .txt files
txts = [f for f in os.listdir(".") if f.endswith(".txt")]

# 4. For each, move to results/
for fn in txts:
    src = os.path.join(".", fn)
    dst = os.path.join("results", fn)
    os.replace(src, dst)   # moves/renames

# 5. Show final contents
print("Results contains:", os.listdir("results"))
```

---

🔑 **Key takeaways**:

- `getcwd()` & `chdir()` let you control your starting point.  
- `listdir()` vs `scandir()`: use `scandir()` in performance‑sensitive loops.  
- `mkdir()` / `makedirs()` and `remove()` / `rmdir()` cover most creation/deletion needs.  
- `rename()` and `replace()` handle moves and atomic overwrites.  

