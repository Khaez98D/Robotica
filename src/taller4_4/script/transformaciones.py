#!/usr/bin/env python

from tf.transformations import euler_from_quaternion


def quad2euler(quaternion):
    return euler_from_quaternion(quaternion)