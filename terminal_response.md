Here is the terminal response from VS Code. 

(lerobot) E:\Mechatronics\Modern-Robot-Learning-1\lerobot>lerobot-teleoperate --robot.type=so101_follower --robot.port=COM5 --robot.id=Ajiket_awesome_follower_arm --teleop.type=so101_leader --teleop.port=COM4 --teleop.id=Ajiket_awesome_leader_arm
INFO 2026-01-22 11:19:44 eoperate.py:201 {'display_compressed_images': False,
 'display_data': False,
 'display_ip': None,
 'display_port': None,
 'fps': 60,
 'robot': {'calibration_dir': None,
           'cameras': {},
           'disable_torque_on_disconnect': True,
           'id': 'Ajiket_awesome_follower_arm',
           'max_relative_target': None,
           'port': 'COM5',
           'use_degrees': False},
 'teleop': {'calibration_dir': None,
            'id': 'Ajiket_awesome_leader_arm',
            'port': 'COM4',
            'use_degrees': False},
 'teleop_time_s': None}
INFO 2026-01-22 11:19:44 so_leader.py:79 Ajiket_awesome_leader_arm SOLeader connected.
INFO 2026-01-22 11:19:45 _follower.py:97 Mismatch between calibration values in the motor and the calibration file or no calibration file found
INFO 2026-01-22 11:19:45 follower.py:123
Running calibration of Ajiket_awesome_follower_arm SOFollower   
Move Ajiket_awesome_follower_arm SOFollower to the middle of its range of motion and press ENTER....
Move all joints except 'wrist_roll' sequentially through their entire ranges of motion.
Recording positions. Press ENTER to stop...

-------------------------------------------
NAME            |    MIN |    POS |    MAX 
shoulder_pan    |    846 |   2098 |   3393 
shoulder_lift   |    834 |    837 |   3180 
elbow_flex      |    919 |   3126 |   3130 
wrist_flex      |    944 |   2967 |   3244 
gripper         |   2039 |   2044 |   3494 
Calibration saved to C:\Users\jiten\.cache\huggingface\lerobot\calibration\robots\so_follower\Ajiket_awesome_follower_arm.json  
INFO 2026-01-22 11:22:38 follower.py:106 Ajiket_awesome_follower_arm SOFollower connected.
Teleop loop time: 16.69ms (60 Hz)
