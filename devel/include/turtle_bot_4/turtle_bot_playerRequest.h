// Generated by gencpp from file turtle_bot_4/turtle_bot_playerRequest.msg
// DO NOT EDIT!


#ifndef TURTLE_BOT_4_MESSAGE_TURTLE_BOT_PLAYERREQUEST_H
#define TURTLE_BOT_4_MESSAGE_TURTLE_BOT_PLAYERREQUEST_H


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
struct turtle_bot_playerRequest_
{
  typedef turtle_bot_playerRequest_<ContainerAllocator> Type;

  turtle_bot_playerRequest_()
    : nombre()  {
    }
  turtle_bot_playerRequest_(const ContainerAllocator& _alloc)
    : nombre(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _nombre_type;
  _nombre_type nombre;





  typedef boost::shared_ptr< ::turtle_bot_4::turtle_bot_playerRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::turtle_bot_4::turtle_bot_playerRequest_<ContainerAllocator> const> ConstPtr;

}; // struct turtle_bot_playerRequest_

typedef ::turtle_bot_4::turtle_bot_playerRequest_<std::allocator<void> > turtle_bot_playerRequest;

typedef boost::shared_ptr< ::turtle_bot_4::turtle_bot_playerRequest > turtle_bot_playerRequestPtr;
typedef boost::shared_ptr< ::turtle_bot_4::turtle_bot_playerRequest const> turtle_bot_playerRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::turtle_bot_4::turtle_bot_playerRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::turtle_bot_4::turtle_bot_playerRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::turtle_bot_4::turtle_bot_playerRequest_<ContainerAllocator1> & lhs, const ::turtle_bot_4::turtle_bot_playerRequest_<ContainerAllocator2> & rhs)
{
  return lhs.nombre == rhs.nombre;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::turtle_bot_4::turtle_bot_playerRequest_<ContainerAllocator1> & lhs, const ::turtle_bot_4::turtle_bot_playerRequest_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace turtle_bot_4

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::turtle_bot_4::turtle_bot_playerRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::turtle_bot_4::turtle_bot_playerRequest_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::turtle_bot_4::turtle_bot_playerRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::turtle_bot_4::turtle_bot_playerRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::turtle_bot_4::turtle_bot_playerRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::turtle_bot_4::turtle_bot_playerRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::turtle_bot_4::turtle_bot_playerRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "b2d4524d8435da3da9b759c1d24015c5";
  }

  static const char* value(const ::turtle_bot_4::turtle_bot_playerRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xb2d4524d8435da3dULL;
  static const uint64_t static_value2 = 0xa9b759c1d24015c5ULL;
};

template<class ContainerAllocator>
struct DataType< ::turtle_bot_4::turtle_bot_playerRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "turtle_bot_4/turtle_bot_playerRequest";
  }

  static const char* value(const ::turtle_bot_4::turtle_bot_playerRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::turtle_bot_4::turtle_bot_playerRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string nombre\n"
;
  }

  static const char* value(const ::turtle_bot_4::turtle_bot_playerRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::turtle_bot_4::turtle_bot_playerRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.nombre);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct turtle_bot_playerRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::turtle_bot_4::turtle_bot_playerRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::turtle_bot_4::turtle_bot_playerRequest_<ContainerAllocator>& v)
  {
    s << indent << "nombre: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.nombre);
  }
};

} // namespace message_operations
} // namespace ros

#endif // TURTLE_BOT_4_MESSAGE_TURTLE_BOT_PLAYERREQUEST_H