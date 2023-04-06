---
title: "Mobile Theft Prevention using Blockchain"
date: 2023-04-06T00:00:00+05:30
author: "Yathin Prakash Kethepalli"
---

# Mobile Theft Prevention using Blockchain

```{admonition} Key Insights
:class: tip
- Mobile theft is a major concern for smartphone users worldwide, with an estimated 70 million smartphones lost each year.
- Blockchain technology has the potential to provide a secure and decentralized solution to prevent mobile theft.
- The proposed model of using blockchain for mobile theft prevention offers several potential advantages over existing methods, including decentralized and tamper-proof tracking, automation of process, cross-border usage, and cost reduction.
- The smart contract enables the registration of new mobile devices and maps them to their respective phone numbers. It provides a secure and tamper-proof solution for tracking the status of mobile devices on the blockchain.
- The implementation of blockchain-based mobile theft prevention solutions provides an added layer of security that can greatly benefit mobile phone users, manufacturers, and society at large.
```

## Introduction
Mobile theft is a major concern for smartphone users worldwide. With the increasing reliance on mobile devices for personal and professional use, the theft or loss of a smartphone can result in a significant loss of data and privacy. Studies indicate that a staggering number of smartphones, estimated at 70 million, are lost each year, with a meager 7% recovered {cite}`hom2016mobile`. Further, company-issued smartphones are not immune to these occurrences, as research has shown that 4.3% of them are lost or stolen annually. Workplace and conference environments are the leading hotspots for smartphone theft, with 52% and 24% of devices stolen, respectively. Moreover, these numbers appear to be increasing, with recent studies indicating a rise of 39.2% between 2019 and 2021 {cite}`henriquez2022mobile`. Given these alarming statistics, there is a growing need for effective mobile theft prevention measures. Blockchain technology has the potential to provide a secure and decentralized solution to prevent mobile theft. By leveraging the immutable and distributed nature of blockchain, it is possible to create a tamper-proof system that can prevent unauthorized access to mobile devices. In this article, we will explore the potential of blockchain technology for mobile theft prevention, its advantages and limitations, and the future prospects of this emerging field.

The proposed technology of using blockchain for mobile theft prevention is still in the development stage and has not yet been widely adopted on a national or international level. However, there are several companies and organizations that are exploring the use of blockchain for mobile security and anti-theft solutions. Internationally, companies such as Samsung and Huawei are researching the use of blockchain for mobile security, with Samsung filing several patents for blockchain-based mobile security solutions {cite}`fortis2022samsung` {cite}`huawei2018whitepaper`.

There is currently no known widespread adoption of blockchain for mobile theft prevention. However, the governments all over the world has been exploring the use of blockchain for various applications, including supply chain management and digital identity. This indicates that there is an interest in the technology and a potential for the proposed model to be adopted globally.

## Rationale Behind Mobile Theft Prevention using Blockchain
Mobile theft has become a growing concern for individuals and organizations around the world. In addition to the financial loss associated with the theft, there is also a significant risk of personal data being compromised. The use of blockchain technology for mobile theft prevention offers a secure and efficient solution for preventing mobile theft {cite}`göbel2018blockchain`. This technology can help individuals and organizations protect their mobile devices and personal information by providing a decentralized and tamper-proof way to track and block stolen mobile devices. By using private blockchains, the proposed model can be implemented in a way that ensures security and privacy, while also reducing the risk of fraud or malicious activity.

- **Decentralized and tamper-proof**: Blockchain technology enables a decentralized and tamper-proof system for tracking and disabling stolen mobile devices. This ensures that the information stored on the blockchain is accurate and cannot be tampered with, making it a reliable source for tracking stolen devices {cite}`chirag2023blockchain`.
- **Secure and private**: The proposed model uses a private blockchain network that connects the mobile manufacturing companies and their nodes {cite}`iredale2021privateblockchain`. This helps to ensure the security of the network and the data stored in it, and also helps to maintain the privacy of the users.
- **Automation of process**: Smart contracts can be programmed to automatically disable the device once the signal is sent, reducing human error and increasing the efficiency {cite}`Das2021`.
- **Cross-border usage**: The proposed model can be used in cross-border cases, making it more efficient and effective than existing methods {cite}`ramakrishnan2021crossborder`.
- **Cost reduction**: By reducing the number of mobile thefts, the proposed model can also have a positive economic impact. This can include reducing the costs associated with mobile theft for consumers, mobile carriers, and insurance companies {cite}`Ali2020costreduction`.

