## [[personal/code/StoneStoryRPG/Stone Story RPG|Stone Story RPG]]

- [[#Crafting|Crafting]]
	- [[#Crafting#Number of items needed for upgrade|Number of items needed for upgrade]]
	- [[#Crafting#Crafting Recipes|Crafting Recipes]]
- [[#Cooldown|Cooldown]]
	- [[#Cooldown#affixes|affixes]]

---

## Crafting

### Number of items needed for upgrade
#upgrade

| ***level*** | ***2*** | ***3*** | ***4*** | ***5*** | ***6*** | ***7*** | ***8*** | ***9*** | ***10*** |
| ----------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | -------- |
| **items**   | 4       | 8       | 16      | 32      | 64      | 128     | 256     | 512     | 1024     |

### Crafting Recipes
#crafting #recipes

| weapon type | id               | recipe item 1     | recipe item2      |
| ----------- | ---------------- | ----------------- | ----------------- |
| bardiche    | #bardiche        | `Shield`          | `Big Sword`       |
| bardiche    | #bardiche        | `Sword`           | `Towering Shield` |
| crossbow    | #heavy_crossbow  | `Sword`           | `Crossbow`        |
| crossbow    | #repeating       | `Heavy Crossbow`  | `Crossbow`        |
| crossbow    | #stone_crossbow  | `Heavy Crossbow`  | `Stone Wand`      |
| crossbow    | #stone_crossbow  | `Crossbow`        | `Stone Sword`     |
| crossbow    | #rune_crossbow   | `Stone Crossbow`  | `Runestone`       |
| crossbow    | #rune_crossbow   | `Heavy Crossbow`  | `Rune Wand`       |
| crossbow    | #rune_crossbow   | `Crossbow`        | `Rune Sword`      |
| hammer      | #war_hammer      | `Sword`           | `Shield`          |
| hammer      | #stone_hammer    | `War Hammer`      | `Stone Wand`      |
| hammer      | #stone_hammer    | `Sword`           | `Stone Shield`    |
| hammer      | #stone_hammer    | `Shield`          | `Stone Sword`     |
| hammer      | #rune_hammer     | `Stone Hammer`    | `Runestone`       |
| hammer      | #rune_hammer     | `War Hammer`      | `Rune Wand`       |
| hammer      | #rune_hammer     | `Sword`           | `Rune Shield`     |
| hammer      | #rune_hammer     | `Shield`          | `Rune Sword`      |
| hammer      | #heavy_hammer    | `War Hammer`      | `Quarterstaff`    |
| shield      | #dash            | `Shield`          | `Crossbow`        |
| shield      | #compound        | `Shield`          | `Dashing Shield`  |
| shield      | #towering        | `Shield`          | `Quarterstaff`    |
| shield      | #stone_shield    | `Shield`          | `Stone Wand`      |
| shield      | #rune_shield     | `Stone Shield`    | `Runestone`       |
| shield      | #rune_shield     | `Shield`          | `Rune Wand`       |
| staff       | #stone_staff     | `Quarterstaff`    | `Stone Wand`      |
| staff       | #rune_staff      | `Stone Staff`     | `Runestone`       |
| staff       | #rune_staff      | `Quarterstaff`    | `Rune Wand`       |
| sword       | #stone_sword     | `Sword`           | `Stone Wand`      |
| wand        | #rune_wand       | `Stone Wand`      | `Runestone`       |
| big sword   | #big_sword       | `Sword`           | `Quarterstaff`    |
| big sword   | #big_stone_sword | `Big Sword`       | `Stone Wand`      |
| big sword   | #big_stone_sword | `Sword`           | `Stone Staff`     |
| big sword   | #big_stone_sword | `Stone Sword`     | `Quarterstaff`    |
| big sword   | #big_rune_sword  | `Big Stone Sword` | `Runestone`       |
| big sword   | #big_rune_sword  | `Big Sword`       | `Rune Wand`       |
| big sword   | #big_rune_sword  | `Sword`           | `Rune Staff`      |
| big sword   | #big_rune_sword  | `Quarterstaff`    | `Rune Sword`      |
| sword       | #rune_sword      | `Stone Sword`     | `Runestone`       |
| sword       | #rune_sword      | `Sword`           | `Rune Wand`       |

### Brewing


| Ing. 1   | Ing. 2   | Name      | Effect                                                                             |
| -------- | -------- | --------- | ---------------------------------------------------------------------------------- |
| 20 Stone | -        | Strength  | For 10s (or 300f), your attacks stun for 0.5s (or 15f) and deal 3x damage to armor |
| 20 Wood  | -        | Experience| For 30s (or 900f), gain +1 experience and +1 ki per enemy killed                   |
| 20 Tar   | -        | Healing   | Heal health to 100%                                                                |
| 20 Bronze| -        | Lightning | Deal 200 damage to all enemies on screen                                           |
| 10 Tar   | 10 Bronze| Vampiric  | For 20s (or 600f), gain health equal to 20% damage dealt                           |
| 10 Stone | 10 Bronze| Lucky     | For 6s (or 180f), your attacks have 100% critical chance                           |
| 10 Wood  | 10 Bronze| Berserk   | For 10s (or 300f), you gain +15 attack speed                                       |
| 10 Wood  | 10 Tar   | Cleansing | Heal half your health and clear all negative debuffs                               |
| 10 Stone | 10 Tar   | Defensive | Heal half your health and gain armor equal to your max health                      |
| 10 Wood  | 10 Stone | Invisibility	For 15s (or 450f), you gain 100% evasion                                         |

### Cooldown
#cooldown

| Item                    | Cooldown ID       |
| ----------------------- | ----------------- |
| Æther Talisman          | `aether_talisman` |
| Bardiche                | `bardiche`        |
| Bashing Shield          | `bash`            |
| Blade of the Fallen God | `blade`           |
| Cinderwisp Devour       | `cinderwisp`      |
| Dashing Shield          | `dash`            |
| Fire Talisman           | `fire_talisman`   |
| Hatchet                 | `hatchet`         |
| Heavy Hammer            | `heavy_hammer`    |
| Cultist Mask            | `mask`            |
| Mind Stone              | `mind`            |
| Quarterstaff            | `quarterstaff`    |
| Skeleton Arm            | `skeleton_arm`    |
| Grasping Staff          | `staff_aether`    |
| Infernal Staff          | `staff_fire`      |
| Eternity Staff          | `staff_ice`       |
| Berserker Staff         | `staff_poison`    |
| Acrobatic Staff         | `staff_stone`     |
| Prevention Staff        | `staff_vigor`     |
| Voidweaver Devour       | `voidweaver`      |
| Calamity Wand           | `wand_aether`     |
| Explosive Wand          | `wand_fire`       |
| Frost Wand              | `wand_ice`        |
| Plague Wand             | `wand_poison`     |
| Gravity Wand            | `wand_stone`      |
| Reset Wand              | `wand_vigor`      |

### affixes
#affixes

| type    | affix | description                                                                                     |
| ------- | ----- | ----------------------------------------------------------------------------------------------- |
| general | **D** | *stronger elemental damage*<br>much higher damage on effective element                          |
| general | **d** | *weaker elemental damage*<br>much lower damage on effective element compared to D               |
| general | **A** | *stronger armour on engage*<br>much higher armour on engaging with effective element            |
| general | **a** | *weaker armour on engage*<br>much lower damage on engaging with effective element compared to A |
| poison  | **P** | *weaken*<br>lowers foe damage                                                                   |
| poison  | **p** | *empower*<br>increases player damage                                                            |
| vigor   | **L** | *lifesteal*<br>chance to heal from damaging                                                     |
| vigor   | **h** | *heal*<br>chance to heal from being hit                                                         |
| aether  | **U** | *unmake*<br>unmakes foes from damaging                                                          |
| aether  | **u** | *unmake*<br>unmakes foes from being hit by them                                                 |
| fire    | **F** | *fire or dot*<br>damage over time afflicted by attacking                                        |
| fire    | **f** | *fire or dot*<br>damage over time afflicted by being hit                                        |
| ice     | **I** | *ice or chill*<br>chill afflicted by attacking                                                  |
| ice     | **i** | *ice or chill*<br>chill afflicted by being hit                                                  |

## Elements

| element | symbol | get from                 | combo version | affixes | strong against | weak against |
| ------- | ------ | ------------------------ | ------------- | ------- | -------------- | ------------ |
| poison  | 🐍     | #CavesOfFear <br>#Temple | `plague`      |         |                |              |
| vigor   | 🤍     | #MushroomForest          | `reset`       |         |                |              |
| æther   | ⭐      | #HauntedHalls            | `calamity`    |         |                |              |
| fire    | 🔥     | #BoilingMine             | `explosive`   |         |                |              |
| ice     | ❄      | #IcyRidge                | `frost`       |         |                |              |
| stone   | 🞈     | #DeadwoodCanyon          | `gravity`     |         |                |              |

 
## Items

---

## War Hammer
#war_hammer

[wiki: War Hammer](https://stonestoryrpg.miraheze.org/wiki/War_Hammer)

---

## Heavy Crossbow
#heavy_crossbow

[wiki: Heavy Crossbow](https://stonestoryrpg.miraheze.org/wiki/Heavy_Crossbow)

---

## Repeating Crossbow
#repeating_crossbow

[wiki: Repeating Crossbow](https://stonestoryrpg.miraheze.org/wiki/Repeating_Crossbow)

---

## Dashing Shield
#dashing_shield

[wiki: Dashing Shield](https://stonestoryrpg.miraheze.org/wiki/Dashing_Shield)

---

## Compound Shield
#compound_shield

[wiki: Compound Shield](https://stonestoryrpg.miraheze.org/wiki/Compound_Shield)

---

## Towering Shield
#towering_shield

[wiki: Towering Shield](https://stonestoryrpg.miraheze.org/wiki/Towering_Shield)

---

## Stone Crossbow
#stone_crossbow

[wiki: Stone Crossbow](https://stonestoryrpg.miraheze.org/wiki/Stone_Crossbow)

---

## Stone Hammer
#stone_hammer

[wiki: Stone Hammer](https://stonestoryrpg.miraheze.org/wiki/Stone_Hammer)

---

## Stone Shield
#stone_shield

[wiki: Stone Shield](https://stonestoryrpg.miraheze.org/wiki/Stone_Shield)

---

## Stone Staff
#stone_staff

[wiki: Stone Staff](https://stonestoryrpg.miraheze.org/wiki/Stone_Staff)

---

## Stone Sword
#stone_sword

[wiki: Stone Sword](https://stonestoryrpg.miraheze.org/wiki/Stone_Sword)

---

## Rune Wand
#rune_wand

[wiki: Rune Wand](https://stonestoryrpg.miraheze.org/wiki/Rune_Wand)

---

## Big Sword
#big_sword

[wiki: Big Sword](https://stonestoryrpg.miraheze.org/wiki/Big_Sword)

---

## Big Stone Sword

[wiki: Big Stone Sword](https://stonestoryrpg.miraheze.org/wiki/Big_Stone_Sword)

---

## Big Rune Sword

[wiki: Big Rune Sword](https://stonestoryrpg.miraheze.org/wiki/Big_Rune_Sword)

---

## Rune Crossbow
#rune_crossbow

[wiki: Rune Crossbow](https://stonestoryrpg.miraheze.org/wiki/Rune_Crossbow)

---

## Rune Hammer
#rune_hammer

[wiki: Rune Hammer](https://stonestoryrpg.miraheze.org/wiki/Rune_Hammer)

---

## Rune Shield
#rune_shield

[wiki: Rune Shield](https://stonestoryrpg.miraheze.org/wiki/Rune_Shield)

---

## Rune Staff
#rune_staff

[wiki: Rune Staff](https://stonestoryrpg.miraheze.org/wiki/Rune_Staff)

---

## Rune Sword
#rune_sword

[wiki: Rune Sword](https://stonestoryrpg.miraheze.org/wiki/Rune_Sword)

---

## Bardiche
#bardiche

[wiki: Bardiche](https://stonestoryrpg.miraheze.org/wiki/Bardiche)

---

## Heavy Hammer
#heavy_hammer

[wiki: Heavy Hammer](https://stonestoryrpg.miraheze.org/wiki/Heavy_Hammer
)

---

