#!/usr/bin/env python3

# RMCS2303 MODBUS PARAMETERS
# --------------------------

"""
    BSD 3-Clause License

    Copyright (c) 2021, Rajesh Subramanian
    All rights reserved.

    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright notice, this
      list of conditions and the following disclaimer.

    * Redistributions in binary form must reproduce the above copyright notice,
      this list of conditions and the following disclaimer in the documentation
      and/or other materials provided with the distribution.

    * Neither the name of the copyright holder nor the names of its
      contributors may be used to endorse or promote products derived from
      this software without specific prior written permission.

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

# RHINO RMCS2303 PARAMETERS
LINES_PER_ROTATION_DEFAULT = 334
SPEED_DEFAULT = 5000
ACCELERATION_DEFAULT = 10000
ROTATION_360_ENCODER_COUNT = 69728.75  # uint32
GEAR_RATIO = 52.19
UPDATE_INTERVAL = 0.15  # 150ms
SPEED_MIN = 0  # RPM
SPEED_MAX = 65535  # RPM
ACCELERATION_MIN = 0  # RPM/sec
ACCELERATION_MAX = 65535  # RPM/sec

__SLAVE_ADDRESS = 7  # Default slave ID of RMCS2303 with all jumpers on

# ADDRESSES
__ADDRESS_MODE_SELECTION = 2  # Address for mode select
__ADDRESS_POSITION_PROPORTIONAL_GAIN = 4  # Address for Position Proportional Gain
__ADDRESS_POSITION_INTEGRAL_GAIN = 6
__ADDRESS_VELOCITY_FEED_FORWARD_GAIN = 8
__ADDRESS_LINES_PER_ROTATION = 10
__ADDRESS_ACCELERATION = 12
__ADDRESS_SPEED_RPM = 14
__ADDRESS_LSB_POSITION_COMMAND = 16
__ADDRESS_MSB_POSITION_COMMAND = 18
__ADDRESS_LSB_POSITION_FEEDBACK = 20
__ADDRESS_MSB_POSITION_FEEDBACK = 22
__ADDRESS_SPEED_FEEDBACK = 24

# COMMANDS
__COMMAND_ENABLE_MOTOR_CW = 257  # Enable motor in Clockwise Direction
__COMMAND_DISABLE_MOTOR_CW = 256  # Disable motor in Clockwise Direction
__COMMAND_BRAKE_CW = 260  # Brake in Clockwise Direction
__COMMAND_ENABLE_MOTOR_CCW = 265  # Enable motor in Counter Clockwise Direction
__COMMAND_DISABLE_MOTOR_CCW = 264  # Disable motor in Counter Clockwise Direction
__COMMAND_BRAKE_CCW = 268  # Brake in Counter Clockwise Direction
__COMMAND_HOME_POSITION = 2048  # Set current encoder count to 0
__COMMAND_EMERGENCY_STOP = 1792  # Stops motion and stops giving power to motor
__COMMAND_STOP = 1793  # Stops motion, motor maintains the position

# SCALING FACTOR
__SCALE_VALUE = 0  # number_of_decimals=2 will multiply value by 100 before sending it to the slave register

# FUNCTION CODES
__FUNCTION_WRITE_REGISTER = 6  # Function code to write to register
__FUNCTION_READ_REGISTER = 3  # Function code to read from register

# NUMBER OF REGISTERS
__ONE_REGISTER = 1
__TWO_REGISTERS = 2

# DATA INDEX
DATA_INDEX = 1

# PRE-DEFINED MESSAGE PACKETS
SPEED_MESSAGE = [__ADDRESS_SPEED_RPM, SPEED_DEFAULT, __SCALE_VALUE, __FUNCTION_WRITE_REGISTER]
ACCELERATION_MESSAGE = [__ADDRESS_ACCELERATION, ACCELERATION_DEFAULT, __SCALE_VALUE, __FUNCTION_WRITE_REGISTER]
LINES_PER_ROTATION_MESSAGE = [__ADDRESS_LINES_PER_ROTATION, LINES_PER_ROTATION_DEFAULT, __SCALE_VALUE, __FUNCTION_WRITE_REGISTER]
TURN_MOTOR_CW_MESSAGE = [__ADDRESS_MODE_SELECTION, __COMMAND_ENABLE_MOTOR_CW, __SCALE_VALUE, __FUNCTION_WRITE_REGISTER]
TURN_MOTOR_CCW_MESSAGE = [__ADDRESS_MODE_SELECTION, __COMMAND_ENABLE_MOTOR_CCW, __SCALE_VALUE, __FUNCTION_WRITE_REGISTER]
STOP_MOTOR_CW_MESSAGE = [__ADDRESS_MODE_SELECTION, __COMMAND_DISABLE_MOTOR_CW, __SCALE_VALUE, __FUNCTION_WRITE_REGISTER]
STOP_MOTOR_CCW_MESSAGE = [__ADDRESS_MODE_SELECTION, __COMMAND_DISABLE_MOTOR_CCW, __SCALE_VALUE, __FUNCTION_WRITE_REGISTER]
POSITION_FEEDBACK_MESSAGE = [__ADDRESS_LSB_POSITION_FEEDBACK, __TWO_REGISTERS, __FUNCTION_READ_REGISTER]
POSITION_FEEDBACK_LSB_MESSAGE = [__ADDRESS_LSB_POSITION_FEEDBACK, __ONE_REGISTER, __FUNCTION_READ_REGISTER]
POSITION_FEEDBACK_MSB_MESSAGE = [__ADDRESS_MSB_POSITION_FEEDBACK, __ONE_REGISTER, __FUNCTION_READ_REGISTER]
HOME_POSITION_MESSAGE = [__ADDRESS_MODE_SELECTION, __COMMAND_HOME_POSITION, __SCALE_VALUE, __FUNCTION_WRITE_REGISTER]
EMERGENCY_STOP_MESSAGE = [__ADDRESS_MODE_SELECTION, __COMMAND_EMERGENCY_STOP, __SCALE_VALUE, __FUNCTION_WRITE_REGISTER]
STOP_MESSAGE = [__ADDRESS_MODE_SELECTION, __COMMAND_STOP, __SCALE_VALUE, __FUNCTION_WRITE_REGISTER]
BRAKE_CW_MESSAGE = [__ADDRESS_MODE_SELECTION, __COMMAND_BRAKE_CW, __SCALE_VALUE, __FUNCTION_WRITE_REGISTER]
BRAKE_CCW_MESSAGE = [__ADDRESS_MODE_SELECTION, __COMMAND_BRAKE_CCW, __SCALE_VALUE, __FUNCTION_WRITE_REGISTER]
SPEED_FEEDBACK_MESSAGE = [__ADDRESS_SPEED_FEEDBACK, __ONE_REGISTER, __FUNCTION_READ_REGISTER]
