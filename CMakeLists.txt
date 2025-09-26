cmake_minimum_required(VERSION 3.16.3)
project(cuzk_tools)

find_package(catkin REQUIRED COMPONENTS
  geographic_msgs
  geometry_msgs
  jsk_recognition_msgs
  message_generation
  sensor_msgs
  std_msgs
  visualization_msgs
)

catkin_python_setup()

add_message_files(FILES
  LineString.msg
  LineStringArray.msg
  OrtoImage.msg
  PointArray.msg
  Polygons.msg
  Topography.msg
  TopographyCategory.msg
)

add_service_files(FILES
  ElevationGet.srv
  ElevationPublish.srv
  ElevationSetTF.srv
  GeoPointElevationGet.srv
  GetTopography.srv
  MarkerGet.srv
  PointElevationGet.srv
)

generate_messages(DEPENDENCIES
  geographic_msgs
  geometry_msgs
  jsk_recognition_msgs
  sensor_msgs
  std_msgs
  visualization_msgs
)

catkin_package(
  CATKIN_DEPENDS
    geographic_msgs
    geometry_msgs
    jsk_recognition_msgs
    message_runtime
    sensor_msgs
    std_msgs
    visualization_msgs 
)

catkin_install_python(PROGRAMS
  nodes/elevation
  nodes/gpkg_parser
  nodes/marker_pub
  nodes/orto2mesh
  nodes/pcd2mesh
  nodes/pose_elevation_srv
  nodes/pose_elevation_tf
  nodes/topography
  nodes/viz_map
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY
  config/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/config
)

install(DIRECTORY
  launch/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
)

install(DIRECTORY
  rviz/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/rviz
)

if (CATKIN_ENABLE_TESTING)
  find_package(roslint REQUIRED)
  find_package(roslaunch REQUIRED)

  roslint_custom(catkin_lint "-W2" .)

  # Run roslint on Python sources
  # file(GLOB_RECURSE python_files nodes/*.py src/${PROJECT_NAME}/*.py setup.py)
  # roslint_python("${python_files}")

  roslint_add_test()

  roslaunch_add_file_check(launch IGNORE_UNSET_ARGS)
endif()
