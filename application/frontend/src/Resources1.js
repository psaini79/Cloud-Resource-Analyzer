import React, { Component, Fragment } from 'react';
import Typography from '@material-ui/core/Typography';
import { AppBar, Toolbar, ListItemText } from '@material-ui/core';
import TextField from '@material-ui/core/TextField'
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import CreateDialog from './CreateDialog.js';
import InstanceName from './InstanceName.js';


import List from '@material-ui/core/ListItem';

import { Paper } from '@material-ui/core';

export default class Resources1 extends Component {
    state = {
        ec2: [],
        tenancy: '',
        instanceNames: []

    }

    parentCallBack = insta => {
        console.log(insta);
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

    render() {
        const { instanceNames } = this.state;

        return (
            <Paper width="50%">
                <MuiThemeProvider>
                    <AppBar position='relative' style={style} >
                        <Toolbar  >
                            <Typography variant='subtitle1' color="scondary" style={{ flex: 3, background: '##FFFFFF' }}>
                                Enter EC2 instance details to monitor
                            </Typography>
                            <CreateDialog onCreate={this.parentCallBack} />
                        </Toolbar>
                    </AppBar>


                  

                        {
                            instanceNames.map(insta => 
                                <InstanceName insta={insta}></InstanceName>
                            )}

                
                </MuiThemeProvider>
            </Paper>



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