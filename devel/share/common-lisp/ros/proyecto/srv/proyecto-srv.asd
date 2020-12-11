
(cl:in-package :asdf)

(defsystem "proyecto-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "points" :depends-on ("_package_points"))
    (:file "_package_points" :depends-on ("_package"))
  ))