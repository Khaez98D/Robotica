; Auto-generated. Do not edit!


(cl:in-package turtle_bot_4-srv)


;//! \htmlinclude turtle_bot_player-request.msg.html

(cl:defclass <turtle_bot_player-request> (roslisp-msg-protocol:ros-message)
  ((nombre
    :reader nombre
    :initarg :nombre
    :type cl:string
    :initform ""))
)

(cl:defclass turtle_bot_player-request (<turtle_bot_player-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <turtle_bot_player-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'turtle_bot_player-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name turtle_bot_4-srv:<turtle_bot_player-request> is deprecated: use turtle_bot_4-srv:turtle_bot_player-request instead.")))

(cl:ensure-generic-function 'nombre-val :lambda-list '(m))
(cl:defmethod nombre-val ((m <turtle_bot_player-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader turtle_bot_4-srv:nombre-val is deprecated.  Use turtle_bot_4-srv:nombre instead.")
  (nombre m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <turtle_bot_player-request>) ostream)
  "Serializes a message object of type '<turtle_bot_player-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'nombre))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'nombre))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <turtle_bot_player-request>) istream)
  "Deserializes a message object of type '<turtle_bot_player-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'nombre) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'nombre) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<turtle_bot_player-request>)))
  "Returns string type for a service object of type '<turtle_bot_player-request>"
  "turtle_bot_4/turtle_bot_playerRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'turtle_bot_player-request)))
  "Returns string type for a service object of type 'turtle_bot_player-request"
  "turtle_bot_4/turtle_bot_playerRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<turtle_bot_player-request>)))
  "Returns md5sum for a message object of type '<turtle_bot_player-request>"
  "de8e7c90c40bd1c3b6a3104b4ac68f54")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'turtle_bot_player-request)))
  "Returns md5sum for a message object of type 'turtle_bot_player-request"
  "de8e7c90c40bd1c3b6a3104b4ac68f54")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<turtle_bot_player-request>)))
  "Returns full string definition for message of type '<turtle_bot_player-request>"
  (cl:format cl:nil "string nombre~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'turtle_bot_player-request)))
  "Returns full string definition for message of type 'turtle_bot_player-request"
  (cl:format cl:nil "string nombre~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <turtle_bot_player-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'nombre))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <turtle_bot_player-request>))
  "Converts a ROS message object to a list"
  (cl:list 'turtle_bot_player-request
    (cl:cons ':nombre (nombre msg))
))
;//! \htmlinclude turtle_bot_player-response.msg.html

(cl:defclass <turtle_bot_player-response> (roslisp-msg-protocol:ros-message)
  ((ruta
    :reader ruta
    :initarg :ruta
    :type cl:string
    :initform ""))
)

(cl:defclass turtle_bot_player-response (<turtle_bot_player-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <turtle_bot_player-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'turtle_bot_player-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name turtle_bot_4-srv:<turtle_bot_player-response> is deprecated: use turtle_bot_4-srv:turtle_bot_player-response instead.")))

(cl:ensure-generic-function 'ruta-val :lambda-list '(m))
(cl:defmethod ruta-val ((m <turtle_bot_player-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader turtle_bot_4-srv:ruta-val is deprecated.  Use turtle_bot_4-srv:ruta instead.")
  (ruta m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <turtle_bot_player-response>) ostream)
  "Serializes a message object of type '<turtle_bot_player-response>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'ruta))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'ruta))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <turtle_bot_player-response>) istream)
  "Deserializes a message object of type '<turtle_bot_player-response>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'ruta) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'ruta) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<turtle_bot_player-response>)))
  "Returns string type for a service object of type '<turtle_bot_player-response>"
  "turtle_bot_4/turtle_bot_playerResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'turtle_bot_player-response)))
  "Returns string type for a service object of type 'turtle_bot_player-response"
  "turtle_bot_4/turtle_bot_playerResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<turtle_bot_player-response>)))
  "Returns md5sum for a message object of type '<turtle_bot_player-response>"
  "de8e7c90c40bd1c3b6a3104b4ac68f54")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'turtle_bot_player-response)))
  "Returns md5sum for a message object of type 'turtle_bot_player-response"
  "de8e7c90c40bd1c3b6a3104b4ac68f54")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<turtle_bot_player-response>)))
  "Returns full string definition for message of type '<turtle_bot_player-response>"
  (cl:format cl:nil "string ruta~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'turtle_bot_player-response)))
  "Returns full string definition for message of type 'turtle_bot_player-response"
  (cl:format cl:nil "string ruta~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <turtle_bot_player-response>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'ruta))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <turtle_bot_player-response>))
  "Converts a ROS message object to a list"
  (cl:list 'turtle_bot_player-response
    (cl:cons ':ruta (ruta msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'turtle_bot_player)))
  'turtle_bot_player-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'turtle_bot_player)))
  'turtle_bot_player-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'turtle_bot_player)))
  "Returns string type for a service object of type '<turtle_bot_player>"
  "turtle_bot_4/turtle_bot_player")