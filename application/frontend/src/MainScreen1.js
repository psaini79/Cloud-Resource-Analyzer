
import React, { Component, Fragment } from 'react';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import { Button } from '@material-ui/core';
import TextField from 'material-ui/TextField';
import axios from 'axios';


var apiBaseUrl = "http://129.146.192.214:8080/";
//var apiBaseUrl = "http://localhost:8080";

class TriggerML extends Component {


    constructor(props) {
        super(props);
        this.state = {
            // ec2: [],
            period: '',
            userId: props.userId

        }
    }

    handleTriggerML = () => {

        // const { instance } = this.state;

        //this.props.onCreate(instance);

        var self = this;
        //   console.log("prop values handlesubmit");
        alert(this.props.userId);
        var payload = {
          
            "period": this.state.period,
            "userId": this.props.userId
        }



        axios.post(apiBaseUrl + "/trigger_ml", payload)
            .then(function (response) {
                console.log("Trigger sucessfull" + response.data);
            })
            .catch(function (error) {
                console.log(error);
            });



    }

    render() {
        return (

            <MuiThemeProvider>
                <TextField style={{ marginRight: 10 }}
                    hintText="Enter the number of days to forecast"
                    onChange={(event, newValue) => this.setState({ period: newValue })}
                />

                <Button variant="contained" color="primary" onClick={(event) => this.handleTriggerML(event)} >
                    Trigger
                </Button>
            </MuiThemeProvider>

        )




    }


}





export default TriggerML;