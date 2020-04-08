import React, { Component } from 'react';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import AppBar from 'material-ui/AppBar';
import RaisedButton from 'material-ui/RaisedButton';
import TextField from 'material-ui/TextField';
import axios from 'axios';
import SimpleTabs from './MainScreen1';
var apiBaseUrl="https://cloudanalyser.info/api";

class Login extends Component {
  constructor(props) {
    super(props);
    var localloginComponent = [];
    localloginComponent.push(
      <MuiThemeProvider key={"theme"} >
        <div>
          <TextField
            hintText="Enter your user id"
            floatingLabelText="User Id"
            onChange={(event, newValue) => this.setState({ username: newValue })}
          />
          <br />
          <TextField
            type="password"
            hintText="Enter your password"
            floatingLabelText="Password"
            onChange={(event, newValue) => this.setState({ password: newValue })}
          />
          <br />
          <RaisedButton label="Submit" primary={true} style={style} onClick={(event) => this.handleClick(event)} />
        </div>
      </MuiThemeProvider>
    )
    this.state = {
      username: '',
      password: '',
      // menuValue:1,
      loginComponent: localloginComponent,
      loginRole: 'user'
    }
  }
  componentWillMount() {
    // console.log("willmount prop values",this.props);
    if (this.props.role !== undefined) {
      if (this.props.role === 'user') {
        console.log("in user componentWillMount");
        var localloginComponent = [];
        localloginComponent.push(
          <MuiThemeProvider>
            <div>
              <TextField
                hintText="Enter your user "
                floatingLabelText="User Id"
                onChange={(event, newValue) => this.setState({ username: newValue })}
              />
              <br />
              <TextField
                type="password"
                hintText="Enter your Password"
                floatingLabelText="Password"
                onChange={(event, newValue) => this.setState({ password: newValue })}
              />
              <br />
              <RaisedButton label="Submit" primary={true} style={style} onClick={(event) => this.handleClick(event)} />
            </div>
          </MuiThemeProvider>
        )
        this.setState({ menuValue: 1, loginComponent: localloginComponent, loginRole: 'user' })
      }
    }
  }
  handleClick(event) {


    var self = this;
    var userIdTemp = this.state.username;
    var payload = {
      "userId": this.state.username,
      "password": this.state.password,
    }
    var uploadScreen = [];
    var loginPage = [];
    axios.post(apiBaseUrl + '/login', payload)
      .then(function (response) {
        console.log(response);
        if (response.data === 'Success') {
          console.log("Login successfully");

          uploadScreen.push(<SimpleTabs userId={userIdTemp} />)
          self.props.appContext.setState({ loginPage: [], uploadScreen: uploadScreen })

          //var uploadScreen=[];
          // uploadScreen.push(<UploadPage appContext={self.props.appContext} role={self.state.loginRole}/>)
          // self.props.appContext.setState({loginPage:[],uploadScreen:uploadScreen})
        }
        else if (response.data.code === 204) {
          console.log("Username password do not match");
          alert(response.data.success)
        }
        else {
          console.log("Username does not exists");
          alert("Username does not exist");
        }
      })
      .catch(function (error) {
        console.log(error);
      });


    //   axios.post(apiBaseUrl+'login', payload)
    //  .then(function (response) {
    //    console.log(response);
    //    if(response.data.code == 200){
    //      console.log("Login successfull");
    //      var uploadScreen=[];
    //      uploadScreen.push(<UploadPage appContext={self.props.appContext} role={self.state.loginRole}/>)
    //      self.props.appContext.setState({loginPage:[],uploadScreen:uploadScreen})
    //    }
    //    else if(response.data.code == 204){
    //      console.log("Username password do not match");
    //      alert(response.data.success)
    //    }
    //    else{
    //      console.log("Username does not exists");
    //      alert("Username does not exist");
    //    }
    //  })
    //  .catch(function (error) {
    //    console.log(error);
    //  });
  }
  // handleMenuChange(value){
  //   console.log("menuvalue",value);
  //   var loginRole;
  //   if(value==1){
  //     var localloginComponent=[];
  //     loginRole='student';
  //     localloginComponent.push(
  //       <MuiThemeProvider>
  //         <div>
  //          <TextField
  //            hintText="Enter your College Rollno"
  //            floatingLabelText="Student Id"
  //            onChange = {(event,newValue) => this.setState({username:newValue})}
  //            />
  //          <br/>
  //            <TextField
  //              type="password"
  //              hintText="Enter your Password"
  //              floatingLabelText="Password"
  //              onChange = {(event,newValue) => this.setState({password:newValue})}
  //              />
  //            <br/>
  //            <RaisedButton label="Submit" primary={true} style={style} onClick={(event) => this.handleClick(event)}/>
  //        </div>
  //        </MuiThemeProvider>
  //     )
  //   }
  //   else if(value == 2){
  //     var localloginComponent=[];
  //     loginRole='teacher';
  //     localloginComponent.push(
  //       <MuiThemeProvider>
  //         <div>
  //          <TextField
  //            hintText="Enter your College Rollno"
  //            floatingLabelText="Teacher Id"
  //            onChange = {(event,newValue) => this.setState({username:newValue})}
  //            />
  //          <br/>
  //            <TextField
  //              type="password"
  //              hintText="Enter your Password"
  //              floatingLabelText="Password"
  //              onChange = {(event,newValue) => this.setState({password:newValue})}
  //              />
  //            <br/>
  //            <RaisedButton label="Submit" primary={true} style={style} onClick={(event) => this.handleClick(event)}/>
  //        </div>
  //        </MuiThemeProvider>
  //     )
  //   }
  //   this.setState({menuValue:value,
  //                  loginComponent:localloginComponent,
  //                  loginRole:loginRole})
  // }
  render() {
    return (
      <div>
        <MuiThemeProvider>

          <AppBar
            title="Cloud Resource Analyzer - 
                    Monitor and Analyze Cloud Resources"
          />
        </MuiThemeProvider>
        <MuiThemeProvider>
          <div>
            <p>Login</p>
            {/* <DropDownMenu value={this.state.menuValue} onChange={(event,index,value)=>this.handleMenuChange(value)}>
          <MenuItem value={1} primaryText="Student" />
          <MenuItem value={2} primaryText="Teacher" />
        </DropDownMenu> */}
          </div>
        </MuiThemeProvider>
        {this.state.loginComponent}
      </div>
    );
  }
}

const style = {
  margin: 15,
};

export default Login;
