import React, { Component } from 'react';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import AppBar from 'material-ui/AppBar';
import RaisedButton from 'material-ui/RaisedButton';
import TextField from 'material-ui/TextField';
import axios from 'axios';
import Login from './Login';

class Register extends Component {
  constructor(props) {
    super(props);
    this.state = {
      firstName: "",
      lastName: '',
      userId: '',
      password: '',
      emailId: '',
      role: '',
      designation: '',
      mobileNum: ''
    }
  }
  componentWillReceiveProps(nextProps) {
    console.log("nextProps", nextProps);
  }
  handleClick(event, role) {
    var apiBaseUrl="https://cloudanalyser.info/api";
    var self = this;
    //To be done:check for empty values before hitting submit
    //  if(this.state.firstName.length>0 && this.state.lastName.length>0 && this.state.email.length>0 && this.state.password.length>0){
    var payload = {
      "firstName": this.state.firstName,
      "lastName": this.state.lastName,
      "userId": this.state.userId,
      "password": this.state.password,
      "emailId": this.state.emailId,
      "role": this.state.role,
      "designation": this.state.designation,
      "mobileNum": this.state.mobileNum,
    }
    axios.post(apiBaseUrl + '/register', payload)
      .then(function (response) {
        console.log(response);
        if (response.data === 'Success') {
          console.log("registration successfull");
          alert("Registration completed successfullt");
          var loginscreen = [];
          loginscreen.push(<Login parentContext={this} appContext={self.props.appContext} role={role} />);
          var loginmessage = "Registered Successfully";
          self.props.parentContext.setState({
            loginscreen: loginscreen,
            loginmessage: loginmessage,
            buttonLabel: "Register",
            isLogin: true
          });
        }
        else {
          console.log("some error ocurred", response.data);
          var loginscreen = [];
          // loginscreen.push(<Login parentContext={this} appContext={self.props.appContext} role={role}/>);
          // var loginmessage = "Not Registered yet.Go to registration -"+response.data;
          self.props.parentContext.setState({
            //loginscreen:loginscreen,
            loginmessage: "Registration Error " + response.data,
            buttonLabel: "Register",
            isLogin: true
          });
          // this.setState({loginmessage:"Registration Error"+response.data});
        }
      })
      .catch(function (error) {
        console.log(error);
      });
    // }
    // else{
    // alert("Input field value is missing");
    // }

  }
  render() {
    // console.log("props",this.props);
    var userhintText, userLabel;
    if (this.props.role === "user") {
      userhintText = "Enter your User Id";
      userLabel = "User Id";
    }
    else {
      userhintText = "Enter your User Id";
      userLabel = "Teacher Id";
    }
    return (
      <div>
        <MuiThemeProvider>
          <div>
            <AppBar
              title="Register"
            />
            <TextField
              hintText="Enter your First Name"
              floatingLabelText="First Name"
              onChange={(event, newValue) => this.setState({ firstName: newValue })}
            />
            <br />
            <TextField
              hintText="Enter your Last Name"
              floatingLabelText="Last Name"
              onChange={(event, newValue) => this.setState({ lastName: newValue })}
            />
            <br />
            <TextField
              hintText={userhintText}
              floatingLabelText={userLabel}
              onChange={(event, newValue) => this.setState({ userId: newValue })}
            />
            <br />
            <TextField
              type="password"
              hintText="Enter your Password"
              floatingLabelText="Password"
              onChange={(event, newValue) => this.setState({ password: newValue })}
            />
            <br />
            <TextField
              hintText="Enter your Email Id"
              floatingLabelText="Email Id"
              onChange={(event, newValue) => this.setState({ emailId: newValue })}
            />
            <br />
            <TextField
              hintText="Enter your Role"
              floatingLabelText="Role"
              onChange={(event, newValue) => this.setState({ role: newValue })}
            />
            <br />
            <TextField
              hintText="Enter your Designation"
              floatingLabelText="Designation"
              onChange={(event, newValue) => this.setState({ designation: newValue })}
            />
            <br />
            <TextField
              hintText="Enter your Mobile Number"
              floatingLabelText="Mobile Number"
              onChange={(event, newValue) => this.setState({ mobileNum: newValue })}
            />
            <br />
            <RaisedButton label="Submit" primary={true} style={style} onClick={(event) => this.handleClick(event, this.props.role)} />
          </div>
        </MuiThemeProvider>
      </div>
    );
  }
}

const style = {
  margin: 15,
};

export default Register;
