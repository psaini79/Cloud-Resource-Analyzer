import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';
import AppBar from 'material-ui/AppBar';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';

const useStyles = makeStyles({
  root: {
    flexGrow: 1,
  },
});

export default function CenteredTabs() {
  const classes = useStyles();
  const [value, setValue] = React.useState(0);

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  return (

   <div>
         <MuiThemeProvider key={"theme"}>
        <AppBar 
             title="Cloud Resource Analyzer - 
                    Monitor and Analyze Cloud Resources"
           />
        </MuiThemeProvider>
   

    <Paper className={classes.root}>
         
      <Tabs
        value={value}
        onChange={handleChange}
        indicatorColor="primary"
        textColor="primary"
        centered
      >
        <Tab label="EC2 Information" > Raji</Tab>
        <Tab label="Current Workload" />
        <Tab label="Forecast" />
      </Tabs>
    </Paper>
    </div>
  );
}


