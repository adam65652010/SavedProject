# SavedProject
SavedProject Scripts

## Python script: save random script found in servers

Use `Scripts/save_random_script.py` to search one or more server directories for script files and copy one random match to an output directory.

### Example

```bash
python3 Scripts/save_random_script.py \
  --servers /srv/server-a /srv/server-b \
  --output-dir ./saved_scripts
```
