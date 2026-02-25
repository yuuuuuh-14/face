[🇰🇷 한국어 문서](05-frontend-stack.md)

# [05] In-depth Frontend Anatomy: Angular and Sci-Fi UI Design

The frontend repository is the jewel of the BCC system. No matter how sophisticated the data is, if the way it's presented is clunky, its value drops.
We removed JavaScript templates (Jinja, etc.) and adopted **Angular (v15+)**, the standard for enterprise modern web apps.

## 1. Why Component-Based Design?
The BCC screen is roughly divided into 3 zones.
- **Stream Layer Panel**: Video and overlay SVG animations
- **Control Command Panel**: Operating actions for registering and deleting people
- **Global Log Panel**: Terminal text displaying system messages

Angular excels at breaking these pieces down into individual parts (`*.component.ts`) and assembling them. Even if a specific component crashes, other elements render normally.

## 2. Sci-Fi HUD Design Resources: Pure SCSS Implementation
We abandoned general-purpose utility CSS like Tailwind and chose controllable **Custom SCSS** based code.
All cyber display effects rely on the techniques below.

- **Neon Glow**: Stacking and blurring `box-shadow` and `text-shadow` to create an illuminating LED feel.
- **Color Palette**: Using HSL basis instead of RGB basis (energetic cyan blue `#00f3ff`, powerful yellow `#f9ca24`).
- **Typography**: Imported the Google web font `Noto Sans KR` for perfect immersion without incongruity, and `Black Han Sans` for bold and overwhelming readability into CSS, replacing all system fonts.

## 3. RxJS-based Asynchronous Streaming
Up to dozens of events pop out from the SSE network every second. Angular utilizes its built-in `RxJS` to intercept (Subscribing) these events fluidly, filtering out excessive duplicates or employing lazy rendering to defend against screen jank (stuttering).
