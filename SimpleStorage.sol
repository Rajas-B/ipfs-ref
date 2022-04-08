// SPDX-License-Identifier: UNLICENSED
pragma solidity >=0.6.0 <0.9.0;

contract SimpleStorage{
    struct People{
        string name;
        uint256 favoriteNumber;
    }
    mapping (string => People) public nameToFav;
    function addPerson(string memory _name, People memory _person) public {
        nameToFav[_name] = _person;
    }
    function retrieveNumber(string memory _name) public view returns (People memory){
        return nameToFav[_name];
    }
}