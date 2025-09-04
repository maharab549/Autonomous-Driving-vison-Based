#!/usr/bin/env python3

"""
Direct Fix: Make car turn left when YOLO detects danger class
"""

# This is the code to add directly to your main loop
# It should be added right after the YOLO detection section

DIRECT_FIX_CODE = """
            # DIRECT FIX: Check if danger class is detected and make immediate left turn
            if len(result_classid) != 0:
                cls_id, area, max_box, score = get_max_area(result_boxes, result_classid, result_scores)
                
                # Check if the detected class is "danger" (index 0)
                if int(cls_id) == 0 and area > 500 and score >= 0.6:
                    print("*" * 50)
                    print(f"DANGER DETECTED! Area: {area}, Score: {score}")
                    print("EXECUTING IMMEDIATE LEFT TURN!")
                    print("*" * 50)
                    
                    # Set direct left turn command
                    twist.angular.z = 2.0  # Strong left turn
                    twist.linear.x = 0.15  # Slow down during turn
                    
                    # Publish the command immediately
                    pub.publish(twist)
                    
                    # Continue turning left for a short duration
                    turn_start_time = time.time()
                    while time.time() - turn_start_time < 2.0:  # Turn for 2 seconds
                        # Keep publishing the turn command
                        pub.publish(twist)
                        time.sleep(0.1)  # Small delay
                        
                    # Gradually return to normal
                    twist.angular.z = 0.0
                    twist.linear.x = 0.2
                    pub.publish(twist)
                    
                    print("LEFT TURN COMPLETED")
"""

import sys
import re

def apply_direct_fix(file_path):
    """
    Apply a direct fix to make the car turn left when YOLO detects danger class.
    """
    # Read the file content
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Create a backup of the original file
    with open(file_path + '.direct_fix_backup', 'w') as backup:
        backup.write(content)
    
    # Find the YOLO detection section in the main loop
    yolo_section_pattern = r"(if yolo_flag:.*?result_boxes, result_scores, result_classid, use_time = yolov5_wrapper\.infer\(frame\))"
    
    # Check if the pattern exists
    if not re.search(yolo_section_pattern, content, re.DOTALL):
        print("Error: Could not find the YOLO detection section in the code.")
        print("Please apply the fix manually using the provided code.")
        return False
    
    # Apply the direct fix
    content = re.sub(yolo_section_pattern, r"\1\n" + DIRECT_FIX_CODE, content, flags=re.DOTALL)
    
    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.write(content)
    
    print(f"Applied direct fix to {file_path}")
    print(f"A backup of the original file was created at {file_path}.direct_fix_backup")
    return True

def create_manual_fix_file():
    """
    Create a file with the manual fix code.
    """
    with open("direct_fix_code.py", "w") as file:
        file.write("""# DIRECT FIX: Add this code right after the YOLO detection section
# Look for the line: result_boxes, result_scores, result_classid, use_time = yolov5_wrapper.infer(frame)
# Add this code immediately after that line:

# DIRECT FIX: Check if danger class is detected and make immediate left turn
if len(result_classid) != 0:
    cls_id, area, max_box, score = get_max_area(result_boxes, result_classid, result_scores)
    
    # Check if the detected class is "danger" (index 0)
    if int(cls_id) == 0 and area > 500 and score >= 0.6:
        print("*" * 50)
        print(f"DANGER DETECTED! Area: {area}, Score: {score}")
        print("EXECUTING IMMEDIATE LEFT TURN!")
        print("*" * 50)
        
        # Set direct left turn command
        twist.angular.z = 2.0  # Strong left turn
        twist.linear.x = 0.15  # Slow down during turn
        
        # Publish the command immediately
        pub.publish(twist)
        
        # Continue turning left for a short duration
        turn_start_time = time.time()
        while time.time() - turn_start_time < 2.0:  # Turn for 2 seconds
            # Keep publishing the turn command
            pub.publish(twist)
            time.sleep(0.1)  # Small delay
            
        # Gradually return to normal
        twist.angular.z = 0.0
        twist.linear.x = 0.2
        pub.publish(twist)
        
        print("LEFT TURN COMPLETED")
""")
    print("Created direct_fix_code.py with the manual fix code")

if __name__ == "__main__":
    # Create the manual fix file regardless
    create_manual_fix_file()
    
    if len(sys.argv) != 2:
        print("Usage: python direct_fix.py <path_to_file>")
        print("Example: python direct_fix.py /home/jetson/catkin_ws/ws/src/opencv_detection/scripts/new_main.py")
        sys.exit(1)
    
    file_path = sys.argv[1]
    apply_direct_fix(file_path)

