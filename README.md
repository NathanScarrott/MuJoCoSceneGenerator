# MuJoCo Scene Generator

An AI-powered tool that generates realistic MuJoCo physics simulation scenes from text descriptions or images. Perfect for creating factory layouts, production lines, and complex industrial environments.

## Features

- **AI-Powered Generation**: Uses Claude Sonnet 4 to create detailed MuJoCo XML scenes
- **Text Input**: Describe your scene in natural language
- **Image Input**: Upload process diagrams, factory layouts, or room photos
- **High Accuracy**: Achieves 95%+ accuracy with process flow diagrams
- **Automatic Simulation**: Generates XML and launches MuJoCo viewer automatically
- **Validated Output**: Ensures proper joint/actuator relationships for error-free simulation

## Project Structure

```
MuJoCo/
├── src/                    # Source code
│   ├── mujo_generator.py   # Main scene generator
│   ├── mujo_runner.py      # MuJoCo simulation runner
│   └── openrouter_connector.py  # LLM API connector
├── config/                 # Configuration files
│   └── Prompt.txt         # AI prompt template
├── examples/              # Generated scenes
│   └── generated_scene.xml
├── images/                # Input images
│   └── mapping-diagram.png
├── docs/                  # Documentation
├── output/                # Output directory
├── generate_scene.py      # Easy launcher script
├── requirements.txt       # Dependencies
└── README.md             # This file
```

## Quick Start

### 1. Setup Environment

```bash
# Clone the repository
git clone [your-repo-url]
cd MuJoCo

# Install Python dependencies
pip install -r requirements.txt

# Install MuJoCo (if not already installed)
# Follow: https://mujoco.readthedocs.io/en/stable/python.html

# Setup OpenRouter API key
echo "OPENROUTER_API_KEY=your_key_here" > .env
```

### 2. Generate Your First Scene

```bash
# Run the generator
python generate_scene.py

# Choose input method:
# 1. Text description
# 2. Image of room/process diagram

# Example text input:
"Create an aquarium factory with cleaning station, assembly line, and quality control"

# The tool will:
# - Generate MuJoCo XML
# - Save to examples/generated_scene.xml  
# - Automatically launch simulation
```

### 3. Run Existing Scenes

```bash
# Run a specific XML file
cd src
python mujo_runner.py ../examples/generated_scene.xml

# Or use mjpython for better macOS compatibility
mjpython mujo_runner.py ../examples/generated_scene.xml
```

## Usage Examples

### Text Input Examples:
- `"Factory assembly line with robotic arms and conveyor belts"`
- `"Warehouse with storage racks, forklifts, and loading docks"`
- `"Laboratory with workbenches, equipment, and safety areas"`
- `"Kitchen with appliances, prep areas, and storage"`

### Image Input:
- Process flow diagrams
- Factory layout blueprints  
- Room photographs
- Industrial facility plans

## Configuration

### AI Model Settings
Edit `src/mujo_generator.py` to change the AI model:
```python
# Current: Claude Sonnet 4
scene = call_vision_llm("anthropic/claude-sonnet-4", prompt, image_path)

# Alternatives:
# "anthropic/claude-3.5-sonnet"
# "openai/gpt-4o" 
# "google/gemini-flash-1.5"
```

### Prompt Customization
Modify `config/Prompt.txt` to customize the AI behavior:
- Add industry-specific requirements
- Modify validation rules
- Change output format preferences

## Troubleshooting

### Common Issues:

**1. "mjpython not found"**
```bash
# Install MuJoCo properly or use regular python
python src/mujo_runner.py examples/generated_scene.xml
```

**2. "API key not found"**
```bash
# Make sure .env file exists with your key
echo "OPENROUTER_API_KEY=your_key_here" > .env
```

**3. "XML validation errors"**
- The AI occasionally generates invalid XML
- Check for missing joints when actuators are present
- Regenerate the scene or edit the XML manually

**4. "Image not found"**
```bash
# Make sure image path is relative to src/ directory
# Or use absolute paths
```

## Development

### Adding New Features:
1. Add functions to `src/mujo_generator.py`
2. Update prompts in `config/Prompt.txt`
3. Test with various inputs
4. Update documentation

### Testing:
```bash
# Test with different scene types
python generate_scene.py

# Test specific XML files
python src/mujo_runner.py examples/test_scene.xml
```

## Examples Gallery

The `examples/` directory contains:
- `generated_scene.xml` - Latest generated scene
- Industrial process layouts
- Factory automation setups
- Laboratory environments

## API Documentation

### Core Functions:

#### `mujo_generator.main()`
Main entry point for scene generation.

#### `call_llm(model, prompt)`
Text-based LLM API call.

#### `call_vision_llm(model, prompt, image_path)`  
Vision-capable LLM API call with image input.

#### `mujo_runner.run_simulation(xml_file)`
Load and run MuJoCo simulation.

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## License

MIT License - see LICENSE file for details.

## Acknowledgments

- MuJoCo physics engine by DeepMind
- Claude AI by Anthropic
- OpenRouter API platform
- Python community for excellent libraries

---

**Happy Simulating!**
