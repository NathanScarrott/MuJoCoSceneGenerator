from openrouter_connector import call_llm, call_vision_llm
import subprocess
import os

def main():
    print("MuJoCo Scene Generator")
    print("Choose input method:")
    print("1. Text description")
    print("2. Image of room")
    
    choice = input("Enter choice (1 or 2): ").strip()
    
    if choice == "1":
        request = input("Describe the space you want to generate: ")
        use_vision = False
        image_path = None
    elif choice == "2":
        image_path = input("Enter path to room image: ").strip()
        if not os.path.exists(image_path):
            print(f"Image file not found: {image_path}")
            return
        request = input("Any additional description (optional): ") or "Generate a MuJoCo scene based on this room image"
        use_vision = True
    else:
        print("Invalid choice")
        return
    
    with open("../config/Prompt.txt", "r") as f:
        prompt_template = f.read()

    prompt = prompt_template.format(request=request)
    
    if use_vision:
        vision_instructions = """
VISION ANALYSIS INSTRUCTIONS:
This image may show a process flow diagram, factory layout, room, or other space. Analyze it carefully:
- If it's a process diagram: Translate the workflow into a physical factory layout
- If it's a room/space: Recreate the layout, furniture, and objects you see
- Pay attention to text labels, arrows, symbols, and spatial relationships
- Look for sequential process steps, production lines, or equipment stations
- Consider both the logical flow and physical arrangement

**CRITIQUE YOUR WORK TO ENSURE ALL COMPONENTS HAVE BEEN INCLUDED ACCURATELY**
"""
        
        final_prompt = vision_instructions + "\n\n" + prompt
        scene = call_vision_llm("anthropic/claude-sonnet-4", final_prompt, image_path)
    else:
        scene = call_llm("anthropic/claude-sonnet-4", prompt)

    if scene:
        # Save to examples directory
        output_file = "../examples/generated_scene.xml"
        with open(output_file, "w") as f:
            f.write(scene)
        print(f"✅ Scene saved to {output_file}")
        
        print("🚀 Launching simulation...")
        try:
            subprocess.run(["mjpython", "mujo_runner.py", output_file], check=True)
        except subprocess.CalledProcessError:
            print("Failed to launch with mjpython, trying python...")
            subprocess.run(["python", "mujo_runner.py", output_file])
        except FileNotFoundError:
            print("mjpython not found. Please run manually: mjpython src/mujo_runner.py")
    else:
        print("Failed to generate scene")

# Removed update_mujo_file() function - no longer needed
# mujo_runner.py now handles XML file loading directly

if __name__ == "__main__":
    main()