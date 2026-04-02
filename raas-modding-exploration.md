# Rabbit & Steel — Modding Exploration

## Engine

Rabbit & Steel is built on **GameMaker Studio (YYC — YoYo Compiler)** by developer mino_dev (released May 2024). The YYC compilation means game code is compiled to **native C++** rather than running as GML bytecode — this is a critical distinction that affects what modding approaches are viable. The game uses the Steamworks API for networking, achievements, cloud saves, and Workshop integration.

---

## File Structure

### Unpacked assets (directly accessible)
- **Character sprites** — PNGs in `Steam/steamapps/common/Rabbit and Steel/Animations/`
  - Sprite sheets are **12500x500 pixels** (25 frames of 500x500 each)
- **Mod definitions** — Spreadsheet files for items and encounters, placed in the game's `Mods` folder
- **Config files** — Plain text (`player_color.txt`, `encounter.txt`, `debug.txt`)

### Packed assets (`data.win`)
The standard GameMaker WAD/IFF container (`FORM` header, `GEN8` chunk). Contains:
- Sprites, texture pages, fonts, shaders
- Sounds (BGM/SFX) — some in separate `audiogroupN.dat` files
- Rooms (level/stage layouts)
- Objects (game object definitions)
- String tables

**Important:** Because R&S is YYC-compiled, **game code lives in the native executable**, NOT as bytecode in `data.win`. You cannot decompile GML code from `data.win` the way you can with VM-compiled GameMaker games like Undertale.

---

## Modding Tiers

### Tier 1: Official / Trivial (Built-in Support)

Steam Workshop support ("Modding and Steel") was added in **Patch 1.0.4.0**. The Workshop hosts **593+ items** across these official categories:

| Category | Count | Description |
|---|---|---|
| **Character Skins** | ~422 | Cosmetic sprite replacements. Trivially replaceable PNGs. |
| **Cosmetics** | ~356 | Visual modifications (effects, accessories, UI flourishes). |
| **Loot Items** | ~100 | Custom equipment with stat/ability effects. |
| **Boss Encounters** | ~31 | Custom boss fights with scripted attack patterns and phases. |
| **Challenges** | ~26 | Custom challenge modifiers or rulesets for runs. |

The official mod system uses a **spreadsheet-based API** with functions like `tset_strength_def`, `tset_critratio`, `bp_showgroups`, `tpat_hb_add_cooldown`, etc. Mods are placed in the game's `Mods` folder and activated via **Options > Mods**. For encounter mods in multiplayer, only the host needs the mod active.

