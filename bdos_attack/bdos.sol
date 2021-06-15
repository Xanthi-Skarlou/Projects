pragma solidity ^0.5.0;
contract Bdos {

    struct Info{
      string ip_address;
      string time;
      string command;
    }
    Info target;

    function set_target( string memory _ip_address, string memory _time, string memory _command) public {
        target.ip_address=_ip_address;
        target.time=_time;
        target.command=_command;
    }

    function get_target() public view returns ( string memory, string memory , string memory) {
        return(target.ip_address, target.time, target.command);
    }
}
