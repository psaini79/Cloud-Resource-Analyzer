import React, { Component, Fragment } from 'react';
import Typography from '@material-ui/core/Typography';
import { AppBar, Toolbar, Button } from '@material-ui/core';
import TextField from '@material-ui/core/TextField'
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import { ListItem, IconButton, List, ListItemText } from 'material-ui';
import { Delete } from '@material-ui/icons';

class Header1 extends Component {

    render() {
        return (

          <div>
                <AppBar position='relative' style={style} >
                    <Toolbar >
                        <Typography style={{ flex: 1 }} >  <h2>   Cloud Resource Analyzer - Monitor and Analyze Workload  </h2>  </Typography>
                        
                        <Button variant="contained" color="primary">
                            Logout
                    </Button>
                    
                    </Toolbar>

                </AppBar>
                </div>
          

        )
    }
}


const style = {
    margin: 0,
    padding: 5,
    marginTop: 0,
    marginBottom: 5,
    marginLeft: 0
   
};

export default  Header1;