# 插画提示词（GenerateImage）

全部规则：图里不能有任何文字、字母、数字、符号或 UI。深色场景统一用夜空底色 #1B1F3B（实际出图约 #010D2D～#020D2B，和 base.css 的 --night 一致）；单个道具或角色要用纯色底，方便抠图。

## 封面主视觉（p1，4:3）
16-bit retro video game title screen pixel art scene, wide: a friendly blue pixel robot standing on a grassy pixel hill next to a big beige CRT computer with a glowing blue screen, a starry night sky with pixel stars and a large pixel moon, distant pixel city skyline silhouette, small floating pixel cubes and sparkles. Crisp hard-edged pixels, limited SNES palette, no anti-aliasing. The top 35% of the image is only plain dark navy sky color #1B1F3B with a few tiny stars (empty space for a title). Absolutely no text, no letters, no numbers, no symbols, no UI.
→ 每篇换主体：把 "next to a big beige CRT computer" 换成和本篇概念相关的物件，机器人保持同一个蓝色小机器人，整个系列认得出来。

## 场景大图（内页，16:9）
16-bit pixel art game scene, wide: a small blue pixel robot <在做什么/在哪里>. Pixel grass, a few pixel trees and rocks, dark navy night sky #1B1F3B with tiny pixel stars. Crisp hard-edged pixels, SNES palette, no anti-aliasing. Absolutely no text, no letters, no numbers, no question marks, no symbols, no UI.
（post01 p3 用的是：standing at a fork in a pixel dirt road; the left path leads to a green pixel flag on a hill, the right path ends at a cracked broken bridge over a gap）

## 存档点（收尾页，16:9）
16-bit pixel art RPG save point scene: a glowing cyan pixel crystal floating above a small stone pedestal, with a small blue pixel robot standing beside it, pixel sparkles around, a treasure chest opened with golden glow on the other side. Crisp hard-edged pixels, SNES palette, no anti-aliasing. Plain flat solid dark navy background #1B1F3B. Absolutely no text, no letters, no numbers, no symbols, no UI.
→ 可以每篇复用 example_post01/img/p04_save_crop.jpg，不必重出。

## 道具图标（16:9，一排五个，奶油底）
Retro RPG inventory item icons in 16-bit pixel art, five separate items in one horizontal row with generous even spacing: <物件1>, <物件2>, … Each item same size, crisp hard pixels, dark outlines, warm limited palette. Plain flat solid cream background #FEF6E4. Absolutely no text, no letters, no numbers.
→ 出图后用 tools/cutout.py 抠图，放进 assets/items/。
