# ComfyUI-PromptGenerator

A ComfyUI custom node that generates high-quality prompts for AI image generation using OpenAI API.
<img width="764" alt="{4154F89B-2DA2-476C-B1F1-F5CF22D9D53E}" src="https://github.com/user-attachments/assets/03c002ef-1837-4357-a18d-f5d003d199d7" />


## Features

- Support for all OpenAI-compatible API services, not limited to specific models:
  - Official OpenAI API
  - Self-hosted open-source models (via LM Studio, text-generation-webui, etc.)
  - Third-party compatible APIs (Claude API, Anthropic API, etc.)
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
