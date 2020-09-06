;; Auto-generated. Do not edit!


(when (boundp 'turtle_bot_4::turtle_bot_player)
  (if (not (find-package "TURTLE_BOT_4"))
    (make-package "TURTLE_BOT_4"))
  (shadow 'turtle_bot_player (find-package "TURTLE_BOT_4")))
(unless (find-package "TURTLE_BOT_4::TURTLE_BOT_PLAYER")
  (make-package "TURTLE_BOT_4::TURTLE_BOT_PLAYER"))
(unless (find-package "TURTLE_BOT_4::TURTLE_BOT_PLAYERREQUEST")
  (make-package "TURTLE_BOT_4::TURTLE_BOT_PLAYERREQUEST"))
(unless (find-package "TURTLE_BOT_4::TURTLE_BOT_PLAYERRESPONSE")
  (make-package "TURTLE_BOT_4::TURTLE_BOT_PLAYERRESPONSE"))

(in-package "ROS")





(defclass turtle_bot_4::turtle_bot_playerRequest
  :super ros::object
  :slots (_nombre ))

(defmethod turtle_bot_4::turtle_bot_playerRequest
  (:init
   (&key
    ((:nombre __nombre) "")
    )
   (send-super :init)
   (setq _nombre (string __nombre))
   self)
  (:nombre
   (&optional __nombre)
   (if __nombre (setq _nombre __nombre)) _nombre)
  (:serialization-length
   ()
   (+
    ;; string _nombre
    4 (length _nombre)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _nombre
       (write-long (length _nombre) s) (princ _nombre s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _nombre
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _nombre (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass turtle_bot_4::turtle_bot_playerResponse
  :super ros::object
  :slots (_ruta ))

(defmethod turtle_bot_4::turtle_bot_playerResponse
  (:init
   (&key
    ((:ruta __ruta) "")
    )
   (send-super :init)
   (setq _ruta (string __ruta))
   self)
  (:ruta
   (&optional __ruta)
   (if __ruta (setq _ruta __ruta)) _ruta)
  (:serialization-length
   ()
   (+
    ;; string _ruta
    4 (length _ruta)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _ruta
       (write-long (length _ruta) s) (princ _ruta s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _ruta
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _ruta (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass turtle_bot_4::turtle_bot_player
  :super ros::object
  :slots ())

(setf (get turtle_bot_4::turtle_bot_player :md5sum-) "de8e7c90c40bd1c3b6a3104b4ac68f54")
(setf (get turtle_bot_4::turtle_bot_player :datatype-) "turtle_bot_4/turtle_bot_player")
(setf (get turtle_bot_4::turtle_bot_player :request) turtle_bot_4::turtle_bot_playerRequest)
(setf (get turtle_bot_4::turtle_bot_player :response) turtle_bot_4::turtle_bot_playerResponse)

(defmethod turtle_bot_4::turtle_bot_playerRequest
  (:response () (instance turtle_bot_4::turtle_bot_playerResponse :init)))

(setf (get turtle_bot_4::turtle_bot_playerRequest :md5sum-) "de8e7c90c40bd1c3b6a3104b4ac68f54")
(setf (get turtle_bot_4::turtle_bot_playerRequest :datatype-) "turtle_bot_4/turtle_bot_playerRequest")
(setf (get turtle_bot_4::turtle_bot_playerRequest :definition-)
      "string nombre
---
string ruta
")

(setf (get turtle_bot_4::turtle_bot_playerResponse :md5sum-) "de8e7c90c40bd1c3b6a3104b4ac68f54")
(setf (get turtle_bot_4::turtle_bot_playerResponse :datatype-) "turtle_bot_4/turtle_bot_playerResponse")
(setf (get turtle_bot_4::turtle_bot_playerResponse :definition-)
      "string nombre
---
string ruta
")



(provide :turtle_bot_4/turtle_bot_player "de8e7c90c40bd1c3b6a3104b4ac68f54")