## Alternative Technologies Available under Development
- **IMEI blocking:** One of the most common methods for preventing mobile theft is to block the IMEI (International Mobile Equipment Identity) number of a stolen device. This can be done by reporting the theft to the mobile carrier, who will then blacklist the IMEI number and prevent the device from connecting to the network {cite}`hicks2022imei`.
- **SIM card blocking:** Similar to IMEI blocking, SIM card blocking involves disabling the SIM card of a stolen device. This can be done by reporting the theft to the mobile carrier, who will then deactivate the SIM card and prevent the device from connecting to the network {cite}`ict2015simblocking`.
- **Remote wipe:** Some mobile devices include a remote wipe feature, which allows the device owner to remotely delete all of the data on their device if it is lost or stolen {cite}`asha2023remotewipe`.
- **Mobile tracking apps:** {cite}`marcus2023phonetracker`.

In comparison, the model of using blockchain for mobile theft prevention offers several potential advantages over these existing methods. A decentralized and tamper-proof system for tracking and disabling stolen devices, and the smart contract can be programmed to automatically disable the device once the signal is sent, reducing human error and increasing the efficiency. Additionally, the proposed model can potentially work in cross-border cases, which is not possible with IMEI and SIM card blocking, and also can be integrated with other theft prevention methods.

## Methodology
The smart contract enables the registration of new mobile devices and maps them to their respective phone numbers. This allows users to update the status of their mobile devices on the blockchain, indicating whether they are lost or stolen. The smart contract also allows for changes to be made to the registered mobile devices’ information, such as their International Mobile Equipment Identity (IMEI) number, and to update the corresponding phone number. In this way, the smart contract provides a secure and tamper-proof solution for tracking the status of mobile devices on the blockchain.

The mobile application is designed to constantly monitor the state of the mobile device by making API calls to the blockchain. If the blockchain indicates that the device has been reported stolen, the application takes action by disabling the device’s Wi-Fi and network connections and forcing it into airplane mode. By doing so, the application prevents the thief from using any of the phone’s features, rendering it useless until it can be recovered by the rightful owner.

When a mobile phone is marked as stolen on the blockchain through the smart contract and later found. The owner of the phone wishes to reactivate the phone, they can connect it to a computer via USB and use USB mode to provide data to the phone. This can allow the owner to activate the phone again by providing the data through the USB based hotspot.

The below code is a smart contract written in Solidity and JavaScript that can be deployed on a blockchain network. It is designed to prevent mobile theft by using a mapping function to keep track of mobile devices using their IMEI numbers and phone numbers.

