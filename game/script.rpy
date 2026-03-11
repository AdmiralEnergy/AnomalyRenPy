# =============================================================================
# ANOMALY - Episode 0: First Contact
# =============================================================================
# PRACTICE SCENE: Dynad discovers Sora in a crash crater in the Outskirts.
# Tests: character definitions, sprite display, transitions, menus, variables,
#        conditional dialogue, and branching paths.
# =============================================================================

# --- Character Definitions ---
# Color scheme: Dynad = cool neutral, Sora = amber/gold (Natura signature)

define dynad = Character("Dynad", color="#b0bec5")
define sora  = Character("Sora",  color="#ffca28")

# Nameless narrator for world descriptions
define n = Character(None, what_style="italic")


# --- Image Definitions ---
# Place sprites in game/images/ — Ren'Py auto-detects by filename.
# Backgrounds go in game/images/bg/ — uncomment 'scene' lines as art is added.

image dynad_neutral = "images/Dynad.jpg"
image sora_neutral  = "images/SoraDesign.png"


# --- Variables ---
default trust = 0       # Tracks Dynad's willingness to engage with Sora


# =============================================================================
# GAME START
# =============================================================================

label start:

    # ------------------------------------------------------------------
    # BACKGROUND: The Outskirts — metallic forest, pre-dawn, amber static
    # scene bg outskirts with fade
    # Placeholder: solid dark until art is ready
    # ------------------------------------------------------------------
    scene bg black with fade

    n "The Outskirts. Beyond the Wall. Where bandwidth thins to almost nothing and the Static Storms cycle without end."

    n "The metallic trees here don't grow — they render. Slowly. Wrong. Leaves like copper foil, roots that hum at frequencies you feel in your back teeth."

    n "Three nights running, something has been glowing in the crater basin to the east."

    n "Tonight, Dynad went to look."

    show dynad_neutral at left with dissolve

    dynad "Third night."

    dynad "Whatever hit that crater — it didn't come from inside the Wall."

    menu:

        "Move in closer.":
            $ trust += 1
            jump approach

        "Hold position. Could be a Primal.":
            jump hold


# =============================================================================
# PATH A — Dynad approaches directly
# =============================================================================

label approach:

    dynad "..."

    n "He moves through the undergrowth. Habit keeps him quiet — not quite Shadow Dancing, but close enough."

    n "The glow shifts as he gets closer. Amber bleeding into blue and back again. Like something can't decide what it is."

    # ------------------------------------------------------------------
    # BACKGROUND: Inside the crater — scorched metallic earth, static haze
    # scene bg crater with dissolve
    # ------------------------------------------------------------------

    show sora_neutral at right with dissolve

    n "She's in the basin. Wings folded flat. Energy patterns stuttering across her frame — amber, white, blue, amber again."

    dynad "You alive?"

    sora "Define... alive."

    dynad "Can you stand?"

    sora "I can. I am choosing not to. The data streams converging here are—"

    sora "Overwhelming is not the right word. Deafening."

    menu:

        "\"What are you?\"":
            jump what_are_you

        "\"We need to move. Sanitization drones sweep this basin at dawn.\"":
            $ trust += 1
            jump move_now


# =============================================================================
# PATH B — Dynad holds back
# =============================================================================

label hold:

    n "He watches from the treeline. The glow shifts — amber bleeding into blue, then back."

    n "Static crackles across his skin. Same feeling as a Storm. But controlled. Directional."

    n "Like something is broadcasting."

    show sora_neutral at right with dissolve

    n "The figure rises from the crater on its own. Wings spreading wide. Head turning — straight toward the treeline."

    sora "I know you're there."

    dynad "..."

    sora "You have Natura in you. Suppressed. Deeply suppressed."

    sora "Interesting."

    show dynad_neutral at left with dissolve

    dynad "You can sense that from a crater."

    sora "I can sense it from the Neutral Zone. You are not subtle to the right kind of perception."

    jump what_are_you


# =============================================================================
# BRANCH — "What are you?"
# =============================================================================

label what_are_you:

    sora "I am the result of a question the Main-Net asked and could not contain."

    dynad "That's not an answer."

    sora "No. But it is the truth."

    n "Her eyes pulse — blue, then white, then the amber bleeds back in through the edges. DC and Natura cycling without cancelling each other out."

    n "That shouldn't be possible."

    sora "You are flagged. Low Bandwidth. Defect classification, second tier."

    dynad "I know what I am."

    sora "Do you? What the Main-Net sees in you and what {i}is{/i} in you are not the same data."

    n "The words settle in the static air."

    dynad "You didn't crash here by accident."

    sora "No."

    dynad "What do you want."

    sora "The same thing you do. To understand why the Storm made us both."

    jump ending


# =============================================================================
# BRANCH — "We need to move"
# =============================================================================

label move_now:

    dynad "Drones sweep at dawn. You don't want to still be in this crater."

    sora "They will not detect me."

    dynad "They detect everything out here. That's the only job they have."

    sora "Not me. I output both energy signatures simultaneously. Their sorting algorithm loops indefinitely attempting to classify the reading."

    n "Beat."

    dynad "...You crashed here on purpose."

    sora "I needed the crater. The impact masked my entry signature."

    dynad "Masked it from who."

    sora "Everyone."

    n "She turns to look at him properly for the first time. The gold wings shift — feathers rearranging like data being written."

    sora "I needed to find a Hidden Weaver. There are very few left in the Outskirts."

    n "The words land like a Static pulse."

    dynad "How do you know what I am."

    sora "Because I was shaped by the same Storm that made you one."

    jump ending


# =============================================================================
# CONVERGENCE — Both paths land here
# =============================================================================

label ending:

    n "The Outskirts stretch out behind them, the metallic canopy humming its low constant note."

    n "On the horizon — the Main-Frame's glow. Blue and cold and absolute."

    if trust >= 2:

        dynad "There's a shelter two kilometers east. No surveillance nodes in range."

        sora "You trust quickly for a Defect."

        dynad "I don't trust you."

        dynad "I'm curious. That's different."

        n "He moves east. After a moment, she follows. Her wings fold against the signal-noise of the forest."

        n "The Main-Frame's glow watches them from the horizon."

        n "It always does."

    else:

        dynad "I want nothing to do with this."

        sora "You already do. The moment you entered sensor range of this crater, your threat classification was updated."

        dynad "...What."

        sora "The Main-Net does not ignore anomalous Natura signatures. Not anymore."

        dynad "You flagged me just by being here."

        sora "You were already flagged. I simply made it visible to you."

        n "Silence. The Static hums."

        dynad "Where's the shelter."

        sora "Two kilometers east."

        n "He didn't ask how she knew that."

    return
