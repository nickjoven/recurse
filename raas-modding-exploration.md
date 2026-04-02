# Rabbit & Steel — Modding Exploration

## Engine

Rabbit & Steel is built on **GameMaker Studio** by developer mino_dev (released May 2024). It uses the Steamworks API for online features and workshop integration.

---

## Modding Tiers

### Tier 1: Official / Trivial (Built-in Support)

The game has official Steam Workshop support ("Modding and Steel") with these categories:

| Category | Description |
|---|---|
| **Character Skins** | Cosmetic sprite replacements for playable characters. Most character sprites are saved as PNGs in the game files and are trivially replaceable. |
| **Cosmetics** | Visual modifications (effects, accessories, UI flourishes). |
| **Loot Items** | Custom loot/equipment that drops during runs and modifies player abilities. |
| **Boss Encounters** | Custom boss fights with scripted attack patterns, phases, and mechanics. |
| **Challenges** | Custom challenge modifiers or rulesets for runs. |

Official modding documentation lives on the [Rabbit and Steel Wiki (Miraheze)](https://rns.miraheze.org/wiki/Modding), organized into:
- **Items mod** — custom loot items with stat/ability effects
- **Encounter mod** — custom boss encounters with a command-based scripting system (see [Encounter commands](https://rns.miraheze.org/wiki/Modding/Encounter/commands))
- **Other mods** — community/unofficial mods

### Tier 2: Texture & Data Swaps (Low Effort, No Code)

- **Sprite/Texture replacement** — Replace PNGs in the game directory or in `data.win` (GameMaker's compiled asset bundle). Tools like TextureSwapper (from RNSModding) automate this by index.
- **Text/localization changes** — Modify strings stored in the data file for dialogue, item names, UI text.
- **Audio replacement** — Swap music/SFX files (OGG/WAV) in the game directory.
- **Color mods** — Change player colors via config files (e.g., `player_color.txt` hex codes).

### Tier 3: Gameplay Modification (Code-Level, Framework Required)

Two major modding frameworks exist:

#### RNSReloaded (Reloaded II)
- **Repository:** [github.com/NotNite/RNSReloaded](https://github.com/NotNite/RNSReloaded)
- **Language:** C# (Reloaded II mod loader)
- **Capabilities:** Exposes `IRNSReloaded` interface to access GameMaker internals directly
- **License:** AGPL-3.0

#### RNSModding (Aurie Manager)
- **Repository:** [github.com/NotNite/RNSModding](https://github.com/NotNite/RNSModding)
- **Language:** C++ (DLL-based mods loaded via Aurie Manager)
- **Note:** Aurie and Reloaded II are mutually exclusive — uninstall one before using the other

Known mods in this tier demonstrate what's possible:

| Mod | Category |
|---|---|
| **DoubleTime** | Speed/tempo modification |
| **DamageTracker** | Combat analytics overlay |
| **PermanentWinds** | Environmental mechanic override (turbulent winds always on) |
| **DebugMenuEnabler** | Exposes dev menus for shop upgrades, encounters, health stats, loot drops |
| **ReColor / PlayerColorChanger** | Runtime visual modification |
| **TextureSwapper** | Programmatic asset replacement via data.win indices |
| **FullmoonArsenal / Fullmetal / Steelheart / Nightcore** | New content (weapons, encounters, systems) |
| **RabbitSeed** | Seeded runs / RNG control |
| **JadeLakeside** | Custom environment/stage |

### Tier 4: Deep / Reverse Engineering

- **GameMaker `data.win` manipulation** — The compiled game data (sprites, scripts, objects, rooms, strings, audio) lives in `data.win`. Tools:
  - [UndertaleModTool (UTMT)](https://github.com/UnderminersTeam/UndertaleModTool) — the standard GameMaker data.win editor, supports decompiling GML scripts, editing game objects, rooms, sprites, fonts, etc.
  - [DogScepter](https://github.com/colinator27/DogScepter) — alternative data.win editor
- **GML script decompilation & patching** — UTMT can decompile GameMaker Language (GML) bytecode back to readable code. This enables:
  - Modifying game logic (damage formulas, drop rates, boss AI)
  - Adding entirely new game objects and behaviors
  - Patching networking/multiplayer code
- **Binary hooking** — RNSReloaded includes reverse engineering support (`structs.h` headers, Python rename scripts for IDA/Ghidra) for hooking the compiled GameMaker runner executable directly.
- **Cheat Engine tables** — Memory manipulation for runtime value editing (HP, damage, cooldowns). Multiple CE tables exist in the community.

---

## Categories of Possible Mods (Summary)

1. **Cosmetic / Visual**
   - Character skins & sprite replacements
   - Custom color palettes
   - UI reskins
   - Visual effects / particles
   - Environment/stage visuals

2. **Audio**
   - Music replacement
   - Sound effect replacement
   - Custom boss themes

3. **Content — Items & Equipment**
   - Custom loot items (official workshop support)
   - Modified item stats/effects
   - New item pools or drop tables

4. **Content — Encounters & Bosses**
   - Custom boss encounters (official workshop support)
   - Modified attack patterns / phases
   - New stage environments
   - Custom challenges / rulesets

5. **Gameplay Mechanics**
   - Speed/tempo modification
   - Environmental mechanic overrides
   - Class/ability rebalancing
   - Damage formula changes
   - RNG seeding / deterministic runs
   - New abilities or class mechanics

6. **Quality of Life / Utility**
   - Damage trackers / DPS meters
   - Debug menus
   - Enhanced UI / HUD overlays
   - Practice mode tools

7. **Text & Localization**
   - Dialogue modifications
   - Fan translations
   - Item/ability name/description changes

8. **Multiplayer**
   - Note: gameplay-altering mods require all players to run the same mod
   - Custom multiplayer rulesets
   - Party composition experiments

9. **Total Conversion (Theoretical)**
   - Full GML decompilation enables replacing virtually any game system
   - New character classes with original sprites and abilities
   - Entirely new dungeons/areas
   - Modified progression systems

---

## Modding Communities & Hubs

| Platform | URL |
|---|---|
| Steam Workshop | steamcommunity.com/app/2132850/workshop |
| GameBanana | gamebanana.com/mods/games/20304 |
| Nexus Mods | nexusmods.com/rabbitandsteel |
| GitHub (RNSReloaded) | github.com/NotNite/RNSReloaded |
| GitHub (RNSModding) | github.com/NotNite/RNSModding |
| Wiki (Miraheze) | rns.miraheze.org/wiki/Modding |
| Wiki (Fandom) | rabbitandsteel.fandom.com |
| Steam Discussions | steamcommunity.com/app/2132850/discussions |

---

## Key Takeaways

- **Officially supported:** Skins, cosmetics, loot items, boss encounters, and challenges via Steam Workshop
- **Trivially possible:** Any sprite/texture/audio swap (PNGs in game directory)
- **Framework-enabled:** Deep gameplay mods via RNSReloaded (C#) or Aurie Manager (C++ DLLs)
- **Reverse-engineerable:** Full GML decompilation via UndertaleModTool opens the entire game logic
- **Multiplayer constraint:** Gameplay mods require all party members to use the same modded client
