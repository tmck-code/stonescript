\## [[personal/code/StoneStoryRPG/Stone Story RPG|Stone Story RPG]]

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

| id               | weapon type | weapon subtype | recipe item 1     | recipe item2      |
| ---------------- | ----------- | -------------- | ----------------- | ----------------- |
| #bardiche        | bardiche    |                | `Shield`          | `Big Sword`       |
| #bardiche        | bardiche    |                | `Sword`           | `Towering Shield` |
| #heavy_crossbow  | crossbow    | heavy          | `Sword`           | `Crossbow`        |
| #repeating       | crossbow    | repeating      | `Heavy Crossbow`  | `Crossbow`        |
| #stone_crossbow  | crossbow    | stone          | `Heavy Crossbow`  | `Stone Wand`      |
| #stone_crossbow  | crossbow    | stone          | `Crossbow`        | `Stone Sword`     |
| #rune_crossbow   | crossbow    | rune           | `Stone Crossbow`  | `Runestone`       |
| #rune_crossbow   | crossbow    | rune           | `Heavy Crossbow`  | `Rune Wand`       |
| #rune_crossbow   | crossbow    | rune           | `Crossbow`        | `Rune Sword`      |
| #war_hammer      | hammer      | war            | `Sword`           | `Shield`          |
| #stone_hammer    | hammer      | stone          | `War Hammer`      | `Stone Wand`      |
| #stone_hammer    | hammer      | stone          | `Sword`           | `Stone Shield`    |
| #stone_hammer    | hammer      | stone          | `Shield`          | `Stone Sword`     |
| #rune_hammer     | hammer      | rune           | `Stone Hammer`    | `Runestone`       |
| #rune_hammer     | hammer      | rune           | `War Hammer`      | `Rune Wand`       |
| #rune_hammer     | hammer      | rune           | `Sword`           | `Rune Shield`     |
| #rune_hammer     | hammer      | rune           | `Shield`          | `Rune Sword`      |
| #heavy_hammer    | hammer      | heavy          | `War Hammer`      | `Quarterstaff`    |
| #dash            | shield      | dash           | `Shield`          | `Crossbow`        |
| #compound        | shield      | compound       | `Shield`          | `Dashing Shield`  |
| #towering        | shield      | towering       | `Shield`          | `Quarterstaff`    |
| #stone_shield    | shield      | stone          | `Shield`          | `Stone Wand`      |
| #rune_shield     | shield      | rune           | `Stone Shield`    | `Runestone`       |
| #rune_shield     | shield      | rune           | `Shield`          | `Rune Wand`       |
| #stone_staff     | staff       | stone          | `Quarterstaff`    | `Stone Wand`      |
| #rune_staff      | staff       | rune           | `Stone Staff`     | `Runestone`       |
| #rune_staff      | staff       | rune           | `Quarterstaff`    | `Rune Wand`       |
| #stone_sword     | sword       | stone          | `Sword`           | `Stone Wand`      |
| #rune_sword      | sword       | rune           | `Stone Sword`     | `Runestone`       |
| #rune_sword      | sword       | rune           | `Sword`           | `Rune Wand`       |
| #big_sword       | sword (big) |                | `Sword`           | `Quarterstaff`    |
| #big_stone_sword | sword (big) | stone          | `Big Sword`       | `Stone Wand`      |
| #big_stone_sword | sword (big) | stone          | `Sword`           | `Stone Staff`     |
| #big_stone_sword | sword (big) | stone          | `Stone Sword`     | `Quarterstaff`    |
| #big_rune_sword  | sword (big) | rune           | `Big Stone Sword` | `Runestone`       |
| #big_rune_sword  | sword (big) | rune           | `Big Sword`       | `Rune Wand`       |
| #big_rune_sword  | sword (big) | rune           | `Sword`           | `Rune Staff`      |
| #big_rune_sword  | sword (big) | rune           | `Quarterstaff`    | `Rune Sword`      |
| #rune_wand       | wand        | rune           | `Stone Wand`      | `Runestone`       |

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

| Category     | :rock: | Item                    | Cooldown ID       |
| ------------ | :----: | ----------------------- | ----------------- |
| special      |   ❓    | Mind Stone              | `mind`            |
| special      |   ❓    | Hatchet                 | `hatchet`         |
| lost item    |   🎁   | Blade of the Fallen God | `blade`           |
| lost item    |   🎁   | Cultist Mask            | `mask`            |
| lost item    |   🎁   | Skeleton Arm            | `skeleton_arm`    |
| summon       |   👻   | Cinderwisp Devour       | `cinderwisp`      |
| summon       |   👻   | Voidweaver Devour       | `voidweaver`      |
| talisman     |   💍   | Æther Talisman          | `aether_talisman` |
| talisman     |   💍   | Fire Talisman           | `fire_talisman`   |
| staff        |   🦯   | Grasping Staff          | `staff_aether`    |
| staff        |   🦯   | Infernal Staff          | `staff_fire`      |
| staff        |   🦯   | Eternity Staff          | `staff_ice`       |
| staff        |   🦯   | Berserker Staff         | `staff_poison`    |
| staff        |   🦯   | Acrobatic Staff         | `staff_stone`     |
| staff        |   🦯   | Prevention Staff        | `staff_vigor`     |
| wand         |   🪄   | Calamity Wand           | `wand_aether`     |
| wand         |   🪄   | Explosive Wand          | `wand_fire`       |
| wand         |   🪄   | Frost Wand              | `wand_ice`        |
| wand         |   🪄   | Plague Wand             | `wand_poison`     |
| wand         |   🪄   | Gravity Wand            | `wand_stone`      |
| wand         |   🪄   | Reset Wand              | `wand_vigor`      |
| heavy weapon |   🪓   | Bardiche                | `bardiche`        |
| heavy weapon |   🪓   | Heavy Hammer            | `heavy_hammer`    |
| heavy weapon |   🪓   | Quarterstaff            | `quarterstaff`    |
| shield       |   🛡   | Bashing Shield          | `bash`            |
| shield       |   🛡   | Dashing Shield          | `dash`            |

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

| \o/ | element | ability     | get from               | affixes | strong against | weak against |
| --- | ------- | ----------- | ---------------------- | ------- | -------------- | ------------ |
| 🐍  | poison  | `plague`    | #CavesOfFear ~ #Temple |         |                |              |
| 🤍  | vigor   | `reset`     | #MushroomForest        |         |                |              |
| ⭐   | æther   | `calamity`  | #HauntedHalls          |         |                |              |
| 🔥  | fire    | `explosive` | #BoilingMine           |         |                |              |
| ❄   | ice     | `frost`     | #IcyRidge              |         |                |              |
| 🞈  | stone   | `gravity`   | #DeadwoodCanyon        |         |                |              |

| staff						 | ability armor cost |
| ---------------- | ------------------ |
| Acrobatic Staff  | 3                  |
| Berserker Staff  | 7                  |
| Prevention Staff | 4                  |
| Grasping Staff   | 2                  |
| Infernal Staff   | 6                  |
| Eternity Staff   | 1                  |
 
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

