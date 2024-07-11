VIRTUAL ENVIRONMENT CREATION:
py -m venv myvenv        

VIRTUAL ENVIRONMENT INITIALIZATION:
./myvenv/scripts/activate

pip install storyteller-core

cd storyteller

INSTALLING DEPENDENCIES:
pip install .

storyteller --writer_prompt "Students are going to college in bike" --writer_device cpu --painter_device cuda:1  --painter_prompt_prefix "REAL" --num_images 5 --enable_attention_slicing true --speaker "tts_models/en/ljspeech/hifi-gan"

storyteller --writer_prompt "Once upon a time, in a forgotten forest, there lived a curious creature named Luna." --writer_device cpu --painter_device cuda  --painter_prompt_prefix "REAL" --num_images 5 --enable_attention_slicing true --writer_dtype float32 --painter_dtype float64  

options:
  -h, --help            show this help message and exit
  --writer_prompt WRITER_PROMPT
                        The prompt to be used for the writer model. This is the text with which your story will begin. Default:
                        'Once upon a time, unicorns roamed the Earth.'
  --painter_prompt_prefix PAINTER_PROMPT_PREFIX
                        The prefix to be used for the painter model's prompt. Default: 'Beautiful painting'
  --num_images NUM_IMAGES
                        The number of images to be generated. Those images will be composed in sequence into a video. Default:
                        10
  --output_dir OUTPUT_DIR
                        The directory to save the generated files to. Default: 'out'
  --seed SEED           The seed value to be used for randomization. Default: 42
  --max_new_tokens MAX_NEW_TOKENS
                        Maximum number of new tokens to generate in the writer model. Default: 50
  --writer WRITER       Text generation model to use. Default: 'gpt2'
  --painter PAINTER     Image generation model to use. Default: 'stabilityai/stable-diffusion-2'
  --speaker SPEAKER     Text-to-speech (TTS) generation model. Default: 'tts_models/en/ljspeech/glow-tts'
  --writer_device WRITER_DEVICE
                        Text generation device to use. Default: 'cpu'
  --painter_device PAINTER_DEVICE
                        Image generation device to use. Default: 'cpu'
  --writer_dtype WRITER_DTYPE
                        Text generation dtype to use. Default: 'float32'
  --painter_dtype PAINTER_DTYPE
                        Image generation dtype to use. Default: 'float32'
  --enable_attention_slicing ENABLE_ATTENTION_SLICING
                        Whether to enable attention slicing for diffusion. Default: 'False'