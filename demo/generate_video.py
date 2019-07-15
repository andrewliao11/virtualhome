# Generate video for a program. Make sure you have the executable open
import sys
sys.path.append('../simulation/')
from unity_simulator.comm_unity import UnityCommunication
script = ['[Walk] <sofa> (1)', '[Sit] <sofa> (1)'] # Add here your script
print('Starting Unity...')
comm = UnityCommunication()
print('Starting scene...')
comm.reset()
print('Generating video...')
success, message = comm.render_script(script, capture_screenshot=False)
if success:
    print('Generated, find video in simulation/unity_simulator/output/')
else:
    print('Cannot generate this video.', message)
