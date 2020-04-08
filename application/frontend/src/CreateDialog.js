import React, { Component, Fragment } from 'react';

import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import { Add, VerticalAlignTop } from '@material-ui/icons';
import axios from 'axios';

var apiBaseUrl="https://cloudanalyser.info/api";

class CreateDialog extends Component {
    state = {
        open: false,
        instance: ''

    }

    handleToggle = () => {
        this.setState({
            open: !this.state.open
        })
    }

    handleChange = instance => event => {

        this.setState({
            [instance]: event.target.value,
        });

        console.log(instance);
    }

    handlesubmit = () => {

        const { instance } = this.state;

        this.props.onCreate(instance);

        var self = this;
        var payload = {
            //"name":this.state.username,
            // "emailId":this.state.password,
            // "userId":this.state.loginRole

            "name": 'Raji',
            "emailId": 'raji@gmail.com',
            "userId": this.props.userId,
            "ec2InstanceName": this.state.instance
        }
        axios.post(apiBaseUrl + '/saveec2instance', payload)
            .then(function (response) {
                console.log("Login successfull");
            })
            .catch(function (error) {
                console.log(error);
            });

    }
    render() {
        const { open } = this.state
        const { instance } = this.state
        return <Fragment>
            <Button variant="fab" onClick={this.handleToggle}  >
                <Add />
            </Button>

            <Dialog open={open}
                onClose={this.handleToggle}
            >
                <DialogTitle id="form-dialog-title">
                    Please enter EC2 instance names or ip
            </DialogTitle>
                <DialogContent>
                    <DialogContentText>
                        Please enter EC2 details
                      </DialogContentText>
                    <form>
                        <TextField
                            id="instance"
                            label="Instance"

                            value={this.state.instance}
                            onChange={this.handleChange('instance')}
                            margin="normal"
                        />
                    </form>
                </DialogContent>
                <DialogActions>
                    <Button color="primary" variant="raised" onClick={this.handlesubmit}>
                        Create
                      </Button>

                </DialogActions>
            </Dialog>


        </Fragment>
    }
}

export default CreateDialog;