# AI_STORY_GENERATOR
The AI Storyteller is an ambitious project that combines cutting-edge technologies to create captivating and immersive stories

***

**AI Story Generator** is a cutting-edge platform merging advanced Artificial Intelligence with the creative process of storytelling. The system empowers anyone to turn simple prompts into immersive video stories—combining natural language generation, visual synthesis, and neural TTS into a fully-animated, multimedia experience.

***

## Abstract

AI Story Generator democratizes the creation of digital narratives, allowing anyone to craft and share rich stories built from AI-generated text, images, and narration. With a GPT-based model for text, Stable Diffusion for visuals, and state-of-the-art neural TTS for audio, users can produce custom video stories without special technical or artistic expertise. Designed for scalability, usability, and creativity, the platform breaks traditional barriers to storytelling and ushers in a new, accessible era of digital narrative creation.[1]

***

## Table of Contents

- [Project Background](#project-background)
- [Key Features](#key-features)
- [System Architecture & Workflow](#system-architecture--workflow)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Command-Line Options](#command-line-options)
- [Implementation](#implementation)
- [Results](#results)
- [Conclusion](#conclusion)
- [Future Scope](#future-scope)
- [References](#references)

***

## Project Background

The AI Story Generator addresses the demand for multi-sensory digital storytelling by unifying text, image, and audio creation. Traditional storytelling is limited by the need for writers, illustrators, and voice actors; this project removes those barriers using AI, making dynamic digital storytelling accessible to all and opening new creative possibilities for education, entertainment, and content creation.[1]

***

## Key Features

- **Automated Story Generation:** Uses a GPT-based LLM to write creative stories from user prompts.
- **Dynamic Visual Illustration:** Stable Diffusion generates detailed images for each story scene.
- **AI-Powered Narration:** Neural TTS produces lifelike voiceovers, adding realism and emotion.
- **Fully Animated Video Output:** All media are assembled into a cohesive video with subtitles.
- **Customizable & User-Friendly:** Users control style, mood, pacing, and export options.
- **Accessibility:** No special skills required; stories are saved with images, audio, and subtitles for easy sharing.
- **Collaborative Options:** Supports multi-user collaborative storytelling (future enhancement).
- **Real-Time Feedback:** Provides suggestions and feedback to users for more engaging stories.[1]

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

1. **Input**: User provides a prompt.
2. **Story Generation**: GPT crafts the narrative, segmented per scene.
3. **Image Synthesis**: Stable Diffusion generates a context image for each scene.
4. **Narration**: Neural TTS generates spoken audio for each scene.
5. **Assembly**: Text, images, and audio merged into a video (with subtitles).
6. **Output**: Downloadable video, with intermediate images/audio files for editing or sharing.[1]

***

## Requirements

### Hardware

- **Processor**: Quad-core (Intel i5 or equivalent recommended)
- **RAM**: 8 GB or higher recommended
- **Storage**: SSD for fastest processing
- **Graphics**: Dedicated GPU (NVIDIA GTX 1050+ or AMD equivalent)
- **Others**: Full HD display, stable internet, basic peripherals

### Software

- **OS**: Windows 10+, macOS High Sierra+, or Linux (e.g., Ubuntu)
- **Python**: 3.7+ (3.8+ recommended)
- **Core Libraries**: PyTorch, Transformers, Stable Diffusion, Neural TTS, NumPy, SciPy, Pandas, OpenCV, Pillow, FFmpeg, Git, Jupyter Notebook, MySQL/PostgreSQL (optional)

***

## Installation

```bash
# Create and activate virtual environment
py -m venv myvenv
./myvenv/scripts/activate

# Install core package
pip install storyteller-core

# Navigate to directory
cd storyteller

# Install dependencies
pip install .
```

***

## Usage

The `storyteller` CLI offers comprehensive options.

### Example Command:

```bash
storyteller --writer_prompt "Once upon a time, unicorns roamed the Earth." \
  --writer_device cpu \
  --painter_device cuda:0 \
  --painter_prompt_prefix "Beautiful painting" \
  --num_images 5 \
  --enable_attention_slicing true \
  --speaker "tts_models/en/ljspeech/hifi-gan"
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

The codebase is organized for modularity and maintainability:

- **Initialization**: Provides a unified API via storyteller-core.
- **Config**: Uses dataclasses for configuration management and validation.
- **Text/Image/Audio Generation**: Efficient pipeline using PyTorch and model-specific optimizations.
- **Assembly**: Automated use of FFmpeg and OpenCV to merge results.
- **Customization**: Supports CLI arguments for maximum flexibility.[1]

***

## Results

- Stories are generated scene-by-scene, each with unique illustration and narration.
- Final output is a cohesive, fully-animated video.
- All intermediate assets (audio, image, subtitles) saved for review or editing.

***

## Conclusion

The AI Story Generator proves the viability and creative power of merging AI with storytelling. This project has demonstrated the effective synthesis of text, visuals, and narration—offering users a seamless way to produce engaging multimedia stories and opening pathways to new creative applications in education, writing, and entertainment.[1]

***

## Future Scope

- **Coherence & Context**: Improving narrative consistency and context awareness.
- **Domain Expansion**: Support for more genres, styles, educational and professional use.
- **Personalization**: Interactive, user-driven parameters and real-time feedback.
- **Collaboration**: Multi-user collaboration tools.
- **Evaluation**: Development of story quality metrics and feedback systems.
- **Deployment**: Extensions for web, mobile, education, and integration with other platforms.[1]

***

## References

- AI Story Generator official report (SSIT, 2023-24).[1]
- OpenAI GPT, Stable Diffusion, Coqui TTS documentation.
- Community benchmarks and sample projects: GRANNY-GPT2, Auto-Story-GPT, Image2Story.

***

**Keywords:** Generative AI, Storytelling, GPT, Stable Diffusion, Neural TTS, NLP, Deep Learning, PyTorch, Transformers, FFmpeg, Multimedia Synthesis, Text-to-Image, Creative Computing, Collaboration, Accessibility, Education, Open Source.

***

This version offers context, usability information, and technical detail for users, contributors, and educators alike.[1]

[1](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/90391685/8ed6507d-f26d-4163-a8f3-ccad088b19db/AI-STORY-GENERATOR-REPORT-Final-1.pdf)
