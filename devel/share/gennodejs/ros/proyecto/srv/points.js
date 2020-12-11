// Auto-generated. Do not edit!

// (in-package proyecto.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class pointsRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.param = null;
    }
    else {
      if (initObj.hasOwnProperty('param')) {
        this.param = initObj.param
      }
      else {
        this.param = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type pointsRequest
    // Serialize message field [param]
    bufferOffset = _serializer.string(obj.param, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type pointsRequest
    let len;
    let data = new pointsRequest(null);
    // Deserialize message field [param]
    data.param = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.param.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'proyecto/pointsRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'eb04b7504512676dca105ab8842899a4';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string param
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new pointsRequest(null);
    if (msg.param !== undefined) {
      resolved.param = msg.param;
    }
    else {
      resolved.param = ''
    }

    return resolved;
    }
};

class pointsResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.coords = null;
    }
    else {
      if (initObj.hasOwnProperty('coords')) {
        this.coords = initObj.coords
      }
      else {
        this.coords = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type pointsResponse
    // Serialize message field [coords]
    bufferOffset = _serializer.string(obj.coords, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type pointsResponse
    let len;
    let data = new pointsResponse(null);
    // Deserialize message field [coords]
    data.coords = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.coords.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'proyecto/pointsResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '193060e1db15ff0c954723b48c3a941b';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string coords
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new pointsResponse(null);
    if (msg.coords !== undefined) {
      resolved.coords = msg.coords;
    }
    else {
      resolved.coords = ''
    }

    return resolved;
    }
};

module.exports = {
  Request: pointsRequest,
  Response: pointsResponse,
  md5sum() { return '177fc52e6c64d96dce1a98062c347269'; },
  datatype() { return 'proyecto/points'; }
};
