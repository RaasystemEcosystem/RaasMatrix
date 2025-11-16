// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/// @title OptimizedRWA - minimal example for Phase 1
/// @notice Simplified RWA token storage with gas-conscious operations
contract OptimizedRWA {
    mapping(bytes32 => uint256) private balances;
    address public admin;

    event Mint(bytes32 indexed id, uint256 amount);
    event Burn(bytes32 indexed id, uint256 amount);

    modifier onlyAdmin() {
        require(msg.sender == admin, "only admin");
        _;
    }

    constructor(address _admin) {
        admin = _admin;
    }

    function mint(bytes32 id, uint256 amount) external onlyAdmin {
        unchecked {
            balances[id] += amount;
        }
        emit Mint(id, amount);
    }

    function burn(bytes32 id, uint256 amount) external onlyAdmin {
        require(balances[id] >= amount, "insufficient");
        unchecked {
            balances[id] -= amount;
        }
        emit Burn(id, amount);
    }

    function balanceOf(bytes32 id) external view returns (uint256) {
        return balances[id];
    }
}
