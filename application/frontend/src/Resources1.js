import React, { Component, Fragment } from 'react';
import Typography from '@material-ui/core/Typography';
import { AppBar, Toolbar, ListItemText } from '@material-ui/core';
import TextField from '@material-ui/core/TextField'
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import CreateDialog from './CreateDialog.js';
import { Delete } from '@material-ui/icons';
import { ListItem, IconButton } from 'material-ui';
import List from '@material-ui/core/ListItem';
import ListItemSecondaryAction from '@material-ui/core/ListItemSecondaryAction';
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
            <div>
                <MuiThemeProvider>
                    <AppBar position='relative' style={style} >
                        <Toolbar  >
                            <Typography variant='subtitle1' color="scondary" style={{ flex: 3, background: '##FFFFFF' }}>
                                Enter EC2 instance details to monitor
                            </Typography>
                            <CreateDialog onCreate={this.parentCallBack} />
                        </Toolbar>
                    </AppBar>

                    <List component="ul">

                    {
                        instanceNames.map(insta => {
                            return (
                                
                                    <ListItem>
                                        <ListItemText primary={insta}>
                                        </ListItemText >

                                      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                      

                                        <ListItemSecondaryAction>
                                            <IconButton >
                                                <Delete />
                                            </IconButton>
                                        </ListItemSecondaryAction>
                                        
                                    </ListItem>
                                                                                                    
                            );
                        })}

</List>

                </MuiThemeProvider>
            </div>



        );
    }
}



const style = {
    margin: 15,
    padding: 5,
    marginTop: 5,
    marginBottom: 5,
    marginLeft: 15,
    align: 'center',
    background: '#87CEFA'
};