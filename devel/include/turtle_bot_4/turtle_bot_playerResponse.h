// Generated by gencpp from file turtle_bot_4/turtle_bot_playerResponse.msg
// DO NOT EDIT!


#ifndef TURTLE_BOT_4_MESSAGE_TURTLE_BOT_PLAYERRESPONSE_H
#define TURTLE_BOT_4_MESSAGE_TURTLE_BOT_PLAYERRESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace turtle_bot_4
{
template <class ContainerAllocator>
struct turtle_bot_playerResponse_
{
  typedef turtle_bot_playerResponse_<ContainerAllocator> Type;

  turtle_bot_playerResponse_()
    : ruta()  {
    }
  turtle_bot_playerResponse_(const ContainerAllocator& _alloc)
    : ruta(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _ruta_type;
  _ruta_type ruta;





  typedef boost::shared_ptr< ::turtle_bot_4::turtle_bot_playerResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::turtle_bot_4::turtle_bot_playerResponse_<ContainerAllocator> const> ConstPtr;

}; // struct turtle_bot_playerResponse_

typedef ::turtle_bot_4::turtle_bot_playerResponse_<std::allocator<void> > turtle_bot_playerResponse;

typedef boost::shared_ptr< ::turtle_bot_4::turtle_bot_playerResponse > turtle_bot_playerResponsePtr;
typedef boost::shared_ptr< ::turtle_bot_4::turtle_bot_playerResponse const> turtle_bot_playerResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::turtle_bot_4::turtle_bot_playerResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::turtle_bot_4::turtle_bot_playerResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::turtle_bot_4::turtle_bot_playerResponse_<ContainerAllocator1> & lhs, const ::turtle_bot_4::turtle_bot_playerResponse_<ContainerAllocator2> & rhs)
{
  return lhs.ruta == rhs.ruta;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::turtle_bot_4::turtle_bot_playerResponse_<ContainerAllocator1> & lhs, const ::turtle_bot_4::turtle_bot_playerResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace turtle_bot_4

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::turtle_bot_4::turtle_bot_playerResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::turtle_bot_4::turtle_bot_playerResponse_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::turtle_bot_4::turtle_bot_playerResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::turtle_bot_4::turtle_bot_playerResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::turtle_bot_4::turtle_bot_playerResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::turtle_bot_4::turtle_bot_playerResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::turtle_bot_4::turtle_bot_playerResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "e704ba92603507372fda36d5fd37cc34";
  }

  static const char* value(const ::turtle_bot_4::turtle_bot_playerResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xe704ba9260350737ULL;
  static const uint64_t static_value2 = 0x2fda36d5fd37cc34ULL;
};

template<class ContainerAllocator>
struct DataType< ::turtle_bot_4::turtle_bot_playerResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "turtle_bot_4/turtle_bot_playerResponse";
  }

  static const char* value(const ::turtle_bot_4::turtle_bot_playerResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::turtle_bot_4::turtle_bot_playerResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string ruta\n"
;
  }

  static const char* value(const ::turtle_bot_4::turtle_bot_playerResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::turtle_bot_4::turtle_bot_playerResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.ruta);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct turtle_bot_playerResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::turtle_bot_4::turtle_bot_playerResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::turtle_bot_4::turtle_bot_playerResponse_<ContainerAllocator>& v)
  {
    s << indent << "ruta: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.ruta);
  }
};

} // namespace message_operations
} // namespace ros

#endif // TURTLE_BOT_4_MESSAGE_TURTLE_BOT_PLAYERRESPONSE_H