### Smart Contract - Solidity
```solidity
// SPDX-License-Identifier: None
pragma solidity 0.8.7;

contract MobileTheftPrevention{
    mapping(bytes32=>bool) private isIMEIexist;
    mapping(bytes32=>bool) private isPhoneNumberexist;
    mapping(address=>mapping(bytes32=>bytes32)) private mapAPI;
    mapping(bytes32=>bool) private isIMEIlost;

    function hash(uint _value) private pure returns(bytes32){
        return keccak256(abi.encodePacked(_value));
    }

    function addIMEI(uint _IMEI, uint _phoneNumber) public{
        require(isIMEIexist[hash(_IMEI)] == false);
        require(isPhoneNumberexist[hash(_phoneNumber)] == false);
        isIMEIexist[hash(_IMEI)] = true;
        isPhoneNumberexist[hash(_phoneNumber)] = true;
        mapAPI[msg.sender][hash(_phoneNumber)] = hash(_IMEI);
    }

    function activateLost(uint _phoneNumber) public{
        require(isIMEIexist[mapAPI[msg.sender][hash(_phoneNumber)]] == true);
        isIMEIlost[mapAPI[msg.sender][hash(_phoneNumber)]] = true;
    }

    function deactivateLost(uint _phoneNumber) public{
        require(isIMEIexist[mapAPI[msg.sender][hash(_phoneNumber)]] == true);
        isIMEIlost[mapAPI[msg.sender][hash(_phoneNumber)]] = false;
    }

    function changeIMEI(uint _IMEI, uint _phoneNumber, uint _newIMEI) public{
        require(isIMEIexist[hash(_IMEI)] == true);
        require(isPhoneNumberexist[hash(_phoneNumber)] == true);
        require(mapAPI[msg.sender][hash(_phoneNumber)] == hash(_IMEI));
        mapAPI[msg.sender][hash(_phoneNumber)] = hash(_newIMEI);
        isIMEIexist[hash(_IMEI)] = false;
        if(isIMEIexist[hash(_newIMEI)] == false){
            isIMEIexist[hash(_IMEI)] = true;
        }
    }

    function changePhoneNumber(uint _IMEI, uint _phoneNumber, uint _newPhoneNumber) public{
        require(isIMEIexist[hash(_IMEI)] == true);
        require(isPhoneNumberexist[hash(_phoneNumber)] == true);
        require(mapAPI[msg.sender][hash(_phoneNumber)] == hash(_IMEI));
        mapAPI[msg.sender][hash(_phoneNumber)] = hash(uint(0));
        mapAPI[msg.sender][hash(_newPhoneNumber)] = hash(_IMEI);
        isPhoneNumberexist[hash(_phoneNumber)] = false;
    }

    function checkIMEI(uint _IMEI) public view returns(bool){
        return isIMEIlost[hash(_IMEI)];
    }

}
```

### Smart Contract - JavaScript
```js
const Web3 = require('web3');
const web3 = new Web3('http://localhost:8545'); // your Blockchain client endpoint

const contractAddress = '0x123456789...'; // your contract address
const abi = [/* Smart Contract ABI */]; // your contract ABI

const contract = new web3.eth.Contract(abi, contractAddress);

const isIMEIexist = {};
const isPhoneNumberexist = {};
const mapAPI = {};
const isIMEIlost = {};

function hash(value) {
  return web3.utils.keccak256(web3.eth.abi.encodeParameter('uint256', value));
}

async function addIMEI(IMEI, phoneNumber) {
  if (!isIMEIexist[hash(IMEI)] && !isPhoneNumberexist[hash(phoneNumber)]) {
    isIMEIexist[hash(IMEI)] = true;
    isPhoneNumberexist[hash(phoneNumber)] = true;
    mapAPI[web3.eth.defaultAccount][hash(phoneNumber)] = hash(IMEI);
    await contract.methods.addIMEI(IMEI, phoneNumber).send({ from: web3.eth.defaultAccount });
  }
}

async function activateLost(phoneNumber) {
  const IMEI = mapAPI[web3.eth.defaultAccount][hash(phoneNumber)];
  if (isIMEIexist[IMEI]) {
    isIMEIlost[IMEI] = true;
    await contract.methods.activateLost(phoneNumber).send({ from: web3.eth.defaultAccount });
  }
}

async function deactivateLost(phoneNumber) {
  const IMEI = mapAPI[web3.eth.defaultAccount][hash(phoneNumber)];
  if (isIMEIexist[IMEI]) {
    isIMEIlost[IMEI] = false;
    await contract.methods.deactivateLost(phoneNumber).send({ from: web3.eth.defaultAccount });
  }
}

async function changeIMEI(IMEI, phoneNumber, newIMEI) {
  if (isIMEIexist[hash(IMEI)] && isPhoneNumberexist[hash(phoneNumber)] && mapAPI[web3.eth.defaultAccount][hash(phoneNumber)] === hash(IMEI)) {
    mapAPI[web3.eth.defaultAccount][hash(phoneNumber)] = hash(newIMEI);
    isIMEIexist[hash(IMEI)] = false;
    if (!isIMEIexist[hash(newIMEI)]) {
      isIMEIexist[hash(newIMEI)] = true;
    }
    await contract.methods.changeIMEI(IMEI, phoneNumber, newIMEI).send({ from: web3.eth.defaultAccount });
  }
}

async function changePhoneNumber(IMEI, phoneNumber, newPhoneNumber) {
  if (isIMEIexist[hash(IMEI)] && isPhoneNumberexist[hash(phoneNumber)] && mapAPI[web3.eth.defaultAccount][hash(phoneNumber)] === hash(IMEI)) {
    mapAPI[web3.eth.defaultAccount][hash(phoneNumber)] = hash(0);
    mapAPI[web3.eth.defaultAccount][hash(newPhoneNumber)] = hash(IMEI);
    isPhoneNumberexist[hash(phoneNumber)] = false;
    await contract.methods.changePhoneNumber(IMEI, phoneNumber, newPhoneNumber).send({ from: web3.eth.defaultAccount });
  }
}

async function checkIMEI(IMEI) {
  return isIMEIlost[hash(IMEI)];
}

module.exports = {
  addIMEI,
  activateLost,
  deactivateLost,
  changeIMEI,
  changePhoneNumber,
  checkIMEI
};
```

