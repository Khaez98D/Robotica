; Auto-generated. Do not edit!


(cl:in-package proyecto-srv)


;//! \htmlinclude points-request.msg.html

(cl:defclass <points-request> (roslisp-msg-protocol:ros-message)
  ((param
    :reader param
    :initarg :param
    :type cl:string
    :initform ""))
)

(cl:defclass points-request (<points-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <points-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'points-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name proyecto-srv:<points-request> is deprecated: use proyecto-srv:points-request instead.")))

(cl:ensure-generic-function 'param-val :lambda-list '(m))
(cl:defmethod param-val ((m <points-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader proyecto-srv:param-val is deprecated.  Use proyecto-srv:param instead.")
  (param m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <points-request>) ostream)
  "Serializes a message object of type '<points-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'param))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'param))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <points-request>) istream)
  "Deserializes a message object of type '<points-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'param) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'param) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<points-request>)))
  "Returns string type for a service object of type '<points-request>"
  "proyecto/pointsRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'points-request)))
  "Returns string type for a service object of type 'points-request"
  "proyecto/pointsRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<points-request>)))
  "Returns md5sum for a message object of type '<points-request>"
  "177fc52e6c64d96dce1a98062c347269")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'points-request)))
  "Returns md5sum for a message object of type 'points-request"
  "177fc52e6c64d96dce1a98062c347269")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<points-request>)))
  "Returns full string definition for message of type '<points-request>"
  (cl:format cl:nil "string param~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'points-request)))
  "Returns full string definition for message of type 'points-request"
  (cl:format cl:nil "string param~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <points-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'param))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <points-request>))
  "Converts a ROS message object to a list"
  (cl:list 'points-request
    (cl:cons ':param (param msg))
))
;//! \htmlinclude points-response.msg.html

(cl:defclass <points-response> (roslisp-msg-protocol:ros-message)
  ((coords
    :reader coords
    :initarg :coords
    :type cl:string
    :initform ""))
)

(cl:defclass points-response (<points-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <points-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'points-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name proyecto-srv:<points-response> is deprecated: use proyecto-srv:points-response instead.")))

(cl:ensure-generic-function 'coords-val :lambda-list '(m))
(cl:defmethod coords-val ((m <points-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader proyecto-srv:coords-val is deprecated.  Use proyecto-srv:coords instead.")
  (coords m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <points-response>) ostream)
  "Serializes a message object of type '<points-response>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'coords))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'coords))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <points-response>) istream)
  "Deserializes a message object of type '<points-response>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'coords) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'coords) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<points-response>)))
  "Returns string type for a service object of type '<points-response>"
  "proyecto/pointsResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'points-response)))
  "Returns string type for a service object of type 'points-response"
  "proyecto/pointsResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<points-response>)))
  "Returns md5sum for a message object of type '<points-response>"
  "177fc52e6c64d96dce1a98062c347269")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'points-response)))
  "Returns md5sum for a message object of type 'points-response"
  "177fc52e6c64d96dce1a98062c347269")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<points-response>)))
  "Returns full string definition for message of type '<points-response>"
  (cl:format cl:nil "string coords~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'points-response)))
  "Returns full string definition for message of type 'points-response"
  (cl:format cl:nil "string coords~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <points-response>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'coords))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <points-response>))
  "Converts a ROS message object to a list"
  (cl:list 'points-response
    (cl:cons ':coords (coords msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'points)))
  'points-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'points)))
  'points-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'points)))
  "Returns string type for a service object of type '<points>"
  "proyecto/points")