# Mathcrowd manim project collection

## Recent Projects

* [2020.05.25 arc in rectangle](project/2020.05.25.arc.in.rectangle)

## Project Structure

```
├── manim
├── projects
│   ├── [date].[project_name]
│       ├── assets 
        ├── videos
        ├── images 
        ├── custom_config.yml 
        ├── start.py
        ├── render.sh

```

`build.sh` example:

```bash
#!/bin/bash

# Write the scene to a file (video).
manimgl -w start.py Scene1
# Write the scene to a file (final frame image).
manimgl -s start.py Scene1
```

## How to use

### Software Requirements

System requirements are FFmpeg, OpenGL and LaTeX (optional, if you want to use LaTeX). For Linux, Pango along with its development headers are required.

### Add manim as submodule (For repo admin only)

```bash
git submodule add https://github.com/3b1b/manim.git manim
```

### Upgrade and install manim

```bash
git submodule update --recursive --init
git submodule update --recursive --remote
cd manim
pip install -e .
```

## License
This project falls under the MIT license.