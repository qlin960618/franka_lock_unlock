cmake_minimum_required(VERSION 3.8)
project(franka_lock_unlock)


find_package(ament_cmake REQUIRED)


install(PROGRAMS
        franka_lock_unlock/run.py
        DESTINATION lib/${PROJECT_NAME})


##### LAUNCH FILES #####

install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME}/
)

##END## LAUNCH FILES #####

ament_package()