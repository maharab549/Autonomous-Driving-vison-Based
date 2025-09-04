# DIRECT FIX: Add this code right after the YOLO detection section
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
