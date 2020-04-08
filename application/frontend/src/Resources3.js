import React, { Component, Fragment } from 'react';
import Typography from '@material-ui/core/Typography';
import { AppBar, Toolbar, ListItemText } from '@material-ui/core';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import CreateDialog from './CreateDialog.js';
import { makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import { IconButton } from 'material-ui';
import { Delete } from '@material-ui/icons';
import { Paper } from '@material-ui/core';
import axios from 'axios';
import { Button } from '@material-ui/core';
import TextField from 'material-ui/TextField';

var apiBaseUrl="https://cloudanalyser.info/api";

const useStyles = makeStyles({
    table: {
        minWidth: 650,
    },
});

export default class Resources3 extends Component {

    constructor(props) {
        super(props);
        this.state = {
            // ec2: [],
            tenancyName: '',
            userId: props.userId,
            instanceNames: [],
            instanceId: []

        }
    }

    parentCallBack = insta => {
        console.log(insta);
        console.log("Callback");
        //    this.setState({
        //        instanceNames : insta
        //    })

        this.setState(({ instanceNames }) => ({
            instanceNames: [
                ...instanceNames,
                insta
            ]
        }))

    }

    componentWillMount() {
        console.log("prop values componentWillMount");
        var printcount;
        //set upload limit based on user role
        var self = this;
        var instanceNamesTemp = [];
        var instanceIdTemp = [];
        this.setState({ instanceNames: instanceNamesTemp });
        // this.state.instanceNames = instanceNamesTemp;
        //this.state.isLoaded= true;
        axios.get(apiBaseUrl + "/ec2/id?userId=" + this.props.userId)
            .then(function (response) {
                console.log("Get successfull" + response.data[0].id);
                instanceNamesTemp = [];
                for (let i = 0; i < response.data.length; i++) {
                    instanceNamesTemp[i] = response.data[i].ec2InstanceName;
                    instanceIdTemp[i] = response.data[i].id;

                }
                console.log("Get successfull Processing the input data" + instanceNamesTemp);
                self.setState({ instanceNames: instanceNamesTemp });
                self.setState({ instanceId: instanceIdTemp });
                console.log("instanceIdTemp" + instanceIdTemp);
                //self.state.instanceIdself.state.instanceId=instanceIdTemp;
            })
            .catch(function (error) {
                console.log(error);
            });
        console.log("Get successfull Processing the input data test" + instanceNamesTemp);
        console.log("instanceIdTemp" + instanceIdTemp);
        this.state.instanceNames = instanceNamesTemp;
        this.state.instanceId = instanceIdTemp;
        console.log("this.state.instanceId" + this.state.instanceId);
        // this.state.isLoaded= true;
    }

    handleSaveTenancy = () => {

       // const { instance } = this.state;

        //this.props.onCreate(instance);

        var self = this;
        console.log("prop values handlesubmit");
        alert(this.state.tenancyName);
        var payload = {
            //"name":this.state.username,
            // "emailId":this.state.password,
            // "userId":this.state.loginRole
         
            "tenancyName": this.state.tenancyName,
            "userId": this.props.userId
        }



        axios.post(apiBaseUrl + "/savetenancy", payload)
            .then(function (response) {
                console.log("Login successfull" + response.data);
            })
            .catch(function (error) {
                console.log(error);
            });



    }

    handlesubmit = (value) => {

        const { instance } = this.state;

        console.log("value" + value);
        console.log("this.state.instanceId" + this.state.instanceId);


        //this.props.onCreate(instance);

        var self = this;
        console.log("prop values handlesubmit" + value);
        this.state.instanceId[value];
        console.log("this.state.instanceId" + this.state.instanceId[value]);
        var payload = {
            //"name":this.state.username,
            // "emailId":this.state.password,
            // "userId":this.state.loginRole

            "name": 'Raji',
            "emailId": 'raji@gmail.com',
            "userId": this.props.userId,
            "ec2InstanceValue": value,
            "ec2InstanceId": this.state.instanceId[value]
        }
        axios.post(apiBaseUrl + "/id/delete", payload)
            .then(function (response) {


                console.log("Login successfull" + response.data);
            })
            .catch(function (error) {
                console.log(error);
            });


        setTimeout(() => {
            this.componentWillMount()
        }, 1000);


        var self = this;
        var instanceNamesTemp = [];
        var instanceIdTemp = [];
        // this.setState({instanceNames:instanceNamesTemp});
        // this.state.instanceNames = instanceNamesTemp;
        //this.state.isLoaded= true;

        //  axios.get(apiBaseUrl+"listall")
        // .then(function (response) {
        // console.log("Get successfull"+response.data[0].id);
        //   instanceNamesTemp =  [];
        //   for (let i = 0; i < response.data.length; i++) {
        //  instanceNamesTemp[i] = response.data[i].ec2InstaneName;
        //   instanceIdTemp[i] = response.data[i].id;

        //  }
        // console.log("Get successfull Processing the input data"+instanceNamesTemp);
        //  self.setState({instanceNames:instanceNamesTemp});
        // self.setState({instanceId:instanceIdTemp});
        //self.state.instanceId=instanceIdTemp;
        //})
        //.catch(function (error) {
        //console.log(error);
        //});   
    }



    render() {

        // const { instanceNames } = this.state;
        //   const classes = useStyles();
        console.log("prop values render" + this.state.isLoaded);
        console.log(this.props.appContext);
        console.log("User Id" + this.state.userId);
        // console.log("prop values render"+instanceNames);

        //var  instanceNamesTemp =  ['ABCD','1234'];
        //this.state.instanceNames = instanceNamesTemp;
        // this.state.instanceNames.insta = instanceNamesTemp;  
        const { instanceNames } = this.state;
        const { instanceId } = this.state;

        return (

            <MuiThemeProvider>
                <TextField style={{ marginRight: 10 }}
                    hintText="Enter your tenancy details"
                    onChange={(event, newValue) => this.setState({ tenancyName: newValue })}
                />

                <Button variant="contained" color="primary" onClick={(event) => this.handleSaveTenancy(event)}>
                    Save
                    </Button>
                <AppBar position='relative' style={style} >
                    <Toolbar  >
                        <Typography variant='subtitle1' color="scondary" style={{ flex: 3, background: '##FFFFFF' }}>
                            Enter EC2 instance details to monitor
                            </Typography>
                        <CreateDialog onCreate={this.parentCallBack}  userId={this.props.userId}/>
                    </Toolbar>
                </AppBar>







                <br />

                <TableContainer component={Paper}>
                    <Table aria-label="simple table">
                        <TableHead>
                            <TableRow>
                                <TableCell>EC2</TableCell>
                                <TableCell>Delete</TableCell>
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            {
                                instanceNames.map((insta, index) =>

                                    <TableRow key={insta}>
                                        <TableCell component="th" scope="row">
                                            {insta}
                                        </TableCell>
                                        <TableCell>
                                            <IconButton>
                                                <Delete onClick={() => this.handlesubmit(index)} />
                                            </IconButton>
                                        </TableCell>

                                    </TableRow>
                                )}
                        </TableBody>
                    </Table>
                </TableContainer>
            </MuiThemeProvider>
        );

    }
}

const style = {
    margin: 15,
    padding: 5,
    marginTop: 5,
    marginBottom: 5,
    marginLeft: 0,
    align: 'center',
    background: '#87CEFA'
};