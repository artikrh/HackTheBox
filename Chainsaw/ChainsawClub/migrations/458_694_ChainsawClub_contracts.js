const ChainsawClub = artifacts.require("./ChainsawClub.sol");

    module.exports = function(deployer) {
      deployer.deploy(ChainsawClub);
    };