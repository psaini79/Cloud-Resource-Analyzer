
import React, { Component, Fragment } from 'react';



class TriggerML extends Component {


    render() {
        return (

            <MuiThemeProvider>
                <TextField style={{ marginRight: 10 }}
                    hintText="Enter the number of days to forecast"
                />

                <Button variant="contained" color="primary" >
                    Trigger
                </Button>
            </MuiThemeProvider>

        )




    }


}





export default TriggerML;