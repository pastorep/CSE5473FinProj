import React, { Component } from 'react';
import './App.css';

import 'antd/dist/antd.css';
import { Form, Icon, Input, Button, Row, Col } from 'antd';

class App extends Component {
  render() {
    var ip = request.connection.remoteAddress
    return (
      <div className="App">
      <Row>
      <Col span={24}>
          <img src="http://cache.marriott.com/Images/TNG/marriott_logo_gray.png"
          className="hotel-logo"
          alt="logo"
          align="left"
          />
          </Col>
      </Row>
      <Row>
          <Col span={12}>
          <br/>
          <p align="left"><b>
          Please Connect to the Hotel Network{"\n"}
          </b></p>
          <p align="left">
          To upgrade to Enhanced Internet, you must first connect to the wireless network. To do so:
          <br/>
          &nbsp;&nbsp;&nbsp;&nbsp;
          - Open your wireless utility or “Settings” app for Wi-Fi connections
          <br/>
          &nbsp;&nbsp;&nbsp;&nbsp;
          - Select the guest network listed for your hotel
          <br/>
          &nbsp;&nbsp;&nbsp;&nbsp;
          - Re-enter the upgrade link: <a>internetupgrade.marriott.com</a>
          <br/>
          <br/>


          <form action="http://localhost:5000/" method="post" role="form">
            <label>
              Name:
              <br/><input type="text" name="name" />
            </label>
            <br/><input type="submit" value="Submit" />
          </form>

          <br/>
            If you are not currently at a property, then we invite you to visit Marriott.com to make a reservation, find a vacation deal, or explore our more than 6000 properties worldwide.
          </p>
          </Col>
      </Row>
      </div>
    );
  }
}

export default App;
