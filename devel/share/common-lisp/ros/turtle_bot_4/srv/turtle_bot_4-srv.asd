
(cl:in-package :asdf)

(defsystem "turtle_bot_4-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "turtle_bot_player" :depends-on ("_package_turtle_bot_player"))
    (:file "_package_turtle_bot_player" :depends-on ("_package"))
  ))