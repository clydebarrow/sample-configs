import os
import yaml
from pathlib import Path
import argparse
import sys

def print_yaml_file(file_path):
    """Print the contents of a YAML file in a readable format"""
    try:
        with open(file_path, 'r') as f:
            config = yaml.unsafe_load(f)
            
        print(f"\n=== {file_path.name} ===")
        print("\nBoard Configuration:")
        if 'esp32' in config:
            print(f"Board: {config['esp32'].get('board', 'Not specified')}")
            print(f"Chip Type: ESP32")
        elif 'esp8266' in config:
            print(f"Board: {config['esp8266'].get('board', 'Not specified')}")
            print(f"Chip Type: ESP8266")
        elif 'rp2040' in config:
            print(f"Board: {config['rp2040'].get('board', 'Not specified')}")
            print(f"Chip Type: RP2040")
        else:
            print("No board configuration found")
            
        print("\nDisplay Configuration:")
        if 'display' in config:
            for display in config['display']:
                print(f"Platform: {display.get('platform', 'Not specified')}")
                print(f"Model: {display.get('model', 'Not specified')}")
        else:
            print("No display configuration found")
            
    except Exception as e:
        print(f"Error reading {file_path.name}: {str(e)}")

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Read and display YAML configuration files')
    parser.add_argument('--platform', type=str, help='Filter by display platform (e.g., "ssd1306", "st7789")')
    args = parser.parse_args()

    # Get the directory containing the YAML files
    script_dir = Path(__file__).parent
    yaml_files = list(script_dir.glob('*.yaml'))
    
    # Process each YAML file
    for yaml_file in yaml_files:
        with open(yaml_file, 'r') as f:
            config = yaml.safe_load(f)
        
        # Skip files that don't match the specified platform
        if args.platform:
            if 'display' not in config:
                continue
            display_platforms = [d.get('platform', '').lower() for d in config['display']]
            if args.platform.lower() not in display_platforms:
                continue
                
        print_yaml_file(yaml_file)

if __name__ == "__main__":
    main()
