import React from 'react';
import { List, IconButton } from 'material-ui';
import { Delete } from '@material-ui/icons';
import nextId from "react-id-generator";

function InstanceName({ insta }) {
    const id1 = nextId();
    return (
        <List>
            <span >

                <p>{insta}</p>  <IconButton ><Delete /></IconButton>
            </span>
        </List>


    );
}

export default InstanceName;