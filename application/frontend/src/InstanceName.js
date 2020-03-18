import React from 'react';

import { List, ListItem, ListItemText, IconButton } from 'material-ui';
import ListItemSecondaryAction from '@material-ui/core/ListItemSecondaryAction';
import { Delete } from '@material-ui/icons';


function InstanceName({ insta }) {





    return (
<List>
        <span >

            <p>{insta}</p>  <IconButton ><Delete /></IconButton>

          


        </span>
        </List>


    );
}

export default InstanceName;