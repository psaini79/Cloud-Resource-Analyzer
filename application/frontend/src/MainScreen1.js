import React, { Fragment } from 'react';
import PropTypes from 'prop-types';
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';
import Typography from '@material-ui/core/Typography';
import Box from '@material-ui/core/Box';
import Grafana from './Grafana';
import Resources3 from './Resources3';
import Header1 from './Header1';
import TriggerML from './TriggerML';
function TabPanel(props) {


  const { children, value, index, ...other } = props;


  return (
    <Typography
      component="div"
      role="tabpanel"
      hidden={value !== index}
      id={`simple-tabpanel-${index}`}
      aria-labelledby={`simple-tab-${index}`}
      {...other}
    >
      {value === index && <Box p={3}>{children}</Box>}
    </Typography>
  );
}

TabPanel.propTypes = {
  children: PropTypes.node,
  index: PropTypes.any.isRequired,
  value: PropTypes.any.isRequired,
};

function a11yProps(index) {
  return {
    id: `simple-tab-${index}`,
    'aria-controls': `simple-tabpanel-${index}`,
  };
}

const useStyles = makeStyles(theme => ({
  root: {
    flexGrow: 1,
    //   backgroundColor: theme.palette.background.paper,
  },
}));

export default function SimpleTabs(props) {

  console.log("User Id in Simple  " + props.userId);
  const classes = useStyles();
  const [value, setValue] = React.useState(0);

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  return (

    <Fragment >
      <div  >

        <Header1 />

        <AppBar position="relative" style={style}>
          <Tabs value={value} onChange={handleChange} aria-label="simple tabs example">
            <Tab label="ENTER RESOURCES" {...a11yProps(0)} />
            <Tab label="CURRENT WORKLOAD" {...a11yProps(1)} />
            <Tab label="FORECAST" {...a11yProps(2)} />
          </Tabs>
        </AppBar>
        <TabPanel value={value} index={0}>
          <Resources3 userId={props.userId} />
        </TabPanel>
        <TabPanel value={value} index={1}>
          <Grafana />
        </TabPanel>
        <TabPanel value={value} index={2}>
        <TriggerML userId={props.userId}/>
          <Grafana />
        </TabPanel>
      </div>
    </Fragment>



  );

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

