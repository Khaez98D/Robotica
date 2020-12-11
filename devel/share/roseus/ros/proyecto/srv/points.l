;; Auto-generated. Do not edit!


(when (boundp 'proyecto::points)
  (if (not (find-package "PROYECTO"))
    (make-package "PROYECTO"))
  (shadow 'points (find-package "PROYECTO")))
(unless (find-package "PROYECTO::POINTS")
  (make-package "PROYECTO::POINTS"))
(unless (find-package "PROYECTO::POINTSREQUEST")
  (make-package "PROYECTO::POINTSREQUEST"))
(unless (find-package "PROYECTO::POINTSRESPONSE")
  (make-package "PROYECTO::POINTSRESPONSE"))

(in-package "ROS")





(defclass proyecto::pointsRequest
  :super ros::object
  :slots (_param ))

(defmethod proyecto::pointsRequest
  (:init
   (&key
    ((:param __param) "")
    )
   (send-super :init)
   (setq _param (string __param))
   self)
  (:param
   (&optional __param)
   (if __param (setq _param __param)) _param)
  (:serialization-length
   ()
   (+
    ;; string _param
    4 (length _param)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _param
       (write-long (length _param) s) (princ _param s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _param
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _param (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass proyecto::pointsResponse
  :super ros::object
  :slots (_coords ))

(defmethod proyecto::pointsResponse
  (:init
   (&key
    ((:coords __coords) "")
    )
   (send-super :init)
   (setq _coords (string __coords))
   self)
  (:coords
   (&optional __coords)
   (if __coords (setq _coords __coords)) _coords)
  (:serialization-length
   ()
   (+
    ;; string _coords
    4 (length _coords)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _coords
       (write-long (length _coords) s) (princ _coords s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _coords
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _coords (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass proyecto::points
  :super ros::object
  :slots ())

(setf (get proyecto::points :md5sum-) "177fc52e6c64d96dce1a98062c347269")
(setf (get proyecto::points :datatype-) "proyecto/points")
(setf (get proyecto::points :request) proyecto::pointsRequest)
(setf (get proyecto::points :response) proyecto::pointsResponse)

(defmethod proyecto::pointsRequest
  (:response () (instance proyecto::pointsResponse :init)))

(setf (get proyecto::pointsRequest :md5sum-) "177fc52e6c64d96dce1a98062c347269")
(setf (get proyecto::pointsRequest :datatype-) "proyecto/pointsRequest")
(setf (get proyecto::pointsRequest :definition-)
      "string param
---
string coords
")

(setf (get proyecto::pointsResponse :md5sum-) "177fc52e6c64d96dce1a98062c347269")
(setf (get proyecto::pointsResponse :datatype-) "proyecto/pointsResponse")
(setf (get proyecto::pointsResponse :definition-)
      "string param
---
string coords
")



(provide :proyecto/points "177fc52e6c64d96dce1a98062c347269")


