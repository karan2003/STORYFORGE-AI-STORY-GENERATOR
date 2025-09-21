

# STORYFORGE: AI Story Generator


![Example output generated with the default prompt.](https://user-images.githubusercontent.com/25360440/210071764-51ed5872-ba56-4ed0-919b-d9ce

**AI Story Generator STORYFORGE** democratizes digital storytelling, letting anyone craft and share immersive narratives from simple text prompts. Combining state-of-the-art language, vision, and speech models, STORYFORGE allows production of animated video stories without technical or artistic expertise. Designed for customizability, scale, and creativity, STORYFORGE redefines the boundaries of storytelling.[1]

***

## Table of Contents

- [Project Background](#project-background)
- [Key Features](#key-features)
- [System Architecture & Workflow](#system-architecture--workflow)
- [Requirements](#requirements)
- [Installation](#installation)
- [Quickstart](#quickstart)
- [Usage](#usage)
- [Command-Line Options](#command-line-options)
- [Implementation](#implementation)
- [Results](#results)
- [Conclusion](#conclusion)
- [Future Scope](#future-scope)
- [References](#references)
- [License](#license)

***

## Project Background

**STORYFORGE AI Story Generator** addresses the challenge of end-to-end, accessible digital storytelling by automating the creation of narrative, illustration, and audio narration using AI. Traditional barriers like artistic or technical expertise are removed; the platform democratizes creative expression in education, entertainment, research, and more.

***

## Key Features

- **Automated Story Generation:** GPT-based LLM composes creative narratives.
- **Dynamic Visual Illustration:** Stable Diffusion generates detailed images per scene.
- **AI-Powered Narration:** Neural TTS produces lifelike, synchronized voiceover.
- **Fully Animated Video Output:** Seamlessly assembles audio, images, and text.
- **Customizable Parameters:** Set mood, style, speed, and more via rich CLI options.
- **Real-Time Feedback:** Get suggestions for enhancing engagement.
- **Collaborative Storytelling:** Planned support for multi-user input and editing.
- **Accessibility:** Simple, CLI-driven operation—no special skills needed.[1]

***

## System Architecture & Workflow

```
[User Prompt]
      │
      ▼
[Narrative Generator: GPT Model]
      │
      ▼
[Visual Synthesizer: Stable Diffusion]
      │
      ▼
[Audio Synthesizer: Neural TTS]
      │
      ▼
[Assembly: Video Editor & Subtitle Generator]
      │
      ▼
[Final Video Output: Images + Audio + Subtitles]
```

***

## Requirements

### Hardware

- **Processor:** Quad-core (Intel i5 or equivalent), 8GB+ RAM, SSD, dedicated GPU recommended (NVIDIA GTX 1050+ or AMD equivalent)
- **Display/Peripherals:** FHD display, stable internet

### Software

- **OS:** Windows 10+, macOS High Sierra+, Linux
- **Python:** 3.7+ (3.8+ recommended)
- **Core Libraries:** PyTorch, Hugging Face Transformers, Stable Diffusion, Neural TTS, NumPy, SciPy, Pandas, OpenCV, Pillow, FFmpeg, Git, Jupyter Notebook

***

## Installation

**PyPI (recommended for most users):**
```
pip install storyteller-core
```

**From Source:**
```
git clone https://github.com/jaketae/storyteller.git
cd storyteller
pip install .
```

**Apple Silicon users:**  
You must [install mecab](https://github.com/SamuraiT/mecab-python3) first:  
```
brew install mecab
```
Then proceed with the regular installation.

**For development:**
```
pip install -e .[dev]
pre-commit install
```

***

## Quickstart

Run a demo using the CLI:
```
storyteller
```
This uses the default prompt: `Once upon a time, unicorns roamed the Earth.`  
Customize your story:
```
storyteller --writer_prompt "The ravenous cat, driven by an insatiable craving for tuna, devised a daring plan to break into the local fish market's coveted tuna reserve."
```
The final video will be saved in `out/out.mp4` along with images, audio, and subtitles.

To see all available CLI options:
```
storyteller --help
```

***

## Usage

### Command Line Interface

**For CUDA (GPU):**
```
storyteller --writer_device cuda --painter_device cuda
```
**Split across multiple GPUs:**
```
storyteller --writer_device cuda:0 --painter_device cuda:1
```
**Use half-precision for faster generation:**
```
storyteller --writer_device cuda --painter_device cuda --writer_dtype float16 --painter_dtype float16
```

**Apple Silicon (MPS):**
```
storyteller --writer_device mps --painter_device mps
storyteller --enable_attention_slicing true
```

### Python API

```python
from storyteller import StoryTeller
story_teller = StoryTeller.from_default()
story_teller.generate(...)
```
Or configure with custom settings:
```python
from storyteller import StoryTeller, StoryTellerConfig
config = StoryTellerConfig(
    writer="gpt2-large",
    painter="CompVis/stable-diffusion-v1-4",
    max_new_tokens=100,
)
story_teller = StoryTeller(config)
story_teller.generate(...)
```

***

## Command-Line Options

| Option                    | Description                                        | Default                          |
|---------------------------|----------------------------------------------------|----------------------------------|
| -h, --help                | Show help message and exit                         |                                  |
| --writer_prompt           | Starting text prompt                               | "Once upon a time, unicorns..."  |
| --painter_prompt_prefix   | Prefix for image prompt                            | "Beautiful painting"             |
| --num_images              | Number of images to generate                       | 10                               |
| --output_dir              | Output directory                                   | "out"                            |
| --seed                    | Seed for reproducibility                           | 42                               |
| --max_new_tokens          | Max tokens for story                               | 50                               |
| --writer                  | Writer model name                                  | "gpt2"                           |
| --painter                 | Image model                                        | "stabilityai/stable-diffusion-2" |
| --speaker                 | TTS model                                          | "tts_models/en/ljspeech/glow-tts"|
| --writer_device           | Writer device (cpu/cuda)                           | "cpu"                            |
| --painter_device          | Painter device (cpu/cuda)                          | "cpu"                            |
| --writer_dtype            | Writer model dtype                                 | "float32"                        |
| --painter_dtype           | Painter model dtype                                | "float32"                        |
| --enable_attention_slicing| Enables attention slicing for diffusion            | False                            |

***

## Implementation

- Unified API via `storyteller-core`
- Modular configuration and scene assembly (text, image, audio pipelines)
- Automated merging via FFmpeg, OpenCV
- Supports comprehensive CLI customization and Python API for advanced workflows.[1]

***

## Results

- Scene-by-scene narrative, illustration, and narration
- Animated, fully-voiced video ready for sharing or further editing
- All intermediate media files accessible in output directory

***

## Conclusion

**AI Story Generator STORYFORGE** transforms accessible, collaborative, and dynamic storytelling using generative AI. It opens new possibilities for digital learning, entertainment, and creative arts for all users.[1]

***

## Future Scope

- Improved narrative coherence and context
- Expanded support for genres and use-cases
- Personalized generation, real-time feedback
- Collaboration features and web/mobile integration
- Quality metrics and intelligent editing tools[1]

***

## References

- AI Story Generator STORYFORGE official report (SSIT, 2023-24)
- OpenAI GPT, Stable Diffusion, Coqui TTS documentation
- Example projects: GRANNY-GPT2, Auto-Story-GPT, Image2Story

***

## License

Released under the [MIT License](LICENSE).

***

**Keywords:** Generative AI, Storytelling, GPT, Stable Diffusion, Neural TTS, NLP, Deep Learning, PyTorch, Transformers, FFmpeg, Multimedia Synthesis, Text-to-Image, Creative Computing, Collaboration, Accessibility, Education, Open Source.

***