Official modding documentation: [Rabbit and Steel Wiki (Miraheze)](https://rns.miraheze.org/wiki/Modding)
- [Items mod](https://rns.miraheze.org/wiki/Modding) — custom loot items with stat/ability effects
- [Encounter mod](https://rns.miraheze.org/wiki/Modding/Encounter) — custom boss encounters via command scripting
- [Encounter commands reference](https://rns.miraheze.org/wiki/Modding/Encounter/commands)

The February 2026 **"Extra Mode"** update added new stats and patterns, though most new functionality is not yet exposed in the mod API.

### Tier 2: Asset Swaps (No Code)

- **Sprite/Texture replacement** — Swap PNGs in `Animations/` or use TextureSwapper to replace packed textures in `data.win` by index.
- **Text/localization changes** — Edit string tables in `data.win` via UndertaleModTool.
- **Audio replacement** — Swap music/SFX files (OGG/WAV) in the game directory or `data.win`.
- **Color mods** — Edit `player_color.txt` with hex color codes.

### Tier 3: Gameplay Modification (Native Code Frameworks)

Two major modding frameworks exist (mutually exclusive — uninstall one before using the other):

#### RNSReloaded (Reloaded II) — Current / Recommended
- **Repository:** [github.com/NotNite/RNSReloaded](https://github.com/NotNite/RNSReloaded)
- **Language:** C# (Reloaded II mod loader)
- **Capabilities:** Exposes `IRNSReloaded` interface to access GameMaker internals directly
- **Contains:** 18+ mod projects, `structs.h` headers, Python rename scripts for IDA/Ghidra
- **License:** AGPL-3.0

#### RNSModding (Aurie Manager) — Legacy / Archived
- **Repository:** [github.com/NotNite/RNSModding](https://github.com/NotNite/RNSModding)
- **Language:** C++ (DLL-based mods via Aurie Manager)
- **Status:** Archived, superseded by RNSReloaded

#### General GameMaker Native Modding Tools
| Tool | Purpose |
|---|---|
| [Aurie Framework](https://github.com/AurieFramework/Aurie) | Native x86/x64 modding framework for GameMaker games. Runtime module loading, atomic inline hooking (SafetyHook), midfunction hooking, pre-entrypoint code execution. |
| [YYToolkit (YYTK)](https://github.com/AurieFramework/YYToolkit) | Built on Aurie. Exposes GameMaker runtime internals for C++ mods. The definitive internal modding tool for GameMaker. |

Known mods demonstrating what's possible at this tier:

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
| **SteelYourself** | Force specific boss encounters |
| **Ice** | New gameplay mechanics |
| **Bounty** | Custom reward systems |

### Tier 4: Deep / Reverse Engineering

- **`data.win` manipulation** — [UndertaleModTool (UTMT)](https://github.com/UnderminersTeam/UndertaleModTool) can open, explore, and edit `data.win` for asset extraction/replacement (textures, sounds, sprites, fonts, rooms, objects). Works on R&S for assets even though code is YYC-compiled.
  - Additional tools: [DogScepter](https://github.com/colinator27/DogScepter), [GMExtract](https://github.com/puggsoy/GMExtract), [gm_data_win](https://github.com/jam1garner/gm_data_win) (Rust)
- **Binary hooking / reverse engineering** — RNSReloaded ships `structs.h` and `rename.py` for IDA/Ghidra to annotate the native executable. This is the path for deep gameplay changes since GML decompilation is not available.
- **Cheat Engine tables** — Runtime memory manipulation (HP, damage, cooldowns). Multiple CE tables exist in the community.

**Key limitation:** Unlike VM-compiled GameMaker games (Undertale, Deltarune), R&S's YYC compilation means you **cannot** decompile and edit GML source code. Deep mods must use native hooking (Aurie/YYTK or Reloaded II) rather than GML code patching.

---

## Categories of Possible Mods (Summary)

1. **Cosmetic / Visual**
   - Character skins & sprite replacements (~422 on Workshop)
   - Custom color palettes
   - UI reskins
   - Visual effects / particles
   - Environment/stage visuals
   - Cosmetic accessories (~356 on Workshop)

2. **Audio**
   - Music replacement
   - Sound effect replacement
   - Custom boss themes

3. **Content — Items & Equipment**
   - Custom loot items via official spreadsheet API (~100 on Workshop)
   - Modified item stats/effects
   - New item pools or drop tables

4. **Content — Encounters & Bosses**
   - Custom boss encounters via official encounter API (~31 on Workshop)
   - Modified attack patterns / phases
   - New stage environments
   - Custom challenges / rulesets (~26 on Workshop)

5. **Gameplay Mechanics**
   - Speed/tempo modification
   - Environmental mechanic overrides
   - Class/ability rebalancing
   - RNG seeding / deterministic runs
   - New abilities or class mechanics
   - Force specific encounters

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
   - Gameplay-altering mods auto-segregate modded clients from vanilla players
   - Custom multiplayer rulesets
   - Encounter mods only require the host to have them active
   - Party composition experiments

9. **Total Conversion (Theoretical)**
   - Requires native hooking (no GML decompilation path)
   - New character classes with original sprites and abilities
   - Entirely new dungeons/areas
   - Modified progression systems
   - Substantially harder than for VM-compiled GameMaker games

---

## Modding Communities & Hubs

| Platform | URL |
|---|---|
| Steam Workshop | steamcommunity.com/app/2132850/workshop |
| GameBanana | gamebanana.com/mods/games/20304 |
| Nexus Mods | nexusmods.com/rabbitandsteel |
| GitHub (RNSReloaded) | github.com/NotNite/RNSReloaded |
| GitHub (RNSModding) | github.com/NotNite/RNSModding |
| SourceHut (Encounter Mods) | sr.ht/~syx/RnS-EncounterMods/ |
| Wiki (Miraheze) | rns.miraheze.org/wiki/Modding |
| Wiki (Fandom) | rabbitandsteel.fandom.com |
| Steam Discussions | steamcommunity.com/app/2132850/discussions |
| Official Discord | discord.gg/mns |

---

## Key Takeaways

- **Officially supported:** Skins, cosmetics, loot items, boss encounters, and challenges via Steam Workshop (593+ items). Uses a spreadsheet-based API.
- **Trivially possible:** Sprite/texture/audio swaps — character sprites are plain PNGs in `Animations/`.
- **Framework-enabled:** Deep gameplay mods via RNSReloaded (C#, Reloaded II) — the current recommended path. 18+ existing mod projects.
- **YYC constraint:** Game code is natively compiled, NOT bytecode. GML decompilation (the Undertale approach) does NOT work. Deep mods require native hooking via Aurie/YYTK or Reloaded II.
- **Multiplayer constraint:** Gameplay mods auto-segregate modded from vanilla clients. Encounter mods only need the host.
- **Active community:** Led by NotNite on GitHub, with hubs on Steam Workshop, GameBanana, Nexus Mods, and the official Discord.
