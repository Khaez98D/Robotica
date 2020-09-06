# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "turtle_bot_4: 0 messages, 1 services")

set(MSG_I_FLAGS "-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(turtle_bot_4_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/robotica/catkin_ws/src/turtle_bot_4/srv/turtle_bot_player.srv" NAME_WE)
add_custom_target(_turtle_bot_4_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "turtle_bot_4" "/home/robotica/catkin_ws/src/turtle_bot_4/srv/turtle_bot_player.srv" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages

### Generating Services
_generate_srv_cpp(turtle_bot_4
  "/home/robotica/catkin_ws/src/turtle_bot_4/srv/turtle_bot_player.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/turtle_bot_4
)

### Generating Module File
_generate_module_cpp(turtle_bot_4
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/turtle_bot_4
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(turtle_bot_4_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(turtle_bot_4_generate_messages turtle_bot_4_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/robotica/catkin_ws/src/turtle_bot_4/srv/turtle_bot_player.srv" NAME_WE)
add_dependencies(turtle_bot_4_generate_messages_cpp _turtle_bot_4_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(turtle_bot_4_gencpp)
add_dependencies(turtle_bot_4_gencpp turtle_bot_4_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS turtle_bot_4_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages

### Generating Services
_generate_srv_eus(turtle_bot_4
  "/home/robotica/catkin_ws/src/turtle_bot_4/srv/turtle_bot_player.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/turtle_bot_4
)

### Generating Module File
_generate_module_eus(turtle_bot_4
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/turtle_bot_4
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(turtle_bot_4_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(turtle_bot_4_generate_messages turtle_bot_4_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/robotica/catkin_ws/src/turtle_bot_4/srv/turtle_bot_player.srv" NAME_WE)
add_dependencies(turtle_bot_4_generate_messages_eus _turtle_bot_4_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(turtle_bot_4_geneus)
add_dependencies(turtle_bot_4_geneus turtle_bot_4_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS turtle_bot_4_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages

### Generating Services
_generate_srv_lisp(turtle_bot_4
  "/home/robotica/catkin_ws/src/turtle_bot_4/srv/turtle_bot_player.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/turtle_bot_4
)

### Generating Module File
_generate_module_lisp(turtle_bot_4
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/turtle_bot_4
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(turtle_bot_4_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(turtle_bot_4_generate_messages turtle_bot_4_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/robotica/catkin_ws/src/turtle_bot_4/srv/turtle_bot_player.srv" NAME_WE)
add_dependencies(turtle_bot_4_generate_messages_lisp _turtle_bot_4_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(turtle_bot_4_genlisp)
add_dependencies(turtle_bot_4_genlisp turtle_bot_4_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS turtle_bot_4_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages

### Generating Services
_generate_srv_nodejs(turtle_bot_4
  "/home/robotica/catkin_ws/src/turtle_bot_4/srv/turtle_bot_player.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/turtle_bot_4
)

### Generating Module File
_generate_module_nodejs(turtle_bot_4
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/turtle_bot_4
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(turtle_bot_4_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(turtle_bot_4_generate_messages turtle_bot_4_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/robotica/catkin_ws/src/turtle_bot_4/srv/turtle_bot_player.srv" NAME_WE)
add_dependencies(turtle_bot_4_generate_messages_nodejs _turtle_bot_4_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(turtle_bot_4_gennodejs)
add_dependencies(turtle_bot_4_gennodejs turtle_bot_4_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS turtle_bot_4_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages

### Generating Services
_generate_srv_py(turtle_bot_4
  "/home/robotica/catkin_ws/src/turtle_bot_4/srv/turtle_bot_player.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/turtle_bot_4
)

### Generating Module File
_generate_module_py(turtle_bot_4
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/turtle_bot_4
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(turtle_bot_4_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(turtle_bot_4_generate_messages turtle_bot_4_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/robotica/catkin_ws/src/turtle_bot_4/srv/turtle_bot_player.srv" NAME_WE)
add_dependencies(turtle_bot_4_generate_messages_py _turtle_bot_4_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(turtle_bot_4_genpy)
add_dependencies(turtle_bot_4_genpy turtle_bot_4_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS turtle_bot_4_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/turtle_bot_4)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/turtle_bot_4
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(turtle_bot_4_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/turtle_bot_4)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/turtle_bot_4
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(turtle_bot_4_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/turtle_bot_4)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/turtle_bot_4
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(turtle_bot_4_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/turtle_bot_4)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/turtle_bot_4
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(turtle_bot_4_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/turtle_bot_4)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/turtle_bot_4\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/turtle_bot_4
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(turtle_bot_4_generate_messages_py std_msgs_generate_messages_py)
endif()
