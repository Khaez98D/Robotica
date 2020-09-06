// Auto-generated. Do not edit!

// (in-package turtle_bot_4.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class turtle_bot_playerRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.nombre = null;
    }
    else {
      if (initObj.hasOwnProperty('nombre')) {
        this.nombre = initObj.nombre
      }
      else {
        this.nombre = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type turtle_bot_playerRequest
    // Serialize message field [nombre]
    bufferOffset = _serializer.string(obj.nombre, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type turtle_bot_playerRequest
    let len;
    let data = new turtle_bot_playerRequest(null);
    // Deserialize message field [nombre]
    data.nombre = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.nombre.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'turtle_bot_4/turtle_bot_playerRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'b2d4524d8435da3da9b759c1d24015c5';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string nombre
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new turtle_bot_playerRequest(null);
    if (msg.nombre !== undefined) {
      resolved.nombre = msg.nombre;
    }
    else {
      resolved.nombre = ''
    }

    return resolved;
    }
};

class turtle_bot_playerResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.ruta = null;
    }
    else {
      if (initObj.hasOwnProperty('ruta')) {
        this.ruta = initObj.ruta
      }
      else {
        this.ruta = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type turtle_bot_playerResponse
    // Serialize message field [ruta]
    bufferOffset = _serializer.string(obj.ruta, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type turtle_bot_playerResponse
    let len;
    let data = new turtle_bot_playerResponse(null);
    // Deserialize message field [ruta]
    data.ruta = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.ruta.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'turtle_bot_4/turtle_bot_playerResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'e704ba92603507372fda36d5fd37cc34';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string ruta
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new turtle_bot_playerResponse(null);
    if (msg.ruta !== undefined) {
      resolved.ruta = msg.ruta;
    }
    else {
      resolved.ruta = ''
    }

    return resolved;
    }
};

module.exports = {
  Request: turtle_bot_playerRequest,
  Response: turtle_bot_playerResponse,
  md5sum() { return 'de8e7c90c40bd1c3b6a3104b4ac68f54'; },
  datatype() { return 'turtle_bot_4/turtle_bot_player'; }
};
