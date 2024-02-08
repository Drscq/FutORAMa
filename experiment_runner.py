import subprocess
import re

def update_config_file(ball_data_size):
    config_path = 'real_oram/config.py'
    
    # Initialize a variable to track whether the first occurrence has been updated
    updated = False
    
    # Read the current content of the file
    with open(config_path, 'r') as file:
        lines = file.readlines()
    
    # Process each line to find the first occurrence of BALL_DATA_SIZE
    for i, line in enumerate(lines):
        if 'BALL_DATA_SIZE' in line and not updated:
            # Replace the value after '=' with the new ball_data_size
            # This assumes the line format "BALL_DATA_SIZE = <value>"
            parts = line.split('=')
            if len(parts) == 2:  # Ensures there is an '=' to split on
                lines[i] = f'{parts[0]}= {ball_data_size}\n'
                updated = True  # Mark as updated to avoid changing any further occurrences
                break  # No need to continue once the first occurrence is updated
    
    # Write the updated content back to the file, if a change was made
    if updated:
        with open(config_path, 'w') as file:
            file.writelines(lines)



def run_experiment(number_of_blocks, block_size=None):
    if block_size is not None:
        update_config_file(block_size)
    
    command = f'python main.py 1 {number_of_blocks}'
    subprocess.run(command, shell=True)

def main():
    # Testing the effect of the number of blocks
    for exponent in range(18, 31): # 2^18 to 2^30
        number_of_blocks = 2 ** exponent
        print(f'Running experiment with {number_of_blocks} blocks.')
        run_experiment(number_of_blocks)
    
    # Testing the effect of block size
    number_of_blocks = 2 ** 18 # Fixed number of blocks
    for exponent in range(12, 23): # 2^12 to 2^22
        block_size = 2 ** exponent
        print(f'Running experiment with block size {block_size} bytes.')
        run_experiment(number_of_blocks, block_size)

if __name__ == '__main__':
    main()
