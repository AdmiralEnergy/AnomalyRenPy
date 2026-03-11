# Anomaly - Ren'Py Visual Novel

A visual novel set in the Anomaly universe featuring Dynad and Sora.

## Project Structure

```
AnomalyRenPy/
├── game/               # Ren'Py game files
│   ├── images/        # Character sprites and backgrounds
│   │   ├── Dynad.jpg
│   │   └── SoraDesign.png
│   ├── script.rpy     # Main game script
│   ├── options.rpy    # Game configuration
│   ├── screens.rpy    # UI screens
│   └── gui.rpy        # GUI configuration
├── Anomaly.code-workspace  # VS Code/Cursor workspace
└── README.md
```

## Development Setup

### Opening the Project

**Option 1: Cursor (Recommended)**
1. Open Cursor
2. File → Open Workspace
3. Select `Anomaly.code-workspace`

**Option 2: VS Code**
1. Open VS Code
2. File → Open Workspace from File
3. Select `Anomaly.code-workspace`

**Option 3: Direct Folder**
- Simply open the `AnomalyRenPy` folder in Cursor or VS Code

### Running the Game

1. Open the Ren'Py Launcher
2. Select the "Anomaly" project (navigate to `C:\LifeOS\Projects\AnomalyRenPy`)
3. Click "Launch Project"

### Current Practice Scene

The current `script.rpy` contains a practice scene:
- **Episode 0: First Contact**
- Features Dynad discovering Sora in a crash crater
- Demonstrates:
  - Character dialogue
  - Branching choices (trust tracking)
  - Conditional paths
  - Variable management
  - Image display

## Workflow with GitHub

### Initial Setup (Already Done)
The repository is cloned from: `https://github.com/AdmiralEnergy/AnomalyRenPy.git`

### Making Changes

1. Edit files in Cursor/VS Code
2. Test in Ren'Py Launcher
3. Commit changes:
   ```bash
   git add .
   git commit -m "Description of changes"
   git push
   ```

### Syncing Between Devices

On your Surface Pro 9 or Desktop:
```bash
cd C:\LifeOS\Projects\AnomalyRenPy
git pull
```

## Asset Development

### Images
- **Sprites**: Place in `game/images/`
- **Backgrounds**: Place in `game/images/bg/` (create if needed)
- Naming: Use lowercase with underscores (e.g., `sora_happy.png`, `bg_outskirts.png`)

### Tools Available
- **OpenArt.ai**: Generate character sprites and backgrounds
- **Blender**: Create 3D animations and renders for cinematics
- **Krita**: Edit and touch up 2D assets

### Adding New Images

1. Generate/create image in OpenArt, Blender, or Krita
2. Save to `game/images/` or `game/images/bg/`
3. In `script.rpy`, reference with:
   ```renpy
   show character_name expression  # For sprites
   scene bg location               # For backgrounds
   ```

## Ren'Py Script Basics

### Character Definition
```renpy
define character_name = Character("Display Name", color="#hexcolor")
```

### Showing Images
```renpy
scene bg location with fade        # Show background
show character_name happy           # Show character sprite
```

### Dialogue
```renpy
character_name "What they say"
```

### Choices
```renpy
menu:
    "Choice 1":
        jump label1
    "Choice 2":
        jump label2
```

### Variables
```renpy
default variable_name = value      # Define at top
$ variable_name += 1               # Modify in script
```

## Next Steps

1. Test the current practice scene
2. Generate additional character expressions in OpenArt
3. Create background images for:
   - The Outskirts (metallic forest)
   - Crash crater
4. Write additional story scenes
5. Add music and sound effects to `game/audio/`

## Resources

- [Ren'Py Documentation](https://www.renpy.org/doc/html/)
- [Ren'Py Quickstart](https://www.renpy.org/doc/html/quickstart.html)
- [Ren'Py Discord](https://discord.gg/renpy)
