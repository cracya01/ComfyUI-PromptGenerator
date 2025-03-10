# ComfyUI-PromptGenerator

A ComfyUI custom node that generates high-quality prompts for AI image generation using OpenAI API.

## Features

- Generate creative and detailed prompts using OpenAI API (GPT-3.5, GPT-4)
- Customize system prompts and user inputs
- Filter generated text using regular expressions
- Configure API parameters (temperature, max tokens, etc.)
- Seamless integration with ComfyUI workflow

## Installation

1. Make sure you have ComfyUI installed
2. Clone this repository to your ComfyUI's custom_nodes directory:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/cracya01/ComfyUI-PromptGenerator.git
3. Install dependencies:
```bash
cd ComfyUI-PromptGenerator
pip install -r requirements.txt
 ```

4. Restart ComfyUI
## Usage
1. Add the "cracya OpenAI API Config" node and set your API key
2. Add the "cracya Prompt Generator" node and connect it to the API config node
3. Set your system prompt and user prompt
4. Optional: Use the "cracya Regex Filter" node to clean up the generated text
5. Connect the generated prompt to other ComfyUI nodes (like CLIP Text Encode)
## Node Descriptions
### cracya OpenAI API Config
Configure OpenAI API parameters, including API key, base URL, model name, temperature, and max tokens.

### cracya Prompt Generator
Generate prompts using OpenAI API. Requires connection to an API config node.

### cracya Regex Filter
Filter text using regular expressions. Useful for cleaning up generated prompts.

## Example Workflow
1. Configure API → Generate Prompt → Filter Prompt → Use in Text to Image
## License
MIT
