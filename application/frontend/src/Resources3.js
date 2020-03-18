import React, { Component, Fragment } from 'react';
import Typography from '@material-ui/core/Typography';
import { AppBar, Toolbar, ListItemText } from '@material-ui/core';
import TextField from '@material-ui/core/TextField'
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import CreateDialog from './CreateDialog.js';
import InstanceName from './InstanceName.js';
import { makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';

import { IconButton } from 'material-ui';
import { Delete } from '@material-ui/icons';


import List from '@material-ui/core/ListItem';

import { Paper } from '@material-ui/core';



const useStyles = makeStyles({
    table: {
        minWidth: 650,
    },
});


export default class Resources3 extends Component {
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
        //   const classes = useStyles();

        return (

            <MuiThemeProvider>
                <AppBar position='relative' style={style} >
                    <Toolbar  >
                        <Typography variant='subtitle1' color="scondary" style={{ flex: 3, background: '##FFFFFF' }}>
                            Enter EC2 instance details to monitor
                            </Typography>
                        <CreateDialog onCreate={this.parentCallBack} />
                    </Toolbar>
                </AppBar>
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
                                instanceNames.map(insta =>
                                    <TableRow key={insta}>
                                        <TableCell component="th" scope="row">
                                            {insta}
                                        </TableCell>
                                        <TableCell>
                                            <IconButton>
                                                <Delete />
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