The smart contract consists of six functions that can be called by authorized users.
- `addIMEI()`  allows users to add their mobile devices to the blockchain by passing in their IMEI and phone numbers. The function first checks if the IMEI and phone numbers already exist on the blockchain, and if not, it adds the device to the mapping function.
- `activateLost()`  is used to activate the lost mode of a mobile device. The function checks if the IMEI number of the device exists on the blockchain and if it does, it sets the value of  `isIMEIlost` to true, indicating that the device is lost.
- `deactivateLost()` is used to deactivate the lost mode of a mobile device. The function checks if the IMEI number of the device exists on the blockchain and if it does, it sets the value of `isIMEIlost` to false, indicating that the device is no longer lost.
- `changeIMEI()` allows users to change the IMEI number of their device. The function checks if the old IMEI and phone number exists on the blockchain and if it does, it replaces the old IMEI with the new one.
- `changePhoneNumber()` allows users to change the phone number associated with their device. The function checks if the old IMEI and phone number exists on the blockchain and if it does, it replaces the old phone number with the new one.
- `checkIMEI()` is a view function that allows anyone to check if a particular device is lost by passing in the IMEI number of the device. The function returns true if the device is lost, and false if it is not.

## Potential Impact
As the world continues to advance technologically, mobile phone theft has become a common issue that affects many people. However, with the implementation of a blockchain-based mobile theft prevention solution, it is possible to mitigate this problem.

## Potential Impact on Users and Mobile Manufacturers
For users, this solution provides an added layer of security, ensuring that their mobile devices cannot be easily used if they are lost or stolen. With the mobile application continuously reading the state of the mobile through API calls to the blockchain, it is possible to detect if the mobile is stolen, and take appropriate actions to disable the mobile network, Wi-Fi, and force activate airplane mode, preventing the thief from using any of the phone’s functionalities.

For mobile manufacturers, implementing blockchain-based mobile theft prevention solution will increase customer satisfaction and retention as users are likely to be attracted to the added security feature. This, in turn, will lead to an increase in sales and profits.

## Potential Economic and Social Benefits
The implementation of blockchain-based mobile theft prevention solutions will lead to a reduction in mobile phone theft and related crimes. This will result in a decrease in the costs of replacing stolen or lost mobile phones, and a corresponding increase in the amount of money available for investment in other areas of the economy. Additionally, it can also help to reduce insurance premiums for mobile phone owners, leading to savings for consumers.

On a social level, it can help to reduce the fear of being robbed or mugged and reduce the potential for violent confrontations between victims and thieves. This can lead to an overall improvement in public safety and security.

## Future Possibilities and Extensions
The implementation of this blockchain-based mobile theft prevention solution has future possibilities and extensions. It can be extended to other mobile devices like laptops, tablets, and smartwatches, further increasing the level of security for users. Additionally, it can be integrated with existing law enforcement agencies to enhance the tracking of lost or stolen mobile devices. This will make it easier for law enforcement to recover stolen mobile devices and increase the likelihood of criminals being brought to justice.

In conclusion, the implementation of blockchain-based mobile theft prevention solutions provides an added layer of security that can greatly benefit mobile phone users, manufacturers, and society at large. The potential for future extensions and possibilities only adds to its value, making it an ideal solution for improving the safety and security of mobile devices.